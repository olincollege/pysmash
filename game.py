"""
Main PySmash Game Class
"""
# pylint: disable=no-member
import pygame

from view import WindowView
from controller import KeyboardController
from characters.mario import Mario

class Game:
    """
    Main PySmash Game Class
    """
    def __init__(self, player1):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.player1 = player1
        self.p1controller = KeyboardController(self.player1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player1)

        self.viewer = WindowView(self, 1240, 720)

    def mainloop(self):
        """
        Main game loop
        """
        while True:
            self.p1controller.move()
            print(self.player1.pos, self.player1.vel)
            self.viewer.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game(Mario())
    game.mainloop()
