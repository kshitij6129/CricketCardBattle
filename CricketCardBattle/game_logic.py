import random
from typing import List, Dict, Any

class GameLogic:
    """Handles core game logic and state management"""
    
    def initialize_game(self, all_players: List[Dict], cards_per_player: int) -> Dict[str, Any]:
        """Initialize a new game with shuffled cards"""
        # Shuffle all players
        shuffled_players = random.sample(all_players, len(all_players))
        
        # Deal cards to user and bot
        total_cards_needed = cards_per_player * 2
        if total_cards_needed > len(shuffled_players):
            # If we need more cards than available, deal all available
            cards_per_player = len(shuffled_players) // 2
        
        user_hand = shuffled_players[:cards_per_player]
        bot_hand = shuffled_players[cards_per_player:cards_per_player * 2]
        
        # Initialize game state
        game_state = {
            'user_hand': user_hand,
            'bot_hand': bot_hand,
            'user_score': 0,
            'bot_score': 0,
            'round_number': 1,
            'total_rounds': cards_per_player,
            'current_round': {
                'stat_chooser': 'user',  # User goes first
                'phase': 'stat_selection'  # stat_selection or card_selection
            }
        }
        
        return game_state
    
    def compare_cards(self, user_card: Dict, bot_card: Dict, chosen_stat: str) -> Dict[str, Any]:
        """Compare two cards and determine the winner"""
        user_stat_value = user_card[chosen_stat]
        bot_stat_value = bot_card[chosen_stat]
        
        result = {
            'user_card': user_card,
            'bot_card': bot_card,
            'chosen_stat': chosen_stat,
            'user_stat_value': user_stat_value,
            'bot_stat_value': bot_stat_value,
            'winner': None,
            'margin': 0,
            'tie_broken_by_total': False
        }
        
        if user_stat_value > bot_stat_value:
            result['winner'] = 'user'
            result['margin'] = user_stat_value - bot_stat_value
        elif bot_stat_value > user_stat_value:
            result['winner'] = 'bot'
            result['margin'] = bot_stat_value - user_stat_value
        else:
            # Tie - compare total stats
            user_total = user_card['batting'] + user_card['bowling'] + user_card['fielding']
            bot_total = bot_card['batting'] + bot_card['bowling'] + bot_card['fielding']
            
            result['tie_broken_by_total'] = True
            result['user_total'] = user_total
            result['bot_total'] = bot_total
            
            if user_total > bot_total:
                result['winner'] = 'user'
                result['margin'] = user_total - bot_total
            elif bot_total > user_total:
                result['winner'] = 'bot'
                result['margin'] = bot_total - user_total
            else:
                result['winner'] = 'tie'
                result['margin'] = 0
        
        return result
    
    def is_game_over(self, game_state: Dict[str, Any]) -> bool:
        """Check if the game is over"""
        return len(game_state['user_hand']) == 0 or len(game_state['bot_hand']) == 0
    
    def get_game_winner(self, game_state: Dict[str, Any]) -> str:
        """Determine the overall game winner"""
        if game_state['user_score'] > game_state['bot_score']:
            return 'user'
        elif game_state['bot_score'] > game_state['user_score']:
            return 'bot'
        else:
            return 'tie'
