"""
Main PySmash Game Class
"""
import pygame
from view import WindowView
from controller import KeyboardController, KeyboardController2
from stages.final_destination import FinalDestination


class Game:
    """
    Main PySmash Game Class

    Class atributes:
        clock: a pygame clock which tracks time used for refresh rate
        viewer: a Window view object
        player1: a player object for player number 1
        player2: a player object for player number 2
        p1controller: a Keyboard Controller for player 1
        p2controller: a Keyboard Controller for player 2
        all_sprites: a sprite group to keep track of collisions
        stage: the map chosen for the game with specific platforms
        these platforms are then set as atributes of each player for
        their internal logic.

    """

    def __init__(self, character1, character2, screen=None):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups

        Args:
            player1 (Player): 1st player in PySmash
            player2 (Player): 2nd player in PySmash
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        if screen is not None:
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
            # Check that we're under halfway through a smash
            if (
                self.player1.attack == "smash"
                and self.player1.attack_cooldown
                < self.player1.smash_cooldown / 2.0
            ) == False:
                attack = self.player1.attacks[self.player1.attack]
                self.player2.health += attack["damage"]
                self.player2.knockback(
                    knockback_calcs(self.player1, self.player2),
                    self.player1.direction,
                    attack["ratio"],
                )

        if (
            self.player2.hitbox.colliderect(self.player1.hurtbox)
            and self.player1.damage_cooldown == 0
        ):
            # Check that we're under halfway through a smash
            if (
                self.player2.attack == "smash"
                and self.player2.attack_cooldown
                < self.player2.smash_cooldown / 2.0
            ) == False:
                attack = self.player2.attacks[self.player2.attack]
                self.player1.health += attack["damage"]
                self.player1.knockback(
                    knockback_calcs(self.player2, self.player1),
                    self.player2.direction,
                    attack["ratio"],
                )

    def gameloop(self):
        """
        Main game loop
        """
        while True:
            if self.player1.stocks == 0:
                return "Player 2"

            elif self.player2.stocks == 0:
                return "Player 1"
            self.p1controller.move()
            self.p2controller.move()
            self.check_attack()
            self.viewer.draw()
            self.clock.tick(60)


def knockback_calcs(attacker, victim):
    """
    Calculate the amount of knockback for a landed attack

    Args:
        attacker (Player): Player that landed the attack
        victim (Player): Player that was attacked
    """
    # Using single letter names for ease of reading and writing knockback
    # formula
    health = victim.health
    damage = attacker.attacks[attacker.attack]["damage"]
    weight = victim.weight
    scaler = 0.04
    base = attacker.attacks[attacker.attack]["base"]
    knockback = (
        (((health / 10 + health * damage / 20) * weight) + 10) * scaler
    ) + base
    return knockback


def launch_local(screen, player1, player2):
    """
    Launch local multiplayer game

    Args:
        screen (pygame.display): screen to play game on
    """
    game = Game(player1, player2, screen)
    return game.gameloop()
