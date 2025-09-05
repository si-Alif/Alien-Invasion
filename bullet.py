import pygame
from pygame.sprite import Sprite

class Bullet(Sprite) :
    """A class to manage bullets fired from the ship"""
    def __init__(self , ai_game_instance) :
        """Create a bullet object at bullets current position"""
        super().__init__()
        self.screen = ai_game_instance.screen
        self.settings = ai_game_instance.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect using pygame.rect() method at (0 , 0) of the screen(just create the bullet for noe , in the next line we placed it at it's proper position) and then assign it to the correct position
        self.rect = pygame.Rect(0 , 0 , self.settings.bullet_width , self.settings.bullet_height)
        # Place the bullet being fired at the middle of top of the ship
        self.rect.midtop = ai_game_instance.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.bullet_position = float(self.rect.y)

    def update(self) :
        """Move the bullet up the screen"""
        # update the exact position of the bullet
        self.bullet_position -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.bullet_position

    def draw_bullet(self) :
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen , self.color , self.rect)