"""
Final Destination stage class
"""
from map import Map, Platform
import pygame

class FinalDestination(Map):
    def __init__(self):
        self.platforms = pygame.sprite.Group(Platform(60,961,160,399))
        super().__init__('resources/fd.jpg', self.platforms)
        
