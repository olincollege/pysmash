"""
Main PySmash Game Class
"""
from dataclasses import asdict
import pygame

# pylint: disable=no-member

from view import WindowView
from controller import KeyboardController, KeyboardController2
from characters.mario import Mario
from stages.final_destination import FinalDestination


class Game:
    """
    Main PySmash Game Class
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self):
        """
        Create Game instance, define clock, player, controllers, viewers, and
        sprite groups

        Args:
            player1 (Player): 1st player in PySmash
            player2 (Player): 2nd player in PySmash
        """
        pygame.init()
        self.clock = pygame.time.Clock()

        self.viewer = WindowView(self, 1240, 720)

        self.player1 = Mario("left")
        self.player2 = Mario("right")
        self.p1controller = KeyboardController(self.player1)
        self.p2controller = KeyboardController2(self.player2)
        self.all_sprites = pygame.sprite.Group(self.player1, self.player2)

        self.stage = FinalDestination()
        self.player1.platforms = self.stage.platforms
        self.player2.platforms = self.stage.platforms

    def check_attack(self):
        """
        Check if a player has landed an attack and if so damage and knock them
        back appropriately
        """
        if (
            self.player1.hitbox.colliderect(self.player2.hurtbox)
            and self.player2.damage_cooldown == 0
        ):
            self.player2.health += self.player1.attack_damage
            self.player2.knockback(
                knockback_calcs(self.player1, self.player2),
                self.player1.direction,
                self.player1.knockback_ratio,
            )
        if (
            self.player2.hitbox.colliderect(self.player1.hurtbox)
            and self.player1.damage_cooldown == 0
        ):
            self.player1.health += self.player2.attack_damage
            self.player1.knockback(
                knockback_calcs(self.player2, self.player1),
                self.player2.direction,
                self.player2.knockback_ratio,
            )
    def start_menu(self):
        """
        Creates a start menu and starts or quits the game
        
        Args: none

        Returns: none
        """
        screen = self.viewer.screen
        # white color for text
        color = (255,255,255) 
        # setting color shades for buttons
        color_light = (170,170,170) 
        color_dark = (100,100,100) 
        # get the width and height 
        width = screen.get_width()  
        height = screen.get_height() 
        
        # defining fonts
        small_font = pygame.font.SysFont('Corbel',35) 
        title_font = pygame.font.SysFont('Corbel',80) 

        quit = small_font.render('Quit' , True , color) 
        local = small_font.render('Local' , True , color) 
        local_width,_ = small_font.size("Local")
        online = small_font.render('Online' , True , color) 
        online_width, _ = small_font.size("Online")
        
        title = title_font.render('PySmash' , True , (30,144,255)) 
        title_size,title_size_height = title_font.size("PySmash")

        while True:
            for ev in pygame.event.get(): 
                
                if ev.type == pygame.QUIT: 
                    pygame.quit() 
                    
                #checks if a mouse is clicked 
                if ev.type == pygame.MOUSEBUTTONDOWN: 
                    
                    #if the mouse is clicked on the 
                    # button the game is terminated 
                    if width-140 <= mouse[0] <= width and 0 <= mouse[1] <= 40: 
                        pygame.quit() 
                    
                    elif width/2-280 <= mouse[0] <= width/2 and \
                        height/2 <= mouse[1] <= height/2+40: 
                        return
                    
                    elif width/2+280 <= mouse[0] <= width/2+280+140 and \
                        height/2 <= mouse[1] <= height/2+40: 
                        return    
            # fills the screen with a color 
            screen.fill((25,25,112)) 
            
            # stores the (x,y) coordinates into 
            # the variable as a tuple 
            mouse = pygame.mouse.get_pos() 
            
            
            # create quit button
            if width-140 <= mouse[0] <= width and 0 <= mouse[1] <= 40: 
                pygame.draw.rect(screen,color_light,[width-140,0,140,40]) 
            else: 
                pygame.draw.rect(screen,color_dark,[width-140,0,140,40]) 
            # superimposing the text onto our button 
            screen.blit(quit , (width-140+40,5)) 
            
            # create Local button      
            if width/2-280 <= mouse[0] <= width/2-140 and \
                height/2 <= mouse[1] <= height/2+40: 
                pygame.draw.rect(screen,color_light,
                [width/2-280,height/2,140,40]) 
            else: 
                pygame.draw.rect(screen,color_dark,
                [width/2-280,height/2,140,40]) 
            # superimposing the text onto our button 
            screen.blit(local , (width/2+local_width/2-280,height/2+5)) 
            
            # create Online button      
            if width/2+140 <= mouse[0] <= width/2+280 and height/2 <= mouse[1] \
                <= height/2+40: 
                pygame.draw.rect(screen,color_light,
                    [width/2+140,height/2,140,40]) 
            else: 
                pygame.draw.rect(screen,color_dark, 
                [width/2+140,height/2,140,40]) 
            # superimposing the text onto our button 
            screen.blit(online , (width/2+140+30,height/2+5)) 
            
            
            # Display title
            screen.blit(title , (width/2-title_size/2.,height/4)) 



            # updates the frames of the game 
            pygame.display.update() 
    def mainloop(self):
        """
        Main game loop
        """
        self.start_menu()
        while True:
            if self.player1.stocks == 0 or self.player2.stocks == 0:
                break
            self.p1controller.move()
            self.p2controller.move()
            self.check_attack()
            print(
                f"p1: {self.player1.health} {self.player1.stocks}, \
                p2: {self.player2.health} {self.player2.stocks}"
            )
            self.viewer.draw()
            self.clock.tick(60)
   
def knockback_calcs(attacker, victim):
    """
    Calculate the amount of knockback for a landed attack
    """
    # Using single letter names for ease of reading and writing knockback
    # formula
    # pylint: disable=invalid-name
    h = victim.health
    d = attacker.attack_damage
    w = victim.weight
    s = 0.05
    b = attacker.base_knockback
    knockback = ((((h / 10 + h * d / 20) * w) + 10) * s) + b
    return knockback


if __name__ == "__main__":
    game = Game()
    game.mainloop()
