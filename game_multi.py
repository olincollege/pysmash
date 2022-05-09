"""
Main PySmash Game Class
"""
import pygame
from stages.final_destination import FinalDestination


class Game:
    """
    Main PySmash Game Class
    """

    def __init__(self, player1, player2):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups

        Args:
            player1 (Player): 1st player in PySmash
            player2 (Player): 2nd player in PySmash
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.player1 = player1
        self.player2 = player2
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
            attack = self.player2.attacks[self.player2.attack]
            self.player1.health += attack["damage"]
            self.player1.knockback(
                knockback_calcs(self.player2, self.player1),
                self.player2.direction,
                attack["ratio"],
            )


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
