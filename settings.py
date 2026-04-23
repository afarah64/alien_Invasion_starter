from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name = "Alien Invasion"

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Frames per second setting
        self.FPS = 60

        # Background settings
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'


        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_direction = 1

        self.botton_width = 200
        self.botton_height = 50
        self.botton_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'fonts' / 'Silkscreen' / 'Silkscreen-bold.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_speed = 7
        self.bullets_amount = 5
        
        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50


    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

         
        
        