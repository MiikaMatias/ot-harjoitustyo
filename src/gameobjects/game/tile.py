"""
Represents a single cell in pygame. I could have inherited many
functions to this class from "Button" but that did not feel sensible.
After all, this is a game object, not a button   object. 
"""

import pygame as pg
from gui.image import Image


class Tile(Image):

    def __init__(self, screen, col: int, row: int, scale_x: int,
                 scale_y: int, file: str, pressed: str) -> None:
        super().__init__(screen, col, row, scale_x, scale_y, file)

        self.pressed_file = pressed

    def resize(self, width, height):
        """
        Called upon VIDEORESIZE event, where loads a new image from assets and
        resizes it according to screen parameters. This is done to keep the image
        quality good.

                Parameters:
                        width: screen width
                        height: screen height

        This is the Tile specific version of resize, because tiles have to always be
        equal in width and height
        """
        mean_scaling_factor = (self.scale_x+self.scale_y)/2
        width, height = width*mean_scaling_factor, width*mean_scaling_factor
        self.rect.size = width, height

        self.image = pg.transform.smoothscale(pg.image.load(self.file),
                                              (width, height),)
        self.image.get_rect().center = (self.screen.get_width() *
                                        self.col, self.screen.get_height()*self.row)

    def check_hover(self):
        """
        Checks if mouse is hovering on object or clicking it. 
        """

        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.flip_appearance(self.pressed_file, 1)
            return True
        self.flip_appearance(self.file, 1)
        return False

    def flip_appearance(self, file, scale):
        """
        Changes the appearance of the tile.

        Parameters:
                file: the file that we change into
                scale: the scaling we do to standard size

        Here too we have to mess with the scaling to allow for equal
        width and height
        """
        mean_scaling_factor = (self.scale_x+self.scale_y)/2
        self.image = pg.transform.smoothscale(pg.image.load(file),
                                              (self.screen.get_width()*mean_scaling_factor*scale,
                                               self.screen.get_width()*mean_scaling_factor*scale),)

        self.image.get_rect().center = (self.screen.get_width() *
                                        self.col, self.screen.get_height()*self.row)
