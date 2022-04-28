import sys
sys.path.append('..')
from player import Player

class Mario(Player):
    def __init__(self):
        super().__init__('mario', 5, 2, 1, 'resources/mario.jpg') 
