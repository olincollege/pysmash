"""
Client file - Must have server running

CLI Args:
    Host IP Address
    Character Name
"""
import sys
import asyncio
import pickle
import pygame

from view import WindowView
from controller import KeyboardController
from game_multi import Game
from characters.mario import Mario
from characters.marth import Marth
from characters.pikachu import Pikachu
from messages import make_player_message, update_game

NAME_DICT = {'mario': Mario, 'marth': Marth, 'pikachu': Pikachu}
BUFFER = 1024

pygame.init()
clock = pygame.time.Clock()

async def get_player_data(reader, game):
    """
    Read player data from network and update local game class

    Args:
        reader (StreamReader): reader to read game data from
        game = (Game): game instance to update

    Returns:
        game (Game): updated game instance
    """
    raw = await reader.read(1024)
    p1_data, p2_data = pickle.loads(raw)
    return update_game(game, p1_data, p2_data)


async def send_player_data(writer, player):
    """
    Send local player data over the network

    Args:
        writer (StreamWriter): writer object to send player data through
        player (Player): player object to send data on

    Returns:
        None
    """
    writer.write(pickle.dumps(make_player_message(player)))
    await writer.drain()


async def main(screen, host, character):
    """
    Main event loop, create connection and run game
    """
    reader, writer = await asyncio.open_connection(host, 5555)
    print("connection made")

    player_num = await reader.read(100)
    player_num = player_num.decode()
    print(player_num)

    player = NAME_DICT[character]()
    print(player.name)
    await send_player_data(writer, player)
    other = await reader.read(100)
    print(other.decode())

    if player_num == "player1":
        game = Game(player, NAME_DICT[other.decode()]())
        player = game.player1
        player.direction = "right"
    else:
        game = Game(NAME_DICT[other.decode()](), player)
        player = game.player2
        player.direction = "left"

    controller = KeyboardController(player)

    await get_player_data(reader, game)
    viewer = WindowView(game, screen)

    while True:
        controller.move()
        await send_player_data(writer, player)
        game = await get_player_data(reader, game)
        game.player1.character_image()
        game.player2.character_image()
        viewer.draw()
        clock.tick(60)

def launch_client(screen, host, character):
    asyncio.run(main(screen, host, character))
