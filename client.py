import sys
import pygame
import asyncio
import pickle

from view import WindowView
from controller import KeyboardController, KeyboardController2

HOST = sys.argv[1]

pygame.init()
clock = pygame.time.Clock()

viewer = WindowView(self, 1240, 720)
controller = KeyboardController(self.player1)

player = Mario('left')

async def main():
    reader, writer = await asyncio.open_connection(HOST, 5555)
    player_num = reader.read().decode()
    writer.write(pickle.dumps(player))
    await writer.drain()

    while True:
        controller.move()
        writer.write(pickle.dumps(player))
        await writer.drain()
        game = await pickle.loads(reader.read())
        player = eval(f'game.{player_num}')
        self.viewer.draw(game)
        self.clock.tick(60)

asyncio.run(main)

    
