import sys
import pygame
import asyncio
import pickle

from view import WindowView
from controller import KeyboardController, KeyboardController2
from game import Game
from characters.mario import Mario

from messages import make_player_message, implement_player_message, update_game

NAME_DICT = {'mario': Mario}

HOST = sys.argv[1]
CHARACTER = NAME_DICT[sys.argv[2]]
BUFFER = 1024

pygame.init()
clock = pygame.time.Clock()

async def get_player_data(reader, game):
    raw = await reader.read(1024)
    p1_data, p2_data = pickle.loads(raw)
    return update_game(game, p1_data, p2_data)

async def send_player_data(writer, player):
    writer.write(pickle.dumps(make_player_message(player)))
    await writer.drain()

async def main():

    reader, writer = await asyncio.open_connection(HOST, 5555)
    print('connection made')
    player_num = await reader.read(100)
    player_num = player_num.decode()
    print(player_num)
    player = CHARACTER()
    if player_num == 'player1':
        game=Game(player, Mario())
        player = game.player1
        player.direction = 'right'
        player.pnum = 'p1'
    else:
        game=Game(Mario(), player)
        player = game.player2
        player.direction = 'left'
        player.pnum = 'p2'

    controller = KeyboardController(player)

    await send_player_data(writer, player)
    await get_player_data(reader, game)
    viewer = WindowView(game, 1240, 720)

    while True:
        controller.move()
        await send_player_data(writer, player)
        game = await get_player_data(reader, game)
        viewer.draw()
        clock.tick(60)

asyncio.run(main())

    
