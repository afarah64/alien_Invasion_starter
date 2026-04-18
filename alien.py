"""Define the Alien class used in the Alien Invasion game.
Each alien is a sprite that moves horizontally and interacts
with screen boundaries
"""
import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize the alien at a specific position."""
        super().__init__()
        
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load the bullet image and scale it to the specified width and height from settings.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_width, self.settings.alien_height)
            )
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Update the alien's horizontal position.
        Moves the alien left or right depending on the fleet's direction.
        """
        temp_speed = self.settings.fleet_speed
        
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def check_edges(self):
        """Check whether the alien has reached a screen edge.

        Returns:
            bool: True if the alien touches the left or right edge.
        """
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
        


    def draw_alien(self):
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)
        

