"""
Class for Mario
"""
import pygame
from spritesheet import SpriteSheet
from player import Player


class Mario(Player):
    """
    Class for Mario character
    """

    def __init__(self):
        """
        Creates Player object with Mario's attributes

        Room for expansion with custom functions/attacks
        """
        pygame.init()
        self.spritesheet = SpriteSheet("resources/mario_sheet.png")
        right = pygame.transform.scale(
            self.spritesheet.image_at((17, 24, 25, 38), (47, 54, 153)), (50, 76)
        )
        left = pygame.transform.flip(right, flip_x=True, flip_y=False)
        attack_r = pygame.transform.scale(
            self.spritesheet.image_at((46, 1003, 44, 31), (47, 54, 153)), (88, 62)
        )
        attack_l = pygame.transform.flip(attack_r, flip_x=True, flip_y=False)
        self.images = {
            "left": left,
            "right": right,
            "attack_r": attack_r,
            "attack_l": attack_l,
        }
        super().__init__()

        self.name = 'mario'
        self.weight = 5
        self.speed = 4
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 76)
        self.attack_damage = 10
        self.base_knockback = 3
        self.knockback_ratio = 2 / 3

    def set_boxes(self):
        """
        Update Mario's hitboxes and hurtboxes
        """
        if self.attacking > 0 and self.direction == "left":
            self.hurtbox = pygame.Rect(self.rect.x + 38, self.rect.y, 50, 76)
            self.hitbox = pygame.Rect(self.rect.x, self.rect.y + 15, 40, 35)
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 76)
            self.hitbox = pygame.Rect(self.rect.x + 50, self.rect.y + 15, 40, 35)

    def attack(self):
        """
        Perform a tilt attack
        """
        self.attack_damage = 10
        self.base_knockback = 3
        self.knockback_ratio = 2 / 3
        self.attacking = 30
        if self.direction == "left":
            self.pos.x -= 30
