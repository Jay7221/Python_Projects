class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Inintialize the game's settings."""
        # Screen settings
        self.screen_width = 1300
        self.screen_height = 650
        self.bg_color = (252, 252, 252)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
