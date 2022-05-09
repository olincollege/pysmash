"""
Test various functions of PySmash players
"""
import pygame
import pytest
from characters.mario import Mario
from characters.marth import Marth
from characters.pikachu import Pikachu
from game import Game

vec = pygame.math.Vector2


@pytest.fixture
def mario_game():
    """
    Create an instance of the game to test with

    Returns:
        game (Game): game with Mario as player 1
    """
    screen = pygame.display.set_mode([1240, 720])
    mario = Mario()
    game = Game(screen, mario, Marth())
    return game


@pytest.fixture
def marth_game():
    """
    Create an instance of the game to test with

    Returns:
        game (Game): game with Marth as player 1
    """
    screen = pygame.display.set_mode([1240, 720])
    marth = Marth()
    game = Game(screen, marth, Marth())
    return game


@pytest.fixture
def pikachu_game():
    """
    Create an instance of the game to test with

    Returns:
        game (Game): game with Pikachu as player 1
    """
    screen = pygame.display.set_mode([1240, 720])
    pikachu = Pikachu()
    game = Game(screen, pikachu, Marth())
    return game


def test_tilt_cooldown(mario_game):
    """
    Test the attack cool down of mario
    after a tilt attack.
    """
    game = mario_game
    game.player1.tilt()
    assert game.player1.attack_cooldown == 25


def test_smash_cooldown(mario_game):
    """
    Test the attack cool down of mario
    after a smash attack.
    """
    game = mario_game
    game.player1.smash()
    assert game.player1.attack_cooldown == 75


def test_damage(pikachu_game):
    """
    Test the amount of damage done after Pikachu's smash attack
    """
    game = pikachu_game
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.health == 20


def test_knockback(pikachu_game):
    """
    Test the knockback of Pikachu on Marth after a smash attack.
    """
    game = pikachu_game
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.vel == vec(11.92, -11.92)


def test_kill(mario_game):
    """
    Test that Mario dies when he leaves the map
    """
    game = mario_game
    game.player1.pos = vec(-401, -401)
    game.player1.move()
    assert game.player1.stocks == 2


def test_images(mario_game):
    """
    Test the change in sprites when tilt and smash attacks occur in different
    directions
    """
    game = mario_game
    game.player1.left()
    game.player1.tilt()
    game.player1.move()
    assert game.player1.image == game.player1.images["tilt_l"]

    game.player1.right()
    game.player1.smash()
    game.player1.move()
    assert game.player1.image == game.player1.images["smash_r"]


def test_direction(mario_game):
    """
    Test that the direction of Mario changes when he moves right or left
    """
    game = mario_game
    game.player1.left()
    assert game.player1.direction == "left"

    game.player1.right()
    assert game.player1.direction == "right"


def test_marth_tilt_cooldown(marth_game):
    """
    Test the attack cool down of marth
    after a tilt attack.
    """
    game = marth_game
    game.player1.tilt()
    assert game.player1.attack_cooldown == 15


def test_marth_smash_cooldown(marth_game):
    """
    Test the attack cool down of marth
    after a smash attack.
    """
    game = marth_game
    game.player1.smash()
    assert game.player1.attack_cooldown == 75


def test_marth_kill(marth_game):
    """
    Test that Marth dies when he leaves the map
    """
    game = marth_game
    game.player1.pos = vec(-401, -401)
    game.player1.move()
    assert game.player1.stocks == 2


def test_marth_images(marth_game):
    """
    Test Marth's change in sprites when tilt and smash attacks occur in
    different directions
    """
    game = marth_game
    game.player1.left()
    game.player1.tilt()
    game.player1.move()
    assert game.player1.image == game.player1.images["tilt_l"]

    game.player1.right()
    game.player1.smash()
    game.player1.move()
    assert game.player1.image == game.player1.images["smash_r"]


def test_marth_direction(marth_game):
    """
    Test that the direction of Marth changes when he moves right or left
    """
    game = marth_game
    game.player1.left()
    assert game.player1.direction == "left"

    game.player1.right()
    assert game.player1.direction == "right"
