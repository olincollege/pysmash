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
    screen = pygame.display.set_mode([1240, 720])
    mario = Mario()
    game = Game(screen, mario, Marth())
    return game


@pytest.fixture
def pikachu():
    screen = pygame.display.set_mode([1240, 720])
    pikachu = Pikachu()
    game = Game(screen, pikachu, Marth())
    return game


def test_tilt_cooldown(mario):
    game = mario
    game.player1.tilt()
    assert game.player1.attack_cooldown == 25


def test_smash_cooldown(mario):
    game = mario
    game.player1.smash()
    assert game.player1.attack_cooldown == 75


def test_damage(pikachu):
    game = pikachu
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.health == 20


def test_knockback(pikachu):
    game = pikachu
    game.player1.smash()
    game.player1.move()
    game.player2.move()
    game.check_attack()
    assert game.player2.vel == vec(11.92, -11.92)


def test_kill(mario):
    game = mario
    game.player1.pos = vec(-401, -401)
    game.player1.move()
    assert game.player1.stocks == 2


def test_images(mario):
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
    game = mario
    game.player1.left()
    assert game.player1.direction == "left"

    game.player1.right()
    assert game.player1.direction == "right"
