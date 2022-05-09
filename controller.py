"""
Contains Controller Classes for PySmash
"""
from abc import ABC, abstractmethod
import pygame


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
        if self.player.attack_cooldown == 0 or \
            self.player.attack == "tilt":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.left()
            if keys[pygame.K_RIGHT]:
                self.player.right()

        # Keys that must be repressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_SPACE]:
                    self.player.jump()
                elif event.key == pygame.K_SLASH:
                    if self.player.attack_cooldown == 0:
                        self.player.tilt()
                elif event.key == pygame.K_PERIOD:
                    if self.player.attack_cooldown == 0:
                        self.player.smash()
                else:
                    pygame.event.post(event)
        self.player.move()


class KeyboardController2(Controller):
    """
    Controller that allows keyboard control of character
    """

    def move(self):
        """
        Takes keyboard input and moves Player object accordingly
        """
        self.player.gravity()
        # Support for keeping a key held down
        if self.player.attack_cooldown == 0 or \
            self.player.attack == "tilt":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.left()
            if keys[pygame.K_d]:
                self.player.right()

        # Keys that must be repressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.player.attack_cooldown == 0:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_1:
                        self.player.tilt()
                    elif event.key == pygame.K_2:
                        self.player.smash()
                if event.key == pygame.K_w:
                    self.player.jump()
        self.player.move()
