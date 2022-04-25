"""
class doctring
"""
import pygame

left = 
right = 
current_row = 0
current_column = 0


class Player:
    """
    Doctring
    """
    def __init__(self, mario, velocity_one, position_one, direction_one, attack_one, knockback_one, health_one):
        self.player_1_character = mario
        self.velocity_one = velocity_one
        self.position_one = position_one
        self.direction_one = direction_one 
        self.attack_one = attack_one
        self.knockback_one = knockback_one
        self.health_one = health_one


    def attack(self):

    def power(self):
    
    def defense(self):
    
    def jump(self):
        current_row += 1
        self.postion_one = [current_row][current_column]
    def collide(self):
        
    def move(self):
        while health_one < 300:
            # for event in pygame.event.get():
            #     if (event.type == KEYUP) or (event.type == KEYDOWN):
            #         print "key pressed"
            #         time.sleep(0.1)

            # pressed = pygame.key.get_pressed()
            # if pressed[pygame.K_w]:
            #     print("w is pressed")
            # if pressed[pygame.K_s]:
            #     print("s is pressed")

            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                # If pressed key is ESC quit program
                if event.key == pygame.K_ESCAPE:
                    self._print("ESC was pressed. quitting...")
                    self.quit()
                if event.key == pygame.K_LEFT:
                    current_column -= 1
                    self.position_one = [current_row][current_column]
                    self.direction_one = left
                if event.key == pygame.K_RIGHT:
                    current_column += 1
                    self.position_one = [current_row][current_column]
                    self.direction_one = right
                if event.key == pygame.K_DOWN:
                    
                if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    self.jump()
                if event.key == pygame.K_a:
                    self.attack()
                if event.key == pygame.K_d:
                    self.defense()
                if event.key == pygame.K_w:
                    self.power()
                else:
                    self.position_one = [current_row][current_column]

 