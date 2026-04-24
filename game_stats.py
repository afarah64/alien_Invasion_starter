"""Track statistics for the Alien Invasion game.

This class manages the lifecycle of game data, including scores, levels, 
    and player lives. It also handles saving and loading the all-time 
    high score to a JSON file.
"""
from pathlib import Path
import json
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """initialize statistics for the game."""

    def __init__(self, game: 'AlienInvasion'):
     
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()
        

    def init_saved_scores(self):
        """Initialize the hi_score from a saved JSON scores file, 
        if the file exists and is valid, it loads the high score; otherwise, 
        it sets the hi_score to 0 and creates the file with the initial score.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
    
    def save_scores(self):
        """Save the hi_score to the scores file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File not Found: {e}")  

    def reset_stats(self):
        """Initialize statistics that can change during the game.
        This method resets the number of ships left, 
        the current score, and the level.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
    
    def update(self, collisions):
        """Update score and high scores based on recent collisions

        Args:
            collisions (dict): A dictionary of collisions returned by pygame.groupcollide.
        """
        # update self.score
        self._update_score(collisions)
        # update max_score
        self._update_max_score()

        # Update hi_score
        self._update_hi_score()

    def _update_max_score(self):
        """Update the session-specific Max score if the current score is higher.
        """
        if self.score > self.max_score:
            self.max_score = self.score
            
    def _update_hi_score(self):
        """Update the all-time high score if the current score exceeds it,
        and save the new high score to the scores file.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        """Calculate points based on the number of aliens hit.

        Args:
            collisions (dict): A dictionary containing the collided sprite groups
        """
        for aliens in collisions.values():
            self.score += self.settings.alien_points
            
    
    def update_level(self):
        """Increase the level by 1 and update the game settings to make the game more challenging."""
        self.level += 1
        

          
        
    
