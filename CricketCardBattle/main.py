import os
import logging
import json
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from game_logic import GameLogic
from bot_ai import BotAI
from data import get_cricket_players

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "cricket-cards-secret-key")

# Initialize game components
game_logic = GameLogic()
bot_ai = BotAI()

@app.route('/')
def index():
    """Home page with game mode selection"""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game with selected mode"""
    mode = request.form.get('mode')
    cards_per_player = 20 if mode == 'quick' else 50
    
    # Get all players and shuffle
    all_players = get_cricket_players()
    
    # Initialize game state
    game_state = game_logic.initialize_game(all_players, cards_per_player)
    
    # Store in session
    session['game_state'] = game_state
    session['mode'] = mode
    
    return redirect(url_for('game'))

@app.route('/game')
def game():
    """Main game interface"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    
    # Check if game is over
    if game_logic.is_game_over(game_state):
        return redirect(url_for('result'))
    
    return render_template('game.html', game_state=game_state)

@app.route('/choose_stat', methods=['POST'])
def choose_stat():
    """Handle stat selection for the round"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    chosen_stat = request.form.get('stat')
    
    # Set the chosen stat for this round
    game_state['current_round']['chosen_stat'] = chosen_stat
    game_state['current_round']['phase'] = 'card_selection'
    
    # Track stat selection
    if 'user_stats' not in session:
        session['user_stats'] = {
            'games_played': 0, 'games_won': 0, 'rounds_played': 0, 'rounds_won': 0,
            'batting_selections': 0, 'bowling_selections': 0, 'fielding_selections': 0,
            'batting_rounds_won': 0, 'bowling_rounds_won': 0, 'fielding_rounds_won': 0,
            'batting_rounds_played': 0, 'bowling_rounds_played': 0, 'fielding_rounds_played': 0,
            'quick_games_played': 0, 'quick_games_won': 0, 'classic_games_played': 0, 'classic_games_won': 0,
            'current_streak': 0, 'best_streak': 0, 'game_history': []
        }
    
    # Only count user selections, not bot selections
    if game_state['current_round']['stat_chooser'] == 'user':
        stats = session['user_stats']
        if chosen_stat == 'batting':
            stats['batting_selections'] += 1
        elif chosen_stat == 'bowling':
            stats['bowling_selections'] += 1
        elif chosen_stat == 'fielding':
            stats['fielding_selections'] += 1
        session['user_stats'] = stats
    
    # If it's bot's turn to choose stat, let bot choose the best card
    if game_state['current_round']['stat_chooser'] == 'bot':
        bot_card = bot_ai.choose_card(game_state['bot_hand'], chosen_stat)
        game_state['current_round']['bot_card'] = bot_card
        game_state['bot_hand'].remove(bot_card)
    
    session['game_state'] = game_state
    return redirect(url_for('game'))

@app.route('/choose_card', methods=['POST'])
def choose_card():
    """Handle card selection by user"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    card_index = int(request.form.get('card_index'))
    
    # Get user's chosen card
    user_card = game_state['user_hand'][card_index]
    game_state['current_round']['user_card'] = user_card
    game_state['user_hand'].remove(user_card)
    
    # If bot hasn't chosen yet, let bot choose
    if 'bot_card' not in game_state['current_round']:
        chosen_stat = game_state['current_round']['chosen_stat']
        bot_card = bot_ai.choose_card(game_state['bot_hand'], chosen_stat)
        game_state['current_round']['bot_card'] = bot_card
        game_state['bot_hand'].remove(bot_card)
    
    session['game_state'] = game_state
    return redirect(url_for('compare_cards'))

@app.route('/compare_cards')
def compare_cards():
    """Compare cards and determine round winner"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    
    # Determine round winner
    round_result = game_logic.compare_cards(
        game_state['current_round']['user_card'],
        game_state['current_round']['bot_card'],
        game_state['current_round']['chosen_stat']
    )
    
    game_state['current_round']['result'] = round_result
    
    # Update scores and statistics
    if round_result['winner'] == 'user':
        game_state['user_score'] += 1
        game_state['current_round']['stat_chooser'] = 'user'
        update_round_stats('user', game_state['current_round']['chosen_stat'])
    elif round_result['winner'] == 'bot':
        game_state['bot_score'] += 1
        game_state['current_round']['stat_chooser'] = 'bot'
        update_round_stats('bot', game_state['current_round']['chosen_stat'])
    else:
        update_round_stats('tie', game_state['current_round']['chosen_stat'])
    # For ties, stat chooser remains the same
    
    session['game_state'] = game_state
    return render_template('round_result.html', game_state=game_state)

@app.route('/next_round', methods=['POST'])
def next_round():
    """Proceed to next round"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    
    # Check if game is over
    if game_logic.is_game_over(game_state):
        return redirect(url_for('result'))
    
    # Prepare for next round
    game_state['round_number'] += 1
    game_state['current_round'] = {
        'stat_chooser': game_state['current_round']['stat_chooser'],
        'phase': 'stat_selection'
    }
    
    # If it's bot's turn to choose stat, let bot choose
    if game_state['current_round']['stat_chooser'] == 'bot':
        chosen_stat = bot_ai.choose_stat(game_state['bot_hand'])
        game_state['current_round']['chosen_stat'] = chosen_stat
        game_state['current_round']['phase'] = 'card_selection'
    
    session['game_state'] = game_state
    return redirect(url_for('game'))

@app.route('/result')
def result():
    """Show final game results"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    game_state = session['game_state']
    
    # Update game completion statistics
    winner = game_logic.get_game_winner(game_state)
    mode = session.get('mode', 'quick')
    update_game_stats(winner, mode)
    
    return render_template('result.html', game_state=game_state)

@app.route('/new_game')
def new_game():
    """Start a new game"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/leaderboard')
def leaderboard():
    """Show player leaderboards"""
    players = get_cricket_players()
    
    # Calculate total stats for overall ranking
    for player in players:
        player['total'] = player['batting'] + player['bowling'] + player['fielding']
    
    # Top 15 in each category
    top_overall = sorted(players, key=lambda x: x['total'], reverse=True)[:15]
    top_batting = sorted(players, key=lambda x: x['batting'], reverse=True)[:15]
    top_bowling = sorted(players, key=lambda x: x['bowling'], reverse=True)[:15]
    top_fielding = sorted(players, key=lambda x: x['fielding'], reverse=True)[:15]
    
    # Quick stats
    total_players = len(players)
    avg_total = sum(p['total'] for p in players) / len(players)
    highest_total = max(p['total'] for p in players)
    
    return render_template('leaderboard.html',
                         top_overall=top_overall,
                         top_batting=top_batting,
                         top_bowling=top_bowling,
                         top_fielding=top_fielding,
                         total_players=total_players,
                         avg_total=avg_total,
                         highest_total=highest_total)

@app.route('/statistics')
def statistics():
    """Show user game statistics"""
    # Initialize default stats if not exists
    if 'user_stats' not in session:
        session['user_stats'] = {
            'games_played': 0,
            'games_won': 0,
            'rounds_played': 0,
            'rounds_won': 0,
            'batting_selections': 0,
            'bowling_selections': 0,
            'fielding_selections': 0,
            'batting_rounds_won': 0,
            'bowling_rounds_won': 0,
            'fielding_rounds_won': 0,
            'batting_rounds_played': 0,
            'bowling_rounds_played': 0,
            'fielding_rounds_played': 0,
            'quick_games_played': 0,
            'quick_games_won': 0,
            'classic_games_played': 0,
            'classic_games_won': 0,
            'current_streak': 0,
            'best_streak': 0,
            'game_history': []
        }
    
    stats = session['user_stats']
    
    # Calculate percentages
    win_rate = (stats['games_won'] / stats['games_played'] * 100) if stats['games_played'] > 0 else 0
    
    # Stat selection percentages
    total_selections = stats['batting_selections'] + stats['bowling_selections'] + stats['fielding_selections']
    batting_pct = (stats['batting_selections'] / total_selections * 100) if total_selections > 0 else 0
    bowling_pct = (stats['bowling_selections'] / total_selections * 100) if total_selections > 0 else 0
    fielding_pct = (stats['fielding_selections'] / total_selections * 100) if total_selections > 0 else 0
    
    # Win rates by stat
    batting_win_rate = (stats['batting_rounds_won'] / stats['batting_rounds_played'] * 100) if stats['batting_rounds_played'] > 0 else 0
    bowling_win_rate = (stats['bowling_rounds_won'] / stats['bowling_rounds_played'] * 100) if stats['bowling_rounds_played'] > 0 else 0
    fielding_win_rate = (stats['fielding_rounds_won'] / stats['fielding_rounds_played'] * 100) if stats['fielding_rounds_played'] > 0 else 0
    
    # Game mode win rates
    quick_win_rate = (stats['quick_games_won'] / stats['quick_games_played'] * 100) if stats['quick_games_played'] > 0 else 0
    classic_win_rate = (stats['classic_games_won'] / stats['classic_games_played'] * 100) if stats['classic_games_played'] > 0 else 0
    
    user_stats = {
        'games_played': stats['games_played'],
        'games_won': stats['games_won'],
        'win_rate': win_rate,
        'current_streak': stats['current_streak'],
        'batting_selections': int(batting_pct),
        'bowling_selections': int(bowling_pct),
        'fielding_selections': int(fielding_pct),
        'batting_win_rate': int(batting_win_rate),
        'bowling_win_rate': int(bowling_win_rate),
        'fielding_win_rate': int(fielding_win_rate),
        'quick_games_played': stats['quick_games_played'],
        'quick_games_won': stats['quick_games_won'],
        'quick_win_rate': quick_win_rate,
        'classic_games_played': stats['classic_games_played'],
        'classic_games_won': stats['classic_games_won'],
        'classic_win_rate': classic_win_rate
    }
    
    # Sample achievements
    achievements = [
        {'title': 'First Victory', 'description': 'Win your first game', 'icon': 'fa-trophy', 'unlocked': stats['games_won'] >= 1, 'progress': min(stats['games_won'], 1), 'target': 1},
        {'title': 'Champion', 'description': 'Win 10 games', 'icon': 'fa-crown', 'unlocked': stats['games_won'] >= 10, 'progress': min(stats['games_won'], 10), 'target': 10},
        {'title': 'Veteran', 'description': 'Play 25 games', 'icon': 'fa-medal', 'unlocked': stats['games_played'] >= 25, 'progress': min(stats['games_played'], 25), 'target': 25},
        {'title': 'Batting Master', 'description': 'Win 50 batting rounds', 'icon': 'fa-running', 'unlocked': stats['batting_rounds_won'] >= 50, 'progress': min(stats['batting_rounds_won'], 50), 'target': 50},
        {'title': 'Bowling King', 'description': 'Win 50 bowling rounds', 'icon': 'fa-baseball-ball', 'unlocked': stats['bowling_rounds_won'] >= 50, 'progress': min(stats['bowling_rounds_won'], 50), 'target': 50},
        {'title': 'Fielding Expert', 'description': 'Win 50 fielding rounds', 'icon': 'fa-hand-paper', 'unlocked': stats['fielding_rounds_won'] >= 50, 'progress': min(stats['fielding_rounds_won'], 50), 'target': 50},
        {'title': 'Win Streak', 'description': 'Win 5 games in a row', 'icon': 'fa-fire', 'unlocked': stats['best_streak'] >= 5, 'progress': min(stats['best_streak'], 5), 'target': 5},
        {'title': 'Bot Slayer', 'description': 'Win 50 games total', 'icon': 'fa-robot', 'unlocked': stats['games_won'] >= 50, 'progress': min(stats['games_won'], 50), 'target': 50},
        {'title': 'Perfect Record', 'description': 'Win 100% of games (min 5 games)', 'icon': 'fa-star', 'unlocked': stats['games_played'] >= 5 and win_rate == 100, 'progress': int(win_rate) if stats['games_played'] >= 5 else 0, 'target': 100}
    ]
    
    # Sample game history for chart
    num_games = min(stats['games_played'], 10) if stats['games_played'] > 0 else 5
    game_history = {
        'dates': json.dumps([f"Game {i+1}" for i in range(num_games)]),
        'win_rates': json.dumps([50 + (i * 5) for i in range(num_games)])
    }
    
    return render_template('statistics.html',
                         user_stats=user_stats,
                         achievements=achievements,
                         game_history=game_history)

def update_round_stats(winner, chosen_stat):
    """Update statistics after each round"""
    if 'user_stats' not in session:
        session['user_stats'] = {
            'games_played': 0,
            'games_won': 0,
            'rounds_played': 0,
            'rounds_won': 0,
            'batting_selections': 0,
            'bowling_selections': 0,
            'fielding_selections': 0,
            'batting_rounds_won': 0,
            'bowling_rounds_won': 0,
            'fielding_rounds_won': 0,
            'batting_rounds_played': 0,
            'bowling_rounds_played': 0,
            'fielding_rounds_played': 0,
            'quick_games_played': 0,
            'quick_games_won': 0,
            'classic_games_played': 0,
            'classic_games_won': 0,
            'current_streak': 0,
            'best_streak': 0,
            'game_history': []
        }
    
    stats = session['user_stats']
    stats['rounds_played'] += 1
    
    # Update stat-specific counters
    if chosen_stat == 'batting':
        stats['batting_rounds_played'] += 1
        if winner == 'user':
            stats['batting_rounds_won'] += 1
    elif chosen_stat == 'bowling':
        stats['bowling_rounds_played'] += 1
        if winner == 'user':
            stats['bowling_rounds_won'] += 1
    elif chosen_stat == 'fielding':
        stats['fielding_rounds_played'] += 1
        if winner == 'user':
            stats['fielding_rounds_won'] += 1
    
    if winner == 'user':
        stats['rounds_won'] += 1
    
    session['user_stats'] = stats

def update_game_stats(winner, mode):
    """Update statistics after each game"""
    if 'user_stats' not in session:
        session['user_stats'] = {
            'games_played': 0,
            'games_won': 0,
            'rounds_played': 0,
            'rounds_won': 0,
            'batting_selections': 0,
            'bowling_selections': 0,
            'fielding_selections': 0,
            'batting_rounds_won': 0,
            'bowling_rounds_won': 0,
            'fielding_rounds_won': 0,
            'batting_rounds_played': 0,
            'bowling_rounds_played': 0,
            'fielding_rounds_played': 0,
            'quick_games_played': 0,
            'quick_games_won': 0,
            'classic_games_played': 0,
            'classic_games_won': 0,
            'current_streak': 0,
            'best_streak': 0,
            'game_history': []
        }
    
    stats = session['user_stats']
    stats['games_played'] += 1
    
    # Update mode-specific stats
    if mode == 'quick':
        stats['quick_games_played'] += 1
        if winner == 'user':
            stats['quick_games_won'] += 1
    else:
        stats['classic_games_played'] += 1
        if winner == 'user':
            stats['classic_games_won'] += 1
    
    # Update streak tracking
    if winner == 'user':
        stats['games_won'] += 1
        stats['current_streak'] += 1
        stats['best_streak'] = max(stats['best_streak'], stats['current_streak'])
    else:
        stats['current_streak'] = 0
    
    session['user_stats'] = stats

@app.route('/reset_statistics', methods=['POST'])
def reset_statistics():
    """Reset all user statistics"""
    session['user_stats'] = {
        'games_played': 0,
        'games_won': 0,
        'rounds_played': 0,
        'rounds_won': 0,
        'batting_selections': 0,
        'bowling_selections': 0,
        'fielding_selections': 0,
        'batting_rounds_won': 0,
        'bowling_rounds_won': 0,
        'fielding_rounds_won': 0,
        'batting_rounds_played': 0,
        'bowling_rounds_played': 0,
        'fielding_rounds_played': 0,
        'quick_games_played': 0,
        'quick_games_won': 0,
        'classic_games_played': 0,
        'classic_games_won': 0,
        'current_streak': 0,
        'best_streak': 0,
        'game_history': []
    }
    return redirect(url_for('statistics'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
