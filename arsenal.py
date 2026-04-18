"""Manage all bullets fired by the player's ship.
This module defines the Arsenal class, which handles bullet creation,
Updating bullet positions, and removing bullets fthat leave the screen
"""
import pygame
from bullet import Bullet

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """A class to manage the ship's arsenal."""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the arsenal.

        Args:
            game (AlienInvasion): The main game instance
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update all bullets and remove those that go off-screen."""
        self.arsenal.update()
        self.remove_bullets_offscreen()
    
    def remove_bullets_offscreen(self):
        """Remove bullets that have disappeared off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets in the arsenal to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create and fire a new bullet if the limit is not exceeded.

        Returns:
            bool: True if a bullet was created, False otherwise.
        """
        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)  
            self.arsenal.add(new_bullet)
            return True
        return False