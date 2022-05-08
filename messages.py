def make_player_message(player):
    return [player.name,
        player.pnum,
        player.direction,
        player.health,
        player.stocks,
        player.hitbox,
        player.hurtbox,
        player.pos,
        player.vel,
        player.acc,
        player.rect,
        player.jump_count,
        player.attacking,
        player.damage_cooldown,
        player.knockback_counter,
        player.attack_damage,
        player.base_knockback,
        player.knockback_ratio]

def implement_player_message(player, message):
    player.name, player.pnum, player.direction, player.health, player.stocks, player.hitbox,\
    player.hurtbox, player.pos, player.vel, player.acc, player.rect, player.jump_count,\
    player.attacking, player.damage_cooldown, player.knockback_counter,\
    player.attack_damage, player.base_knockback,\
    player.knockback_ratio = message
    return player

def make_server_message(game):
    return [make_player_message(game.player1), make_player_message(game.player2)]

def update_game(game, p1_data, p2_data):
    game.player1 = implement_player_message(game.player1, p1_data)
    game.player2 = implement_player_message(game.player2, p2_data)
    return game
