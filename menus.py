import pygame

def start_menu(game):
    """
    Creates a start menu and starts or quits the game
    
    Args: game class 
    """
    screen = game.viewer.screen
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
