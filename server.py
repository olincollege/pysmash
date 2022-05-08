import asyncio
from game import Game, knockback_calcs
import pickle
import pprint

players = {}

async def new_client(reader, writer):
    print('New Connection')
    if not players:
        print('Player 1 Joined')
        players['p1'] = (reader, writer)
        writer.write(b'player1')
        p1_raw = await reader.read(1024)
        p1_data = pickle.loads(p1_raw)
    else:
        print('Player 2 Joined')
        players['p2'] = (reader, writer)
        writer.write(b'player2')
        p2_raw = await reader.read(1024)
        p2_data = pickle.loads(p2_raw)
    await writer.drain()
    
async def main():
    server = await asyncio.start_server(new_client, '127.0.0.1', 5555)
    print('listening on 127.0.0.1 on port 5555')

    while len(players) < 2:
        await asyncio.sleep(.5)

    game = Game(player1, player2)

    while True:
        game.player1 = pickle.loads(players['p1'][0].read(1024))
        game.player2 = pickle.loads(players['p2'][0].read(1024))
        game.check_attack()
        players['p1'][1].write(pickle.dumps(game))
        players['p2'][1].write(pickle.dumps(game))

        players['p1'][1].drain()
        players['p2'][1].drain()
        self.clock.tick(60)

asyncio.run(main())
