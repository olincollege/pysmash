"""
Main PySmash Game Class
"""
# pylint: disable=no-member
import pygame

from view import WindowView
from controller import KeyboardController, KeyboardController2
from characters.mario import Mario
from stages.final_destination import FinalDestination

class Game:
    """
    Main PySmash Game Class
    """
    def __init__(self, player1, player2):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.viewer = WindowView(self, 1240, 720)

        self.player1 = Mario('left')
        self.player2 = Mario('right')
        self.p1controller = KeyboardController(self.player1)
        self.p2controller = KeyboardController2(self.player2)
        self.all_sprites = pygame.sprite.Group(self.player1, self.player2)

        self.stage = FinalDestination()
        self.player1.platforms = self.stage.platforms
        self.player2.platforms = self.stage.platforms


    def check_attack(self):
        if self.player1.hitbox.colliderect(self.player2.hurtbox):
            self.player2.health += self.player1.attack_damage
            self.player2.knockback(self.knockback_calcs(self.player1, self.player2), self.player1.direction)
        if self.player2.hitbox.colliderect(self.player1.hurtbox):
            self.player1.health += self.player2.attack_damage
            self.player1.knockback(self.knockback_calcs(self.player2, self.player1), self.player2.direction)

    def knockback_calcs(self, attacker, victim):
        h = victim.health
        d = attacker.attack_damage
        w = victim.weight
        b = attacker.base_knockback
        knockback = (((h/10 + h*d/20) * w) + 10) + b
        return knockback

    def mainloop(self):
        """
        Main game loop
        """
        while True:
            self.p1controller.move()
            self.p2controller.move()
            self.check_attack()
            # print(f'p1: {self.player1.health} {self.player1.stocks}, p2: {self.player2.health} {self.player2.stocks}')
            print(self.player2.vel)
            self.viewer.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game(1, 2)
    game.mainloop()
