from typing import List, Dict, Any
import logging
import random

class BotAI:
    """Intelligent bot AI for cricket cards game"""
    
    def choose_stat(self, bot_hand: List[Dict]) -> str:
        """Choose the optimal stat based on bot's remaining cards with strategic variability"""
        if not bot_hand:
            return 'batting'  # Fallback
        
        # Calculate average values for each stat
        stat_averages = {
            'batting': sum(card['batting'] for card in bot_hand) / len(bot_hand),
            'bowling': sum(card['bowling'] for card in bot_hand) / len(bot_hand),
            'fielding': sum(card['fielding'] for card in bot_hand) / len(bot_hand)
        }
        
        # Also consider maximum values (bot's strongest cards)
        stat_maximums = {
            'batting': max(card['batting'] for card in bot_hand),
            'bowling': max(card['bowling'] for card in bot_hand),
            'fielding': max(card['fielding'] for card in bot_hand)
        }
        
        # More strategic weighted decision: 50% average, 30% maximum, 20% strategic variance
        stat_scores = {}
        for stat in ['batting', 'bowling', 'fielding']:
            base_score = (0.5 * stat_averages[stat]) + (0.3 * stat_maximums[stat])
            # Add strategic variance to avoid predictability
            variance = random.uniform(-5, 5)
            stat_scores[stat] = base_score + variance
        
        # Choose the stat with the highest score
        best_stat = max(stat_scores, key=stat_scores.get)
        
        # Additional strategic logic: sometimes choose second-best to be unpredictable
        if random.random() < 0.2:  # 20% chance to be unpredictable
            sorted_stats = sorted(stat_scores.items(), key=lambda x: x[1], reverse=True)
            if len(sorted_stats) > 1:
                # Choose second best or a random one
                alternate_choices = [stat for stat, score in sorted_stats[1:]]
                if alternate_choices:
                    best_stat = random.choice(alternate_choices)
        
        # Debug logging
        logging.debug(f"Bot hand size: {len(bot_hand)}")
        logging.debug(f"Stat averages: {stat_averages}")
        logging.debug(f"Stat maximums: {stat_maximums}")
        logging.debug(f"Stat scores: {stat_scores}")
        logging.debug(f"Bot chose stat: {best_stat}")
        
        return best_stat
    
    def choose_card(self, bot_hand: List[Dict], chosen_stat: str) -> Dict:
        """Choose the best card for the given stat"""
        if not bot_hand:
            return None
        
        # Find the card with the highest value for the chosen stat
        best_card = max(bot_hand, key=lambda card: card[chosen_stat])
        
        return best_card
    
    def analyze_hand_strength(self, bot_hand: List[Dict]) -> Dict[str, Any]:
        """Analyze the overall strength of bot's hand"""
        if not bot_hand:
            return {'total_strength': 0, 'best_stats': []}
        
        # Calculate total strength
        total_strength = sum(
            card['batting'] + card['bowling'] + card['fielding'] 
            for card in bot_hand
        )
        
        # Find strongest stats
        stat_totals = {
            'batting': sum(card['batting'] for card in bot_hand),
            'bowling': sum(card['bowling'] for card in bot_hand),
            'fielding': sum(card['fielding'] for card in bot_hand)
        }
        
        # Sort stats by total strength
        best_stats = sorted(stat_totals.keys(), key=lambda x: stat_totals[x], reverse=True)
        
        return {
            'total_strength': total_strength,
            'best_stats': best_stats,
            'stat_totals': stat_totals,
            'average_strength': total_strength / len(bot_hand) if bot_hand else 0
        }
