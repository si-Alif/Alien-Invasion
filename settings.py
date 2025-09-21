class Settings :
    """A central class to manage all the settings needed for the application"""
    def __init__(self) :
        """Initialize the games settings"""
        self.bg_color = (230 ,230, 230)
        self.screen_width = 1200
        self.screen_height = 800
        self.movement_speed = 1.5

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60 ,60 ,60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # direction 1 is right and -1 is left
        self.fleet_direction = 1