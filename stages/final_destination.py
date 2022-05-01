"""
Final Destination stage class
"""
# pylint: disable=too-few-public-methods
# pylint: disable=import-error
from map import Map, Platform
import pygame

class FinalDestination(Map):
    """
    Define Final Destination stage object
    """
    def __init__(self):
        """
        Create platforms and construct Final Destination map
        """
        self.platforms = pygame.sprite.Group(Platform(60,961,160,399))
        super().__init__('resources/fd.jpg', self.platforms)
