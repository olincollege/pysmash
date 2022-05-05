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
    def __init__(self, weight, images, direction, acc, damage):
        super().__init__()
        self.direction = direction
        self._health = 0
        self.images = images
        self.image = self.images['right']
        self.mover = 'stand'
        self.rect = self.image.get_rect()
        self.weight = weight
        self._stocks = 3
        self.speed = acc

        self.pos = vec((620, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
        self.jump_count = 0

        self.attack_damage = damage
        self.knockback = knockback #knockback growth
        self.attack_base_knockback = attack_base_knockback #base knockback
        self.multiplier = multiplier

        self.attacking = 0

    # def knockback(self, calculation):#, attack_damage):
    #     """
    #     Knock a character back based on knockback amount from an attack

    #     Args:
    #         strength (int): amount of knockback to apply to the character
    #     """
    #     calculation

    def calculation_knockback(self):
        # (((((Percent.Value/10 + Percent.Value*Damage/20) * 200/Weight+100 + 1.4) + 18) + Scaling) + BKB) * Ratio
		# local LaunchSpeed = KnockbackCalculation*0.03
        self.calculation_y = (((self.percent + self.attack_damage) * 0.1 + self.attack_damage * \
        (self.percent + self.attack_damage)) * self.multiplier * 1.4 * \
        (200/(self.weight + 100)) + 18) * self.knockback * 0.01 + self.attack_base_knockback
        if self.direction == 'right':
            self.calculation_x = self.calculation_y
        elif self.direction == 'left':
            self.calculation_x = - self.calculation_y
        self.vel = vec(self.calculation_x, self.calculation_y)


    def attack(self):
        self.attacking = 30
        if self.direction == 'left':
            self.pos.x -= 30

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

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def stocks(self):
        return self._stocks

    @stocks.setter
    def stocks(self, value):
        self._stocks = value

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
        self.set_boxes()
        self.character_image()

        self.is_dead()

    def is_dead(self):
        if not(-400 <= self.pos.x <= 1640) or  not(-400 <= self.pos.y <= 1120):
            self._health = 0
            self._stocks -= 1
            self.pos = vec((620, 360))
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
        if self.attacking > 0:
            self.attacking -= 1
            if self.direction == 'right':
                self.image = self.images['attack_r']
            else:
                self.image = self.images['attack_l']
            if self.attacking == 0 and self.direction == 'left':
                self.pos.x += 30
        else:
            self.hitbox = pygame.Rect(0,0,0,0)
            if self.direction == 'right':
                self.image = self.images['right']
            else:
                self.image = self.images['left']
