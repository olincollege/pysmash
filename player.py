"""
class doctring
"""
# pylint: disable=unnecessary-pass
import pygame

vec = pygame.math.Vector2
ACC = 5
FRIC = -.25

class Player(pygame.sprite.Sprite):
    """
    Doctring
    """
    def __init__(self, chosen_character, weight, image_path):
        super().__init__()
        self.name = chosen_character
        self.direction = 'left'
        self._health = 0
        self.image = pygame.transform.scale(pygame.image.load(image_path), (50, 100))
        self.mover = 'stand'
        self.rect = self.image.get_rect()
        self.weight = weight
        self.speed = 34 / self.weight

        self.pos = vec((620, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def knockback(self):
        """
        Knock a character back based on knockback amount from an attack

        Args:
            strength (int): amount of knockback to apply to the character
        """
        pass

    def attack(self):
        pass
    def power(self):
        pass
    def defense(self):
        pass
    def crouch(self):
        pass

    def gravity(self):
        """
        Apply acceleration due to gravity to player object
        """
        self.acc = vec(0,0.7)

    @property
    def health(self):
        return self._health

    def damage(self, amount):
        self._health += amount

    def jump(self):
        """
        Make the character jump
        """
        self.vel.y -= 20

    def left(self):
        """
        Move the character left
        """
        self.acc.x = -ACC
        self.mover = 'walk'
        self.direction = 'left'

    def right(self):
        """
        Move the character right
        """
        self.acc.x = ACC
        self.mover = 'walk'
        self.direction = 'right'

    def move(self):
        """
        Take the current acceleration and velocity, calculate player's position,
        and update the player's rectangle
        """
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc

        if self.pos.y > 720:
            self.pos.y = 720
            self.vel.y = 0

        self.rect.midbottom = self.pos

    def normal(self):
        """
        docstring
        """
        self.mover = 'normal'

    def character_image(self):
        """
        docstring
        """
        if self.mover == 'normal':
            if self.direction_one == 'right':
                #self.image = mw2.png
                print('stand right')
            elif self.direction_one == 'left':
                #self.image = mw2.png
                print('stand left')
        elif self.mover == 'walk':
            if self.direction_one == 'right':
                #self.image = mw2.png
                print('walk right')
            elif self.direction_one == 'left':
                #self.image = mw2.png
                print('walk left')
        elif self.mover == 'jump':
            if self.direction_one == 'right':
                #self.image = mw2.png
                print('jump right')
            elif self.direction_one == 'left':
                #self.image = mw2.png
                print('jump left')
        elif self.mover == 'attack':
            if self.direction_one == 'right':
                #self.image = mw2.png
                print('attack right')
            elif self.direction_one == 'left':
                #self.image = mw2.png
                print('attack left')
