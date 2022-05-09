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
        tilt_r = pygame.transform.scale(
            self.spritesheet.image_at((46, 1003, 44, 31), (47, 54, 153)),
            (88, 62),
        )
        tilt_l = pygame.transform.flip(tilt_r, flip_x=True, flip_y=False)
        smash_r = pygame.transform.scale(
            self.spritesheet.image_at((73, 303, 47, 43), (47, 54, 153)),
            (96, 86),
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

        self.name = "mario"
        self.weight = 5
        self.speed = 3
        self.smash_cooldown=75
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 76)
        self.attacks = {
            "tilt": {"damage": 10, "base": 5, "ratio": 2 / 3},
            "smash": {"damage": 30, "base": 10, "ratio": 2 / 3},
        }

    def set_boxes(self):
        """
        Update Mario's hitboxes and hurtboxes
        """
        if self.attack_cooldown > 0:
            if self.attack == "tilt":
                if self.direction == "left":
                    self.hurtbox = pygame.Rect(
                        self.rect.x + 38, self.rect.y, 50, 76
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x, self.rect.y + 15, 40, 35
                    )
                else:
                    self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 76)
                    self.hitbox = pygame.Rect(
                        self.rect.x + 50, self.rect.y + 15, 40, 35
                    )
            if self.attack == "smash":
                if self.direction == "left":
                    self.hurtbox = pygame.Rect(
                        self.rect.x + 50, self.rect.y + 10, 46, 76
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x, self.rect.y - 15, 59, 109
                    )
                else:
                    self.hurtbox = pygame.Rect(
                        self.rect.x, self.rect.y + 10, 46, 76
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x + 35, self.rect.y - 15, 59, 109
                    )
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 50, 76)
            self.hitbox = pygame.Rect(0, 0, 0, 0)

    def tilt(self):
        """
        Perform a tilt attack
        """
        self.attack = "tilt"
        self.attack_cooldown = 25
        if self.direction == "left":
            self.pos.x -= 30

    def smash(self):
        """
        Perform a tilt attack
        """
        self.attack = "smash"
        self.attack_cooldown = 75
        if self.direction == "left":
            self.pos.x -= 30
