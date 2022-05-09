import pygame
import pytest
from characters.mario import Mario
from characters.marth import Marth
from characters.pikachu import Pikachu
from game import Game
from controller import KeyboardController
from messages import make_player_message, implement_player_message

vec = pygame.math.Vector2


@pytest.fixture
def mario():
    """
    Pytest Fixture that creates a game with Mario as player 1to test with

    Returns:
        game (Game): game with Mario as player 1
    """
    screen = pygame.display.set_mode([1240, 720])
    mario = Mario()
    game = Game(screen, mario, Marth())
    return game


def test_making_messages(mario):
    """
    Test that a player class can successfully be translated into a message

    Args:
        mario (Game): Game with Mario as player 1
    """
    global message
    sender = mario
    sender.player1.jump_count = 2
    sender.player1.attack = "smash"
    sender.player1.health = 47
    message = make_player_message(sender.player1)

    assert message[2] == 47
    assert message[10] == 2
    assert message[15] == "smash"


def test_implementing_messages(mario):
    """
    Test that a message can be integrated into an existing player class
    
    Args:
        mario (Game): Game with Mario as player 1
    """
    global message
    receiver = mario
    receiver.player1 = implement_player_message(receiver.player1, message)
    assert receiver.player1.health == 47
    assert receiver.player1.jump_count == 2
    assert receiver.player1.attack == "smash"
