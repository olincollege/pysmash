import asyncio
from game import Game, knockback_calcs

players = {}

async def new_client(reader, writer):
    if not players:
        players['p1'] = (reader, writer)
        writer.write(b'player1')
        player1 = await pickle.loads(reader.read())
    else:
        players['p2'] = (reader, writer)
        writer.write(b'player2')
        player2 = await pickle.loads(reader.read())
    await writer.drain()
    
async def main():
    server = await asyncio.start_server(new_client, '127.0.0.1', 5555)
    game = Game()

    while True:
        game.player1 = pickle.loads(players['p1'][0].read())
        game.player2 = pickle.loads(players['p2'][0].read())
        game.check_attack()
        players['p1'][1].write(pickle.dumps(game))
        players['p2'][1].write(pickle.dumps(game))
        players['p1'][1].drain()
        self.clock.tick(60)

asyncio.run(main())
