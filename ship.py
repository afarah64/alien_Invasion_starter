"""Define the ship class for the player-controlled spacecraft.
This ship moves Horizontally along the bottom of the screen and 
can fire bullets to destroy aliens
"""
import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initialize the ship and its starting position.

        Args:
            game (AlienInvasion): The main game instance
            arsenal (Arsenal): The ship's bullet manager.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
                (self.settings.ship_width, self.settings.ship_height)
                )
        # Get the rect of the ship image and the screen.
        self.rect = self.image.get_rect()
        self.boundaries = game.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self._center_ship()

        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the ship's horizontal position.

        # Store a reference to the arsenal instance.    
        self.arsenal = arsenal

    def _center_ship(self):
        """ centers the ship at bottom of the screen"""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position and its arsenal based on the movement flags."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Update the ship's position based on the movement flags."""
          
        temp_speed = self.settings.ship_speed
        #check if ship is moving right and if it is within the right boundary
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        #check if ship is moving left and if it is within the left boundary    
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        # Update rect object from self.x.
        self.rect.x = int(self.x)


    def draw(self):
        """Draw the ship at its bullets on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect) 
    
    def fire(self):
        """Fire a bullet if the limit has not been reached.

        Returns:
            bool: True if a bullet was fired, False otherwise.
        """
        return self.arsenal.fire_bullet()
        
    def check_collisions(self, other_group):
        """Check for collision with another sprite group.

        Args:
            other_group (pygame.sprite.Group): Group to check collisions with.

        Returns:
            bool: True if a collision occurs, False otherwise.
        """
        if pygame.sprite.spritecollideany(self, other_group,):
            self._center_ship()
            return True 
        return False
    
   