"""Define the Bullet class used in the Alien Invasion game.
Bullets are fired from the ship and travel vertically across 
the screen to hit aliens
"""
import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize a bullet at the ship's current position.

        Args:
            game (AlienInvasion): The main game instance
        """
        super().__init__()
        
        # store a reference to the game instance and its settings and screen attributes
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and scale it to the specified width and height from settings.
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_width, self.settings.bullet_height)
            )
        
        # Get the rect of the bullet image and set its midtop to the ship's midtop.
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet vertically across the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = int(self.y)

    def draw_bullet(self):
        """Draw the bullet at its current position on the screen."""
        self.screen.blit(self.image, self.rect)
        

