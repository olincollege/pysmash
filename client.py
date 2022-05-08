import sys
import pygame
import asyncio
import pickle

from view import WindowView
from controller import KeyboardController, KeyboardController2
from view import WindowView
from characters.mario import Mario

import messages

HOST = sys.argv[1]
CHARACTER = sys.argv[2]

pygame.init()
clock = pygame.time.Clock()

async def main():
    player = Mario()
    controller = KeyboardController(player)

    reader, writer = await asyncio.open_connection(HOST, 5555)
    print('connection made')

    player_num = await reader.read(100)
    print(player_num.decode())
    if player_num == 'player1':
        player.direction = 'right'
    else:
        player.direction = 'left'

    writer.write(pickle.dumps(messages.make_client_message(player)))
    await writer.drain()
    
    game = await pickle.loads(reader.read(1024))
    viewer = WindowView(game, 1240, 720)

    while True:
        controller.move()
        writer.write(pickle.dumps(player))
        await writer.drain()
        game = await pickle.loads(reader.read(1024))
        player = exec(f'game.{player_num}')
        self.viewer.draw(game)
        self.clock.tick(60)

asyncio.run(main())

    
