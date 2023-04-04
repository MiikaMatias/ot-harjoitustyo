import pygame


class Image():

    def __init__(self,screen, x:int,y:int,scale_x:int,scale_y:int,file:str, ON = True) -> None:
        """
        Describes an Image in the game. Initialized with image which is rescaled to percentage of screensize.

                    Parameters:
                            screen (pygame.surface.Surface): the screen by which the object is scaled
                            x (int): defines x coordinate through operation self.screen.getwidth()*x
                            y (int): defines y coordinate through operation self.screen.getheight()*y
                            scale_x(int): scale the original image on the x_axis by factor of [0-1]
                            scale_y(int): scale the original image on the y_axis by factor of [0-1]
                            file (str): the address of the image

                    Optional:
                            ON (bool): by default True, turns the gameobject on
        """
        self.screen = screen
        self.scale_x, self.scale_y = scale_x, scale_y
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width()*scale_x, self.image.get_height()*scale_y),)
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()*x,screen.get_height()*y)

        # This special variable is responsible of actually drawing the image
        # if it is not True then the image is not drawn and gameobject functionality
        # will cease.

        # It is the keystone on which scene management is built in my version of pygame
        # scenes are basically just lists of gameobjects that are either on or off.
        self.ON = ON

    def draw(self, x, y):
        """
        Draws the Image in game.

                Parameters:
                    screen (pygame.surface.Surface): the screen object used in drawing
                    x (int): defines x coordinate through operation self.screen.getwidth()*x
                    y (int): defines y coordinate through operation self.screen.getheight()*y
        """
        x,y = self.screen.get_width()*x,self.screen.get_height()*y
        self.rect.center = (x,y)
        self.screen.blit(self.image, (self.rect.x,self.rect.y))
