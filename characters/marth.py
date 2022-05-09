"""
Class for Marth
"""
import pygame
from spritesheet import SpriteSheet
from player import Player


class Marth(Player):
    """
    Class for Marth character
    """

    def __init__(self):
        """
        Creates Player object with Marths's attributes

        Room for expansion with custom functions/attacks
        """
        pygame.init()
        self.spritesheet = SpriteSheet("resources/marth_sheet.png")
        right = pygame.transform.scale(
            self.spritesheet.image_at((0, 5, 30, 55), (0, 128, 0)), (42, 70)
        )
        left = pygame.transform.flip(right, flip_x=True, flip_y=False)
        tilt_r = pygame.transform.scale(
            self.spritesheet.image_at((80, 215, 70, 55), (0, 128, 0)), (98, 70)
        )
        tilt_l = pygame.transform.flip(tilt_r, flip_x=True, flip_y=False)
        smash_r = pygame.transform.scale(
            self.spritesheet.image_at((80, 650, 78, 73), (0, 128, 0)),
            (117, 110),
        )
        smash_l = pygame.transform.flip(smash_r, flip_x=True, flip_y=False)

        self.images = {
            "left": left,
            "right": right,
            "tilt_r": tilt_r,
            "tilt_l": tilt_l,
            "smash_r": smash_r,
            "smash_l": smash_l,
        }
        super().__init__()

        self.name = "marth"
        self.weight = 4
        self.speed = 4
        self.smash_cooldown=75
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 42, 70)
        self.attacks = {
            "tilt": {"damage": 7, "base": 3, "ratio": 1 / 2},
            "smash": {"damage": 25, "base": 8, "ratio": 2 / 3},
        }

    def set_boxes(self):
        """
        Update Marth's hitboxes and hurtboxes
        """
        if self.attack_cooldown > 0:
            if self.attack == "tilt":
                if self.direction == "left":
                    self.hurtbox = pygame.Rect(
                        self.rect.x + 38, self.rect.y, 50, 70
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x, self.rect.y + 10, 50, 35
                    )
                    self.rect = self.image.get_rect()
                elif self.direction == "right":
                    self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 70)
                    self.hitbox = pygame.Rect(
                        self.rect.x + 50, self.rect.y + 10, 50, 35
                    )
                    self.rect = self.image.get_rect()
            if self.attack == "smash":
                if self.direction == "left":
                    self.hurtbox = pygame.Rect(
                        self.rect.x + 37 * 1.4,
                        self.rect.y + 31 * 1.4,
                        42 * 1.4,
                        42 * 1.4,
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x, self.rect.y, 66 * 1.4, 60 * 1.4
                    )
                    self.rect = self.image.get_rect()
                elif self.direction == "right":
                    self.hurtbox = pygame.Rect(
                        self.rect.x, self.rect.y + 31 * 1.4, 42 * 1.4, 42 * 1.4
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x + 12 * 1.4, self.rect.y, 66 * 1.4, 60 * 1.4
                    )
                    self.rect = self.image.get_rect()
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 42, 70)
            self.hitbox = pygame.Rect(0, 0, 0, 0)
            self.rect = self.image.get_rect()

    def tilt(self):
        """
        Perform a tilt attack
        """
        self.attack = "tilt"
        self.attack_cooldown = 15
        if self.direction == "left":
            self.pos.x -= 30

    def smash(self):
        """
        Perform a smash attack
        """
        self.attack = "smash"
        self.attack_cooldown = 75
        if self.direction == "left":
            self.pos.x -= 30
