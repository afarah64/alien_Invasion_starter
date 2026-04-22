"""Track statistics for the Alien Invasion game.

This class stores and manages game-related state information,
such as the number of remaining ships (lives).
"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, game: 'AlienInvasion'):
     
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()
    


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
    
    def update(self, collisions):
        # update self.score
        self._update_score(collisions)
        # update max_score
        self._update_max_score()

        # Update hi_score
    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            

    def _update_score(self, collisions):
        for aliens in collisions.values():
            self.score += self.settings.alien_points
           
    
    def update_level(self):
        self.level += 1
        

          
        
    
