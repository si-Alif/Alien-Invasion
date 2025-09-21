import pygame
from pygame.sprite import Sprite


class Alien(Sprite) :
    """A class representing a single aline in the fleet"""

    def __init__(self , ai_instance) :
        """Initialize alien and set it to the starting position on the screen"""
        super().__init__()
        self.screen = ai_instance.screen
        self.settings = ai_instance.settings

        # Load the alien image
        try :
            self.image = pygame.image.load("./images/alien.bmp")
        except FileNotFoundError :
            print("Alien Image not found")

        self.rect = self.image.get_rect()

        # Getting the ship into it' position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's horizontal position precisely
        self.alien_horizontal_dimension = float(self.rect.x)
        self.alien_vertical_dimension = float(self.rect.y)

    def update(self) :
        """Move the alien to the right"""
        self.alien_horizontal_dimension += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x  = self.alien_horizontal_dimension

    def check_edges(self) :
        """Return True if the alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)