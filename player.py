"""
class doctring
"""
current_row = 0
current_column = 0
class Player:
    """
    Doctring
    """
    def __init__(self, chosen_character, velocity_one, position_one, \
    direction_one, attack_one, knockback_one, health_one):
        self.player_1_character = chosen_character
        self.velocity_one = velocity_one
        self.position_one = position_one
        self.direction_one = direction_one 
        self.attack_one = attack_one
        self.knockback_one = knockback_one
        self.health_one = health_one
        #self.image = mw1.png
        self.mover = 'stand'
        self.weight = self.player_1_character.weight()
        self.speed = 34 / self.weight

    def knockback(self):
        health = 1000 / self.weight
        pass
    def attack(self):
        pass
    def power(self):
        pass
    def defense(self):
        pass
    def jump(self):
        """
        docstring
        """
        self.mover = 'jump'
        lift = 68 / self.weight
        current_row += lift
        self.postion_one = [current_row][current_column]
    def collide(self):
        pass
    def left(self):
        """
        docstring
        """
        current_column -= self.speed
        self.position_one = [current_row][current_column]
        self.mover = 'walk'
        self.direction_one = 'left'

    def right(self):
        """
        docstring
        """
        current_column += self.speed
        self.position_one = [current_row][current_column]
        self.mover = 'walk'
        self.direction_one = 'right'
    def normal(self):
        """
        docstring
        """
        self.mover = 'normal'
        self.direction_one = self.direction_one
        self.position_one = [current_row][current_column]
    
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
        
