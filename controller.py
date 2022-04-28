"""
Contains Controller Classes for PySmash
"""
import pygame
from abc import ABC, abstractmethod

class Controller(ABC):
    """
    Abstract class to define a character controller
    """
    def __init__(self, player):
        """
        Creates a private instance attribute of a Smash player

        Args: player is an instance of Player
        """
        self._player = player

    @property
    def player(self):
        """
        player property that returns the Player object the controller controls
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
    Controller that allows keyboard control of character
    """
    def move(self):
        """
        Takes keyboard input and moves Player object accordingly
        """
        self.player.gravity()

        # Support for keeping a key held down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.left()
        if keys[pygame.K_RIGHT]:
            self.player.right()

        if keys[pygame.K_a]:
            self.player.attack()
        elif keys[pygame.K_d]:
            self.player.defense()
        elif keys[pygame.K_w]:
            self.player.power()

        # Keys that must be repressed
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

        self.player.move()
