"""
Class for Pikachu
"""
# pylint: disable=import-error
import pygame
from spritesheet import SpriteSheet
from player import Player

vec = pygame.math.Vector2


class Pikachu(Player):
    """
    Class for Pikachu character
    """

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=no-member

    def __init__(self):
        """
        Creates Player object with Pikachu's attributes

        Room for expansion with custom functions/attacks
        """
        pygame.init()
        self.spritesheet = SpriteSheet("resources/pikachu_sheet.png")
        right = pygame.transform.scale(
            self.spritesheet.image_at((5, 40, 35, 28), (134, 255, 104)),
            (70, 56),
        )
        left = pygame.transform.flip(right, flip_x=True, flip_y=False)
        tilt_r = pygame.transform.scale(
            self.spritesheet.image_at((14, 3067, 55, 28), (134, 255, 104)),
            (120, 52),
        )
        tilt_l = pygame.transform.flip(tilt_r, flip_x=True, flip_y=False)
        smash_r = self.spritesheet.image_at(
            (316, 1093, 120, 309), (255, 255, 255)
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

        self.name = "pikachu"
        self.weight = 3
        self.speed = 4.5
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 70, 56)
        self.attacks = {
            "tilt": {"damage": 5, "base": 2, "ratio": 1 / 2},
            "smash": {"damage": 20, "base": 8, "ratio": 1},
        }

    def set_boxes(self):
        """
        Update Pikachu's hitboxes and hurtboxes
        """
        if self.attack_cooldown > 0:
            if self.attack == "tilt":
                if self.direction == "left":
                    self.hurtbox = pygame.Rect(
                        self.rect.x + 58, self.rect.y, 62, 56
                    )
                    self.hitbox = pygame.Rect(
                        self.rect.x, self.rect.y + 10, 68, 42
                    )
                else:
                    self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 62, 56)
                    self.hitbox = pygame.Rect(
                        self.rect.x + 52, self.rect.y + 10, 68, 42
                    )
            if self.attack == "smash":
                self.hurtbox = pygame.Rect(
                    self.rect.x + 50, self.rect.y + 236, 68, 52
                )
                self.hitbox = pygame.Rect(
                    self.rect.x + 37, self.rect.y - 15, 49, 322
                )
                self.rect = self.image.get_rect()
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 70, 56)
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
        self.attack_cooldown = 60
        if self.direction == "left":
            self.pos.x -= 30

    def gravity(self):
        """
        Apply acceleration due to gravity to player object except if on a
        platform
        Changes jump count to 3
        """
        self.acc = vec(0, 0.5)
        if 185 < self.pos.x < (185 + 861) and 405 < (self.pos.y - 70) < 430:
            self.vel.y = 1
        if self.knockback_counter <= 0 and 405 > (self.pos.y - 70):
            hits = pygame.sprite.spritecollide(self, self.platforms, False)
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
                self.jump_count = 3
