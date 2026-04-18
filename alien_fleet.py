"""Manages the fleet of aliens in the Alien Invasion game.
Handles fleet creation, movement, collision detection, 
and fleet state updates.
"""
import pygame
from alien import Alien

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet:
    """A class to manage the fleet of aliens."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed  

        self.create_fleet()

    def create_fleet(self):
        """Create a grid-based fleet of aliens."""
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_hight = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(
            alien_width, screen_width, alien_height, screen_hight)
        
        x_offset, y_offset = self.calculate_offsets(
            alien_width, alien_height, screen_width, fleet_width, fleet_height)
        
        self._create_rectangle_fleet(alien_width, alien_height, 
                                     fleet_width, fleet_height, 
                                     x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_width, alien_height, 
                                fleet_width, fleet_height, 
                                x_offset, y_offset):
        """Populate the fleet with aliens in a rectangular grid.

        Args:
            alien_width (int): Width of each alien
            alien_height (int): Height of each alien
            fleet_width (int): Number rows
            fleet_height (int): Number of colums
            x_offset (int): Horizontal starting offset
            y_offset (int): Vertical starting offset
        """
        for row in range(fleet_height):
            for col in range(fleet_width):
                current_x = alien_width * col + x_offset
                current_y = alien_height * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_width, alien_height, 
                          screen_width, fleet_width, fleet_height):
        """ Calculates offsets to position the fleet on the screen

        Args:
            alien_width (int): Width of each alien
            alien_height (int): Height of each alien
            screen_width (int): Wiidth of the screen
            fleet_width (int): Number of columns
            fleet_height (int): Number of rows

        Returns:
            tuple[int, int]: x_offset and y_offset for positioning the fleet.
        """
        half_screen = self.settings.screen_height // 2
        fleet_horizontal_spac = (fleet_width * alien_width)
        fleet_vertical_space = (fleet_height * alien_height)
        x_offset = int((screen_width - fleet_horizontal_spac) // 2)
        y_offset = int((half_screen - fleet_vertical_space) // 2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_width, screen_width, 
                             alien_height, screen_height):
        """Determine how many aliens fit on the screen.

        Args:
            alien_width (int): Width of each alien
            screen_width (int): Width of the screen
            alien_height (int): Height of each alien
            screen_height (int): Width of the screen

        Returns:
            tuple[int, int]: Number of rows and columns(fleet_width , fleet_height)
        """
        fleet_width = (screen_width // alien_width )
        fleet_height = ((screen_height / 2) // alien_height)
        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2
        
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return int(fleet_width), int(fleet_height)
        
    def _create_alien(self, current_x: int, current_y: int):
        """Create a single alien and add it the fleet.

        Args:
            current_x (int): Horizontal position
            current_y (int): Vertical position
        """
        new_alien = Alien(self, current_x, current_y)
        
        self.fleet.add(new_alien)

    def check_fleet_edges(self):
        """Check if any alien has reached a screen edge.
        if an edge is reached, drop the fleet and reverse direction
        """
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Drop the entire fleet to the bottom
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """Update all aliens in the fleet.
        """
        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw all aliens in the fleet to the screen.
        """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between aliens and another sprite group.

        Args:
            other_group (pygame.sprite.Group): Group to check collisions with.

        Returns:
            dict: Collision dictionary from pygame.groupcollide.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """Check if any alien has reached to bottom of the screen

        Returns:
            bool: True if an alien touches to the bottom of the screen
        """
        alien: 'Alien'
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_height:
                return True
        return False
    
    def check_destroyed_status(self):
        """Check whether all aliens have been destroyed.

        Returns:
            bool: True if the fleet is empty.
        """
        return not self.fleet
        