"""
Class for Mario
"""
# pylint: disable=too-few-public-methods
from player import Player

class Mario(Player):
    """
    Class for Mario character
    """
    def __init__(self):
        """
        Creates Player object with Mario's attributes

        Room for expansion with custom functions/attacks
        """
        super().__init__('mario', 5, 'resources/mario2.png')
