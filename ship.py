import pygame

class Ship :
    """A class to manage the ship"""

    def __init__(self , ai_game_instance) :
        """Initialize the ship and set it's position on the screen"""
        self.screen = ai_game_instance.screen
        self.settings = ai_game_instance.settings
        self.screen_rect = ai_game_instance.screen.get_rect()

        # Load the screen image
        try :
            self.image = pygame.image.load("./images/ship.bmp")
        except FileNotFoundError :
            print("Ship Image not found")

        self.rect = self.image.get_rect()

        # Set each new ship at the bottom of the screen
        # say : "the midbottom of ship's rect should be at the midbottom of the screen's rect"
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        # as the ships positions are stored in rect which is integer , we need to store it as float as the speed might be a float
        self.horizontal_dimension = float(self.rect.x)

    def update(self) :
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.horizontal_dimension += self.settings.movement_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.horizontal_dimension -= self.settings.movement_speed
        # Update the ship's horizontal position
        # all the rect related data is integer , so if a float is passed it will be converted to integer
        self.rect.x = self.horizontal_dimension

    def blitme(self) :
        """draw the screen at it's current position"""
        self.screen.blit(self.image , self.rect)

    def center_ship(self) :
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom # assign screen's midbottom to ship's midbottom
        self.horizontal_dimension = float(self.rect.x)