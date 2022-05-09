"""
Class for Mario
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
        Creates Player object with Marths's attributes

        Room for expansion with custom functions/attacks
        """
        pygame.init()
        self.spritesheet = SpriteSheet("resources/pikachu_sheet.png")
        right = pygame.transform.scale(
            self.spritesheet.image_at((5, 40, 35, 28), (134,255,104)), (70, 56)
        )
        left = pygame.transform.flip(right, flip_x=True, flip_y=False)
        attack_r = pygame.transform.scale(
            self.spritesheet.image_at((10, 3068, 60, 26), (134,255,104)),
            (120, 52)
        )
        attack_l = pygame.transform.flip(attack_r, flip_x=True, flip_y=False)
        self.images = {
            "left": left,
            "right": right,
            "attack_r": attack_r,
            "attack_l": attack_l,
        }
        super().__init__()

        self.weight = 3
        self.speed = 4.5
        self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 70, 56)

    def set_boxes(self):
        """
        Update Marth's hitboxes and hurtboxes
        """
        if self.attacking > 0 and self.direction == "left":
            self.hurtbox = pygame.Rect(self.rect.x + 50, self.rect.y, 60, 52)
            self.hitbox = pygame.Rect(self.rect.x, self.rect.y+18, 70, 34)
        elif self.attacking > 0 and self.direction == "right":
            self.hurtbox = pygame.Rect(self.rect.x+10, self.rect.y, 60, 52)
            self.hitbox = pygame.Rect(self.rect.x+60, self.rect.y+18, 70, 34)
        else:
            self.hurtbox = pygame.Rect(self.rect.x, self.rect.y, 70, 56)
            self.hitbox = pygame.Rect(self.rect.x + 50, self.rect.y + 15, 40, 35)

    def attack(self):
        """
        Perform a tilt attack
        """
        self.attack_damage = 10
        self.base_knockback = 3
        self.knockback_ratio = 2 / 3
        self.attacking = 15
        if self.direction == "left":
            self.pos.x -= 30
    def gravity(self):
        """
        Apply acceleration due to gravity to player object except if on a
        platform
        Changes jump count to 3
        """
        self.acc = vec(0, 0.5)
        if self.knockback_counter == 0:
            hits = pygame.sprite.spritecollide(self, self.platforms, False)
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
                self.jump_count = 3