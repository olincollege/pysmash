"""
Main PySmash Game Class
"""
from dataclasses import asdict
import pygame


# pylint: disable=no-member

from view import WindowView
from controller import KeyboardController, KeyboardController2
from characters.pikachu import Pikachu
from characters.mario import Mario
from characters.marth import Marth
from stages.final_destination import FinalDestination


class Game:
    """
    Main PySmash Game Class
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, screen, character1, character2):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups

        Args:
            player1 (Player): 1st player in PySmash
            player2 (Player): 2nd player in PySmash
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.viewer = WindowView(self, screen)

        self.player1 = character1
        self.player2 = character2
        self.p1controller = KeyboardController(self.player1)
        self.p2controller = KeyboardController2(self.player2)
        self.all_sprites = pygame.sprite.Group(self.player1, self.player2)

        self.stage = FinalDestination()
        self.player1.platforms = self.stage.platforms
        self.player2.platforms = self.stage.platforms

    def check_attack(self):
        """
        Check if a player has landed an attack and if so damage and knock them
        back appropriately
        """
        if (
            self.player1.hitbox.colliderect(self.player2.hurtbox)
            and self.player2.damage_cooldown == 0
        ):
            self.player2.health += self.player1.attack_damage
            self.player2.knockback(
                knockback_calcs(self.player1, self.player2),
                self.player1.direction,
                self.player1.knockback_ratio,
            )
        if (
            self.player2.hitbox.colliderect(self.player1.hurtbox)
            and self.player1.damage_cooldown == 0
        ):
            self.player1.health += self.player2.attack_damage
            self.player1.knockback(
                knockback_calcs(self.player2, self.player1),
                self.player2.direction,
                self.player2.knockback_ratio,
            )
            
    def gameloop(self):
        """
        Main game loop
        """
        while True:
            if self.player1.stocks == 0 or self.player2.stocks == 0:
                return
            self.p1controller.move()
            self.p2controller.move()
            self.check_attack()
            self.viewer.draw()
            self.clock.tick(60)                

def knockback_calcs(attacker, victim):
    """
    Calculate the amount of knockback for a landed attack
    """
    # Using single letter names for ease of reading and writing knockback
    # formula
    # pylint: disable=invalid-name
    h = victim.health
    d = attacker.attack_damage
    w = victim.weight
    s = 0.04
    b = attacker.base_knockback
    knockback = ((((h / 10 + h * d / 20) * w) + 10) * s) + b
    print(knockback)
    return knockback

def launch_local(screen, player1, player2):
    game = Game(screen, player1, player2)
    game.gameloop()


