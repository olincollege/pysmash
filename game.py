"""
Main PySmash Game Class
"""
# pylint: disable=no-member
import pygame

from view import WindowView
from controller import KeyboardController, KeyboardController2
from characters.mario import Mario
from stages.final_destination import FinalDestination

class Game:
    """
    Main PySmash Game Class
    """
    def __init__(self, player1, player2):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.player1 = player1
        self.player2 = player2
        self.p1controller = KeyboardController(self.player1)
        self.p2controller = KeyboardController2(self.player2)
        self.all_sprites = pygame.sprite.Group(self.player1, self.player2)
        # self.all_sprites.add(self.player1)
        # self.all_sprites.add(self.player2)

        self.stage = FinalDestination()
        self.player1.platforms = self.stage.platforms
        self.player2.platforms = self.stage.platforms

        self.viewer = WindowView(self, 1240, 720)

    def mainloop(self):
        """
        Main game loop
        """
        while True:
            self.p1controller.move()
            self.p2controller.move()
            self.viewer.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game(Mario('left'), Mario('right'))
    game.mainloop()
