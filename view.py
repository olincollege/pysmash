"""
class docstring
"""
from abc import ABC, abstractmethod

class CharaterView(ABC):
    """
    docstring
    """
    def __init__(self, player, map):

        self._player = player
        self._map = map
    
    @property
    def board(self):
        """
        docstring
        """
        return self._player and self._map

    @abstractmethod
    def draw(self):
        """
        A method that is an abstract method that does nothing
        """
    
class TextView(CharaterView):
    """
   dostring
    """

    def draw(self):
        """
        implement the 'draw' method, which should print the
        map and character
        """
        print(self.player)
        print(self.map)
        

