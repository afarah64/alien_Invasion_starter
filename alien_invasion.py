import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        # Initialize pygame
        pygame.init()
        
        # Set up the display window and caption.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # initialize a variable to control the main loop
        self.running = True

    def run_game(self):
        #Game loop
        while self.running:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            pygame.display.flip()        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
