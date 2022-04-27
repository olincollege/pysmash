import pygame
from abc import ABC, abstractmethod

class Controller(ABC):
    def __init__(self, board):
        """
        Creates a private instance attribute of a tic tac toe
        board.

        Args: board is an instance of a `TicTacToeBoard`
        """
        self._board = board

    @property
    def board(self):
        """
        A 'board' property that returns the tic-tac-toe
        board stored in the `TicTacToeView` instance.

        Returns: self._board which is a private
            instance of the game board.
        """
        return self._board

    @abstractmethod
    def move(self):
        """
        A method that is an abstract method that does nothing
        """


class TextController(Controller):
    """
    """
    def move(self, player):
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                # If pressed key is ESC quit program
                if event.key == pygame.K_ESCAPE:
                    self._print("ESC was pressed. quitting...")
                    self.quit()
                elif event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_DOWN:
                    player.crouch()
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()
                else:
                    player.normal()

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_a]:
                    player.attack()
                elif pressed[pygame.K_d]:
                    player.defense()
                elif pressed[pygame.K_w]:
                    player.power()
