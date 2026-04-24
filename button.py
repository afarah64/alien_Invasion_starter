"""
A module to define the Button class, which creates and manages a button in the game.
The Button class initializes the button's attributes, 
prepares the message to be displayed on the button, 
and provides methods to draw the button on the screen and check if it has been clicked.
"""
import pygame.font

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
class Button:
    """ A class to create a button for the game."""

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """ Initialize button attributes.

        Args:
            game (AlienInvasion): The main game instance
            msg (str): The text to display on the button"""

        self.game=game
        self.screen= game.screen
        self.boundries = self.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.botton_width, 
            self.settings.botton_height)
        self.rect.center = self.boundries.center
        self._prep_msg(msg)

       
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button
        Args:
            msg (str): The text to display on the button
        """

        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message.
        """
        self.screen.fill(self.settings.botton_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
    def check_clicked(self, mouse_pos):
        """Check if the button has been clicked.
        Args:
            mouse_pos (tuple): The position of the mouse click.

        Returns:
            bool: True if the button is clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)