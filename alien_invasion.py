import sys
import pygame


from settings import Settings
from ship import Ship

class AlienInvasion :
    """Overall Class to manage the entire application's assets and functionalities ."""
    def __init__(self) :
        pygame.init()

        # Maintaining a constant frame rate is crucial for our application cz we don't want it to run too fast or too slow based on different hardware
        # To resolve this issue rather than depending on the system we use the pygame.time.Clock class to maintain a constant frame rate
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        # In the central class , we set a attribute screen which stores a display instance of the pygame's display class .
        # Using this instance we customize the display of our application
        # passed the first positional argument co-ordinate , a tuple for the width and height
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    # Loop which runs the game in an infinite loop until we reach a certain threshold .
    def run_game(self) :
        """Entry point function to the game"""
        while True :
            self._check_events()
            self._update_screen()
            # here the tick method takes one argument which is the frame of the game that we want to maintain . This simply means the game will run at 60 frames per second or from the codes perspective this loop will run 60 times per second
            self.clock.tick(60)

    # ⭐ Helper methods
    def _check_events(self) :
        """A helper method to check for new events"""
        # pygame catches all the events that occur since the last iteration and stores them in a list via the event.get() method
        for event in pygame.event.get() :
            #  here the pygame.QUIT is an event which is raised when the user exits the game
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self) :
        """Update images on the screen and get to the most recent state of the game"""
        self.screen.fill(self.settings.bg_color)

        # update images
        self.ship.blitme()

        # update the screen
        # Redraw the screen during each pass through the loop . This is used to tell the pygame "Hey , redraw the screen with the most recent state of the game"
        pygame.display.flip()

#  If the entry is the main menu , then we create an instance of the class and call the run_game method
if __name__ == "__main__" :
    ai = AlienInvasion()
    ai.run_game()
