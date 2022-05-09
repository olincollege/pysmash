"""
Contains classes related to creating PySmash maps/stages
"""
import pygame


class Map:
    """
    Map class which contains the necessary attributes for the different maps

    Attributes:
        platforms (pygame.sprite.Group): group of platforms on the stage
        image (pygame.image): image of stage to display
    """

    def __init__(self, img_path, platforms):
        """
        defines the image and atributes of a specific map for the game

        Args: platforms is a list of sprites representing the platforms on
            the map
        """
        self.platforms = platforms
        self.image = pygame.transform.scale(
            pygame.image.load(img_path), (1240, 720)
        )


class Platform(pygame.sprite.Sprite):
    """
    class to define a general platform sets the values for its width
    length and starting coordinates

    Attributes:
        image (pygame.Surface): platform Surface and footprint
        rect (pygame.Rect): Bounding rectangle of platform
    """

    def __init__(self, height, width, start_x, start_y):
        """
        Construct platform object based on given dimensions
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
