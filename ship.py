import pygame

class Ship :
    """A class to manage the ship"""

    def __init__(self , ai_game_instance) :
        """Initialize the ship and set it's position on the screen"""
        self.screen = ai_game_instance.screen
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
    def blitme(self) :
        """draw the screen at it's current position"""
        self.screen.blit(self.image , self.rect)