"""
Class for Mario
"""
# pylint: disable=too-few-public-methods
# pylint: disable=import-error
import pygame
from player import Player

class Mario(Player):
    """
    Class for Mario character
    """
    def __init__(self, direction):
        """
        Creates Player object with Mario's attributes

        Room for expansion with custom functions/attacks
        """
        left = pygame.transform.scale(pygame.image.load('resources/mario_left.png'), (80, 120))
        right = pygame.transform.scale(pygame.image.load('resources/mario_right.png'), (80, 120))
        super().__init__(5, {'left': left, 'right': right}, direction, 4, 23, 98, 25, 1, 0)
