import pygame
from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self, player):
        """
        Creates a private instance attribute of a tic tac toe
        board.

        Args: board is an instance of a `TicTacToeBoard`
        """
        self._player = player

    @property
    def player(self):
        """
        A 'board' property that returns the tic-tac-toe
        board stored in the `TicTacToeView` instance.

        Returns: self._board which is a private
            instance of the game board.
        """
        return self._player

    @abstractmethod
    def move(self):
        """
        A method that is an abstract method that does nothing
        """
        pass


class KeyboardController(Controller):
    """
    """
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.left()
        if keys[pygame.K_RIGHT]:
            self.player.right()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If pressed key is ESC quit program
                if event.key == pygame.K_ESCAPE:
                    self._print("ESC was pressed. quitting...")
                    self.quit()
                elif event.key == pygame.K_DOWN:
                    self.player.crouch()
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.player.jump()
                else:
                    self.player.normal()

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_a]:
                    self.player.attack()
                elif pressed[pygame.K_d]:
                    self.player.defense()
                elif pressed[pygame.K_w]:
                    self.player.power()
