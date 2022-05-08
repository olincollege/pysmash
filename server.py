"""
Contains PySmash Server Code

Must run clients to play
"""
import asyncio
import pickle
import logging
import pygame

from game_multi import Game
from messages import make_server_message, implement_player_message, update_game
from characters.mario import Mario

# logging config
logging.basicConfig(level=logging.DEBUG)

networks = {}
NAME_DICT = {"mario": Mario}
BUFFER = 1024
player1 = player2 = None
clock = pygame.time.Clock()


async def new_client(reader, writer):
    """
    Handle a new client connecting to the server

    Args:
        reader (StreamReader): new client's reader object, given by asyncio
        writer (StreamWriter): new client's writer object, given by asyncio

    Returns:
        None
    """
    global player1, player2
    logging.info("New Connection")
    if not networks:
        logging.info("Player 1 Joined")
        networks["p1"] = (reader, writer)
        writer.write(b"player1")
        p1_raw = await reader.read(BUFFER)
        p1_data = pickle.loads(p1_raw)
        player1 = NAME_DICT[p1_data[0]]()
        implement_player_message(player1, p1_data)
    else:
        logging.info("Player 2 Joined")
        networks["p2"] = (reader, writer)
        writer.write(b"player2")
        p2_raw = await reader.read(BUFFER)
        p2_data = pickle.loads(p2_raw)
        player2 = NAME_DICT[p2_data[0]]()
        implement_player_message(player2, p2_data)
    await writer.drain()


async def broadcast(message):
    """
    Broadcast a message to both players on the network

    Args:
        message (bytes): message to send

    Returns:
        None
    """
    networks["p1"][1].write(message)
    networks["p2"][1].write(message)
    await networks["p1"][1].drain()
    await networks["p2"][1].drain()


async def get_player_data(game):
    """
    Read data from both players over network and update game class

    Args:
        game (Game): game instance to update

    Returns:
        game (Game): updated game_instance
    """
    p1_raw = await networks["p1"][0].read(BUFFER)
    p1_data = pickle.loads(p1_raw)
    p2_raw = await networks["p2"][0].read(BUFFER)
    p2_data = pickle.loads(p2_raw)
    return update_game(game, p1_data, p2_data)


async def main():
    """
    Main event loop, create connection and run game
    """
    server = await asyncio.start_server(new_client, "0.0.0.0", 5555)
    logging.info("listening on 0.0.0.0 on port 5555")

    while len(networks) < 2:
        await asyncio.sleep(2)
    await asyncio.sleep(2)

    game = Game(player1, player2)
    logging.info("generated game")

    message = make_server_message(game)
    logging.debug(message)
    await broadcast(pickle.dumps(message))
    logging.info("sent game")

    while True:
        game = await get_player_data(game)
        game.check_attack()
        message = make_server_message(game)
        await broadcast(pickle.dumps(message))
        if game.player1.stocks == 0 or game.player2.stocks == 0:
            return
        clock.tick(60)


asyncio.run(main())
