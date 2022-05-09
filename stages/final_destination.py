"""
Final Destination stage class
"""
import pygame
from map import Map, Platform


class FinalDestination(Map):
    """
    Define Final Destination stage object
    """

    def __init__(self):
        """
        Create platforms and construct Final Destination map
        """
        self.platforms = pygame.sprite.Group(Platform(1, 861, 185, 399))
        super().__init__("resources/fd.jpg", self.platforms)
