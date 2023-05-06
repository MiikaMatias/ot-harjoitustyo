"""
Represents a single cell in pygame.
"""

import pygame as pg
from gui.image import Image


class Tile(Image):

    def __init__(self, screen, col: int, row: int, scale_x: int,
                 scale_y: int) -> None:
        super().__init__(screen, col, row, scale_x, scale_y,
                         "src/assets/game_items/tile000_l.png",)

        self.sprite_hover = "src/assets/game_items/tile002_l.png"
        self.sprite_player_1 = "src/assets/game_items/tile001_l.png"
        self.sprite_player_2 = "src/assets/game_items/tile003_l.png"

        # this variable is set after construction by running
        # through the gameboard
        self.coords = (0, 0)

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
        mean_scaling_factor = (self.scale_x + self.scale_y) / 2
        width, height = width * mean_scaling_factor, width * mean_scaling_factor
        self.rect.size = width, height

        width_to_height = self.screen.get_width() / self.screen.get_height()
        height_to_width = self.screen.get_height() / self.screen.get_width()

        self.image = pg.transform.smoothscale(pg.image.load(self.file),
                                              (((self.screen.get_width() * width_to_height +
                                                 self.screen.get_height() * height_to_width) / 2) *
                                               mean_scaling_factor * self.scale_x,
                                               ((self.screen.get_width() * width_to_height +
                                                 self.screen.get_height() * height_to_width) / 2) *
                                               mean_scaling_factor * self.scale_y),)

        self.image.get_rect().center = (self.screen.get_width() * height_to_width * self.col,
                                        self.screen.get_height() * width_to_height * self.row)

    def check_hover(self):
        """
        Checks if mouse is hovering on object or clicking it.

        Returns:
                bool: mouse on tile
        """

        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.flip_appearance(self.sprite_hover, 1)
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
        mean_scaling_factor = (self.scale_x + self.scale_y) / 2

        width_to_height = self.screen.get_width() / self.screen.get_height()
        height_to_width = self.screen.get_height() / self.screen.get_width()

        self.image = pg.transform.smoothscale(pg.image.load(file),
                                              (((self.screen.get_width() * width_to_height +
                                                 self.screen.get_height() * height_to_width) / 2) *
                                               mean_scaling_factor * scale,
                                               ((self.screen.get_width() * width_to_height +
                                                 self.screen.get_height() * height_to_width) / 2) *
                                               mean_scaling_factor * scale),)

        self.image.get_rect().center = (self.screen.get_width() * width_to_height * self.col,
                                        self.screen.get_height() * height_to_width * self.row)
