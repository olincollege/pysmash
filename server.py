import asyncio
from game import Game, knockback_calcs
from messages import make_server_message, implement_player_message, update_game
from player import Player
from characters.mario import Mario
from view import WindowView
import pickle
from pprint import pformat
import pygame
import logging

# logging config
logging.basicConfig(filename='server.log', filemode='w', level=logging.DEBUG)

networks = {}
NAME_DICT = {'mario': Mario}
BUFFER = 1024
player1 = player2 = None
clock = pygame.time.Clock()


async def new_client(reader, writer):
    global player1, player2
    logging.info('New Connection')
    if not networks:
        logging.info('Player 1 Joined')
        networks['p1'] = (reader, writer)
        writer.write(b'player1')
        p1_raw = await reader.read(BUFFER)
        p1_data = pickle.loads(p1_raw)
        player1 = NAME_DICT[p1_data[0]]()
        implement_player_message(player1, p1_data)
    else:
        logging.info('Player 2 Joined')
        networks['p2'] = (reader, writer)
        writer.write(b'player2')
        p2_raw = await reader.read(BUFFER)
        p2_data = pickle.loads(p2_raw)
        player2 = NAME_DICT[p2_data[0]]()
        implement_player_message(player2, p2_data)
    await writer.drain()

async def broadcast(message):
    networks['p1'][1].write(message)
    networks['p2'][1].write(message)
    await networks['p1'][1].drain()
    await networks['p2'][1].drain()

    
async def get_player_data(game):
    p1_raw = await networks['p1'][0].read(BUFFER)
    p1_data = pickle.loads(p1_raw)
    p2_raw = await networks['p2'][0].read(BUFFER)
    p2_data = pickle.loads(p2_raw)
    return update_game(game, p1_data, p2_data)

async def main():
    global player1, player2
    server = await asyncio.start_server(new_client, '127.0.0.1', 5555)
    logging.info('listening on 127.0.0.1 on port 5555')

    while len(networks) < 2:
        await asyncio.sleep(2)

    game = Game(player1, player2)
    logging.info('generated game')

    message = make_server_message(game)
    logging.debug(message)
    await broadcast(pickle.dumps(message))
    logging.info('sent game')
    

    while True:
        game = await get_player_data(game)
        game.check_attack()
        message = make_server_message(game)
        logging.debug(message[0][1], *message[0][7:10])
        await broadcast(pickle.dumps(message))
        # logging.info(game.player1.health, game.player2.health)
        clock.tick(60)

asyncio.run(main())
