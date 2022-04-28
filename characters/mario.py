"""
Class for Mario
"""
import sys
sys.path.append('..')
from player import Player

class Mario(Player):
    def __init__(self):
        """
        Creates Player object with Mario's attributes

        Room for expansion with custom functions/attacks
        """
        super().__init__('mario', 5, 2, 1, 'resources/mario.jpg') 
