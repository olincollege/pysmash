"""
Contains helper functions to create and interpret network messages
"""


def make_player_message(player):
    """
    Build network message from player object

    Args:
        player (Player): Player object to build message from

    Returns:
        message (List): Message to send over network
    """
    return [
        player.name,
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
        player.attack_cooldown,
        player.damage_cooldown,
        player.knockback_counter,
        player.attacks,
        player.attack,
    ]


def implement_player_message(player, message):
    """
    Update player class from network message

    Args:
        player (Player): player to update
        message (List): message to update player from

    Returns:
        player (Player): updated player object
    """
    (
        player.name,
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
        player.attack_cooldown,
        player.damage_cooldown,
        player.knockback_counter,
        player.attacks,
        player.attack,
    ) = message
    return player


def make_server_message(game):
    """
    Build server's outgoing message from game object

    Args:
        game (Game): game object to build message from

    Returns:
        message (List): outgoing server message
    """
    return [
        make_player_message(game.player1),
        make_player_message(game.player2),
    ]


def update_game(game, p1_data, p2_data):
    """
    Update a game object with message data from two players

    Args:
        game (Game): game object to update
        p1_data (List): message data from player 1
        p2_data (List): message data from player 2

    Returns:
        game (Game): updated game object
    """
    game.player1 = implement_player_message(game.player1, p1_data)
    game.player2 = implement_player_message(game.player2, p2_data)
    game.player1.character_image()
    game.player2.character_image()
    return game
