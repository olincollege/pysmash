"""
class doctring
"""
# pylint: disable=unnecessary-pass
import pygame

vec = pygame.math.Vector2
FRIC = -.25

class Player(pygame.sprite.Sprite):
    """
    Doctring
    """
    def __init__(self, weight, images, direction, acc):
        super().__init__()
        self.direction = direction
        self._health = 0
        self.images = images
        self.image = self.images['right']
        self.mover = 'stand'
        self.rect = self.image.get_rect()
        self.weight = weight
        self.speed = 34 / self.weight
        self._stocks = 3
        self.speed = acc

        self.pos = vec((620, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
        self.jump_count = 0

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
        Apply acceleration due to gravity to player object except if on a
        platform
        """
        self.acc = vec(0,0.5)

        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jump_count = 2

    @property
    def health(self):
        return self._health

    @property
    def stocks(self):
        return self._stocks

    def damage(self, amount):
        self._health += amount

    def jump(self):
        """
        Make the character jump
        """
        if self.jump_count:
            self.vel.y = -15
            self.jump_count -= 1

    def left(self):
        """
        Move the character left
        """
        self.acc.x = -self.speed
        self.image = self.images['left']
        self.mover = 'walk'
        self.direction = 'left'

    def right(self):
        """
        Move the character right
        """
        self.acc.x = self.speed
        self.image = self.images['right']
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

        self.rect.midbottom = self.pos

        self.is_dead()

    def is_dead(self):
        if not(-400 <= self.pos.x <= 1640) or  not(-400 <= self.pos.y <= 1120):
            self._health = 0
            self._stocks -= 1
            self.pos = vec((620, 360))
            self.direction 
            print('you have died!')

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
