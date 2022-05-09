"""
Class for Marth
"""
# pylint: disable=import-error
import pygame
from spritesheet import SpriteSheet
from player import Player


class Marth(Player):
    """
    Class for Marth character
    """

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=no-member

    def __init__(self):
        """
        Creates Player object with Marths's attributes

        Room for expansion with custom functions/attacks
        """
        pygame.init()
        self.spritesheet = SpriteSheet("resources/marth_sheet.png")
        right = pygame.transform.scale(
            self.spritesheet.image_at((0, 0, 30, 70), (0,128,0)), (33, 77)
        )
        left = pygame.transform.flip(right, flip_x=True, flip_y=False)
        attack_r = pygame.transform.scale(
            self.spritesheet.image_at((80, 220, 70, 50), (0,128,0)), (70, 50)
        )
        attack_l = pygame.transform.flip(attack_r, flip_x=True, flip_y=False)
        self.images = {
            "left": left,
            "right": right,
            "attack_r": attack_r,
            "attack_l": attack_l,
        }
        super().__init__()

        self.name = 'marth'
        self.weight = 4
        self.speed = 4
        self.attack_damage = 7
        self.base_knockback = 3
        self.knockback_ratio = 1 / 2
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 33, 77)

    def set_boxes(self):
        """
        Update Marth's hitboxes and hurtboxes
        """
        if self.attack_cooldown > 0 and self.direction == "left":
            self.hurtbox = pygame.Rect(self.rect.x + 38, self.rect.y, 25, 50)
            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 40, 35)
        elif self.attack_cooldown > 0 and self.direction == "right":
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 25, 50)
            self.hitbox = pygame.Rect(self.rect.x+25, self.rect.y, 40, 35)
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 33, 77)

    def attack(self):
        """
        Perform a tilt attack
        """
        self.attack_damage = 7
        self.base_knockback = 3
        self.knockback_ratio = 1 / 2
        self.attack_cooldown = 30
        if self.direction == "left":
            self.pos.x -= 30
