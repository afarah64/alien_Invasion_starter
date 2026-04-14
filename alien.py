import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        """Initialize the alien at a specific position."""
        super().__init__()
        
        # store a reference to the game instance and its settings and screen attributes
        self.screen = game.screen
        #get the boundaries of the screen to ensure the alien stays within them
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Load the bullet image and scale it to the specified width and height from settings.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_width, self.settings.alien_height)
            )
        
        # Get the rect of the image and set its initial position based on the x and y parameters.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
        #self.y = float(self.rect.y)

    def update(self):
        pass

    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)
        

