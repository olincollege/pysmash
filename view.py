"""
class docstring
"""
from abc import ABC, abstractmethod
import pygame

class CharaterView(ABC):
    """
    docstring
    """
    def __init__(self, game):
        self._game = game
    
    @property
    def game(self):
        """
        docstring
        """
        return self._game

    @abstractmethod
    def draw(self):
        """
        A method that is an abstract method that does nothing
        """
    
class WindowView(CharaterView):
    """
   dostring
    """
    def __init__(self, game, x_dim, y_dim):
        super().__init__(game)
        self.screen = pygame.display.set_mode([x_dim, y_dim])

    def draw(self):
        """
        implement the 'draw' method, which should print the
        map and character
        """
        self.game.all_sprites.update()
        self.screen.fill((255, 255, 255))
        self.game.all_sprites.draw(self.screen)
        pygame.display.flip()

        

