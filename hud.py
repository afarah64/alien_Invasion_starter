"""The HUD class manages the display of scoring information, player lives, and 
the current level in the Alien Invasion game. 
It renders this information as images and positions them on the screen. 
The HUD updates these images whenever the score or level changes, 
ensuring that the player always has up-to-date information about their progress in the game.
"""
import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    """A class to manage scoring information, level, and player lives.
    """
    
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the HUD.

        Args:
            game (AlienInvasion): The main game instance
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_imange()
        self.update_level()

    def _setup_life_imange(self):
        """load and scale the ship image used to represent remaining lives
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, 
                (self.settings.ship_width, self.settings.ship_height)
                )
        self.life_rect = self.life_image.get_rect()
    

    def update_scores(self):
        """Update all score-related images (Current-score, Max-score and highest score)
        """
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self):
        """Turn the current score into a rendered image.
        """
        score_str = f"Score: {self.game_stats.score: ,.0f}"
        self.score_image = self.font.render(score_str, True, 
            self.settings.text_color, None)
        #position the score at the top right of the screen below the max score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """Turn the max score into a rendered image."""        
        max_score_str = f"Max-Score: {self.game_stats.max_score: ,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, 
            self.settings.text_color, None)
        #position the max score at the top right of the screen
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundries.right - self.padding
        self.max_score_rect.top = self.padding
       
       
    def _update_hi_score(self):
        """Turn the High-score into a rendered image.
        """
        hi_score_str = f"Hi-Score: {self.game_stats.hi_score: ,.0f}"
        self.hi_score_image = self.font.render(hi_score_str, True, 
            self.settings.text_color, None)
        #position the hi score at the top center of the screen
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundries.centerx, self.padding)
    
    def update_level(self):
        """Turn the current level into a rendered image.
        """
        level_str = f"Level: {self.game_stats.level: ,.0f}"
        self.level_image = self.font.render(level_str, True, 
            self.settings.text_color, None)
        #position the level at the top left of the screen below the lives
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self):
        """Draw ships representing remaining lives.
        """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draw the scores, level and ships to the screen.
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
