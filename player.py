"""
class doctring
"""
import abc
import pygame

class Player(pygame.sprite.Sprite):
    """
    Doctring
    """
    def __init__(self, chosen_character, weight, \
    direction, knockback, image_path):
        super().__init__()
        self.name = chosen_character
        self.velocity = 0
        self.accel = 0
        self.x_pos = 0
        self.y_pos = -420
        self.direction = 'left'
        self.knockback = knockback
        self._health = 0
        self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 200))
        self.mover = 'stand'
        self.rect = self.image.get_rect()
        self.weight = weight
        self.speed = 34 / self.weight
        self.isjumping = False

    def knockback(self):
        health = 1000 / self.weight
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
        self.rect.y += 3.3 * 3
        self.rect.y = min(self.rect.y, 520)
        self.y_pos = self.rect.y

    @property
    def health():
        return self._health

    def damage(self, amount):
        self._health += amount

    def jump(self):
        """
        docstring
        """
        isjumping = True
        

    def collide(self):
        pass
    def left(self):
        """
        docstring
        """
        self.rect.x -= self.speed
        self.mover = 'walk'
        self.direction_one = 'left'

    def right(self):
        """
        docstring
        """
        self.x_pos += self.speed
        self.rect.x += self.speed
        self.mover = 'walk'
        self.direction_one = 'right'
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
        elif self.mover == 'defense':
            if self.direction_one == 'right':
                #self.image = mw2.png
                print('defense right')
            elif self.direction_one == 'left':
                #self.image = mw2.png
                print('defense left')
        
