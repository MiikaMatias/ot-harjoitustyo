import pygame as pg


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
        self.file = file
        self.col, self.row = col, row

        self.scale_x, self.scale_y = scale_x, scale_y
        self.image = pg.image.load(file)
        self.image = pg.transform.smoothscale(self.image,
                                            (self.image.get_width()*scale_x,
                                            self.image.get_height()*scale_y),)
        self.scale_x, self.scale_y = self.image.get_width()/self.screen.get_width(),self.image.get_height()/self.screen.get_height()

        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width()*col, screen.get_height()*row)

    def draw(self):
        """
        Draws the Image in game based on the values of self.rect
        """
        self.rect.center = (self.screen.get_width()*self.col, self.screen.get_height()*self.row)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.text_draw()

    def resize(self, width, height):
        """
        Called upon VIDEORESIZE event, where loads a new image from assets and
        resizes it according to screen parameters. This is done to keep the image
        quality good.

                Parameters:
                        width: screen width
                        height: screen height
        """
        w, h = width*self.scale_x, height*self.scale_y
        self.image = pg.transform.smoothscale(pg.image.load(self.file), 
                                        (w,h),)
        self.rect.size = w,h
        self.image.get_rect().center = (self.screen.get_width()*self.col, self.screen.get_height()*self.row)

    def text_draw(self):
        # required at lower inheritance levels
        pass