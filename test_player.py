import pygame
import pytest
from characters.mario import Mario
from characters.marth import Marth
from characters.pikachu import Pikachu
from game import Game
from controller import KeyboardController

vec = pygame.math.Vector2


@pytest.fixture
def mario():
    """
    creates an instance of the game

    returns: game is equal to the class Game
    """
    screen = pygame.display.set_mode([1240, 720])
    mario = Mario()
    game = Game(screen, mario, Marth())
    return game

@pytest.fixture
def marth():
    screen = pygame.display.set_mode([1240, 720])
    marth = Marth()
    game = Game(screen, marth, Marth())
    return game

@pytest.fixture
def pikachu():
    """
    creates an instance of the game

    returns: A game which has pikachu and
    Marth as the players
    """
    screen = pygame.display.set_mode([1240, 720])
    pikachu = Pikachu()
    game = Game(screen, pikachu, Marth())
    return game


def test_tilt_cooldown(mario):
    """
    Tests the attack cool down of mario
    after a tilt attack.
    """
    game = mario
    game.player1.tilt()
    assert game.player1.attack_cooldown == 25


def test_smash_cooldown(mario):
    """
    tests the attack cool down of mario
    after a smash attack.
    """
    game = mario
    game.player1.smash()
    assert game.player1.attack_cooldown == 75


def test_damage(pikachu):
    """
    Tests the health of Pikachu
    after taking damage from Pikachu.
    """
    game = pikachu
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.health == 20


def test_knockback(pikachu):
    """
    Tests the knockback of Pikachu
    after a smash attack.
    """
    game = pikachu
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.vel == vec(11.92, -11.92)


def test_kill(mario):
    """
    Tests the stocks of a player
    when that player leaves the
    map.
    """
    game = mario
    game.player1.pos = vec(-401, -401)
    game.player1.move()
    assert game.player1.stocks == 2


def test_images(mario):
    """
    Tests the change in sprites when
    a tilt attack occurs.

    Tests the change in sprites when
    a smash attack occurs.
    """
    game = mario
    game.player1.left()
    game.player1.tilt()
    game.player1.move()
    assert game.player1.image == game.player1.images["tilt_l"]

    game.player1.right()
    game.player1.smash()
    game.player1.move()
    assert game.player1.image == game.player1.images["smash_r"]


def test_direction(mario):
    """
    Tests the direction of mario.
    """
    game = mario
    game.player1.left()
    assert game.player1.direction == "left"

    game.player1.right()
    assert game.player1.direction == "right"

def test_marth_tilt_cooldown(marth):
    game = marth
    game.player1.tilt()
    assert game.player1.attack_cooldown == 15


def test_marth_smash_cooldown(marth):
    game = marth
    game.player1.smash()
    assert game.player1.attack_cooldown == 75


def test_marth_kill(marth):
    game = marth
    game.player1.pos = vec(-401, -401)
    game.player1.move()
    assert game.player1.stocks == 2


def test_marth_images(marth):
    game = marth
    game.player1.left()
    game.player1.tilt()
    game.player1.move()
    assert game.player1.image == game.player1.images["tilt_l"]

    game.player1.right()
    game.player1.smash()
    game.player1.move()
    assert game.player1.image == game.player1.images["smash_r"]


def test_marth_direction(marth):
    game = marth
    game.player1.left()
    assert game.player1.direction == "left"

    game.player1.right()
    assert game.player1.direction == "right"
