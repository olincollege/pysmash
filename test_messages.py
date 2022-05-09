"""
Test code that encodes and decodes player classes into network-sendable messages
"""
import pygame
import pytest
from characters.mario import Mario
from characters.marth import Marth
from game import Game
from messages import make_player_message, implement_player_message

vec = pygame.math.Vector2


@pytest.fixture
def mario_game():
    """
    Pytest Fixture that creates a game with Mario as player 1to test with

    Returns:
        game (Game): game with Mario as player 1
    """
    screen = pygame.display.set_mode([1240, 720])
    mario_player = Mario()
    game = Game(screen, mario_player, Marth())
    return game


message = []
def test_making_messages(mario_game):
    """
    Test that a player class can successfully be translated into a message

    Args:
        mario (Game): Game with Mario as player 1
    """
    global message
    sender = mario_game
    sender.player1.jump_count = 2
    sender.player1.attack = "smash"
    sender.player1.health = 47
    message = make_player_message(sender.player1)

    assert message[2] == 47
    assert message[10] == 2
    assert message[15] == "smash"


def test_implementing_messages(mario_game):
    """
    Test that a message can be integrated into an existing player class

    Args:
        mario (Game): Game with Mario as player 1
    """
    receiver = mario_game
    receiver.player1 = implement_player_message(receiver.player1, message)
    assert receiver.player1.health == 47
    assert receiver.player1.jump_count == 2
    assert receiver.player1.attack == "smash"
