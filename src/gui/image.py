import pygame


class Image():

    def __init__(self, screen, col: int, row: int, scale_x: int,
                 scale_y: int, file: str) -> None:
        """
        Describes an Image in the game. Initialized with image which is 
        rescaled to percentage of screensize.

                    Parameters:
                            screen (pygame.surface.Surface): the screen by which 
                            the object is scaled
                            x (int): defines x coordinate through operation 
                            self.screen.getwidth()*x
                            y (int): defines y coordinate through operation 
                            self.screen.getheight()*y
                            scale_x(int): scale the original image on the x_axis 
                            by factor of [0-1]
                            scale_y(int): scale the original image on the y_axis 
                            by factor of [0-1]
                            file (str): the address of the image

                    Optional:
                            ON (bool): by default True, turns the gameobject on
        """
        self.screen = screen
        self.scale_x, self.scale_y = scale_x, scale_y
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width()*scale_x,
                                            self.image.get_height()*scale_y),)
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()*col, screen.get_height()*row)

        # This special variable is responsible of actually drawing the image
        # if it is not True then the image is not drawn and gameobject functionality
        # will cease.

        # It is the keystone on which scene management is built in my version of pygame
        # scenes are basically just lists of gameobjects that are either on or off.
        # all objects are initially on
        self.is_on = True

    def draw(self, col, row):
        """
        Draws the Image in game.

                Parameters:
                    screen (pygame.surface.Surface): the screen object used in drawing
                    col (int): defines x coordinate through operation self.screen.getwidth()*x
                    row (int): defines y coordinate through operation self.screen.getheight()*y
        """
        col, row = self.screen.get_width()*col, self.screen.get_height()*row
        self.rect.center = (col, row)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
