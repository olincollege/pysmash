import pygame

class Map:
    """
    Map class which contains the necessary attributes for the different maps
    """
    
    def __init__(self, img_path, platforms):
        """
        defines the image and atributes of a specific map for the game

        Args: platforms is a list of sprites representing the platforms on
            the map
        """
        self.platforms=platforms
        self.image=img_path

class Platform(pygame.sprite.Sprite):
    """
    class to define a general platform sets the values for its width 
    length and starting coordinates 
    """
    def __init__(self, height, width, start_x, start_y):
        self.rect.x=start_x
        self.rect.y=start_y
        self.rect.width=width
        self.rect.height=height


#creating Final Destination Map Object
final_destination_image=""
final_destination_platforms=[]
final_destination=map(final_destination_image,final_destination_platforms)

#creating Battlefield Map Object
battlefield_image=""
battlefield_platforms=[]
battlefield=map(final_destination_image,final_destination_platforms)