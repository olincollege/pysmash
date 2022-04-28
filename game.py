from player import Player
from view import WindowView
from controller import KeyboardController
from characters.mario import Mario
import pygame

class Game:
    def __init__(self, player1):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.p1 = player1
        self.p1controller = KeyboardController(self.p1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.p1)

        self.viewer = WindowView(self, 1240, 720)

    def mainloop(self):
        while True:
            self.p1controller.move()
            self.p1.gravity()
            self.viewer.draw()
            print(self.p1.x_pos, self.p1.y_pos)
            self.clock.tick(60)
            
if __name__ == "__main__":
    game = Game(Mario())
    game.mainloop()
