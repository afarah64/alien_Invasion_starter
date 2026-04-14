""" Alien Invasion - A simple 2D game where the player controls a spaceship to defend against alien invaders.
    Author: Abdalla Farah
    Date: 04/10/2026
"""


import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
from alien_fleet import AlienFleet
from time import sleep


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        # Initialize pygame
        pygame.init()

        # Create an instance of the Settings class and store it in the settings attribute.
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)
        
        # Set up the display window and caption.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        # Set the caption of the game window to the name specified in settings.
        pygame.display.set_caption(self.settings.name)

        # Load the background image and scale it to fit the screen dimensions.
        self .bg_image = pygame.image.load(self.settings.bg_file)
        self.bg_image = pygame.transform.scale(self.bg_image, 
                (self.settings.screen_width, self.settings.screen_height)
                )
        
        # Set the running attribute to True to indicate that the game is active.
        self.running = True
        # Create a clock object to manage the frame rate of the game.
        self.clock = pygame.time.Clock()

        # Initialize the mixer module for sound and load the laser sound effect.
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(str(self.settings.impact_sound))
        self.impact_sound.set_volume(0.7)



        # Create an instance of the Ship class and store it in the ship attribute.
        self.ship = Ship(self, Arsenal(self))

        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        self.game_active = True 



    def run_game(self):
        #Game loop
        while self.running:
            # Watch for keyboard and mouse events.
            self._check_events()
            if self.game_active:
                # Update the ship's position based on the movement flags.
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
                # Update the screen during each pass through the loop.
            self._update_screen()
            # Limit the frame rate to the value specified in settings.
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        #check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
             
        #subtract one lif if possible
       
        #check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        
        #check collision of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
        
        if self.alien_fleet.check_destroyed_status(): 
            self._reset_level()   

    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -=1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False
        


    def _reset_level(self):

        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.
        """
        self.screen.blit(self.bg_image, (0, 0))

        # Draw the ship to the screen.
        self.ship.draw()
        self.alien_fleet.draw()
        
        # Redraw the screen during each pass through the loop.
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event: pygame.event.Event): 
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event: pygame.event.Event):
        """Respond to keypresses."""
        #checks for right and left arrow keys to set the ship's movement flags accordingly
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # checking for spacebar to fire a bullet, and giving it a sound effect when fired
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250 )
        # checking for 'q' key to quit the game     
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
