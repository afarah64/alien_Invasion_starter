""" Alien Invasion - A simple 2D game where the player controls a spaceship to defend against alien invaders.
    Author: Abdalla Farah
    Date: 04/10/2026
"""


import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        # Initialize pygame
        pygame.init()

        # Create an instance of the Settings class and store it in the settings attribute.
        self.settings = Settings()
        
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


        # Create an instance of the Ship class and store it in the ship attribute.
        self.ship = Ship(self, Arsenal(self))



    def run_game(self):
        #Game loop
        while self.running:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Update the ship's position based on the movement flags.
            self.ship.update()
            # Update the screen during each pass through the loop.
            self._update_screen()
            # Limit the frame rate to the value specified in settings.
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen.
        """
        self.screen.blit(self.bg_image, (0, 0))
        # Draw the ship to the screen.
        self.ship.draw()
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
