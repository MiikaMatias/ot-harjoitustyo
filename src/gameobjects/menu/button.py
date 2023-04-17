"""
Contains the Button gameobject
"""
import pygame as pg
from gui.image import Image

class Button(Image):
    """
    Inherits from: Image
    Present in scene: menu, settings, pre_game, game
    Functionality: 
                - when pressed, calls a function; plays sound effect
                - when hovered over, changes appearance; plays sound effect
                - when not hovered over, if appearance is changed, change to normal
                - what does the button say
    """

    def __init__(self, screen, col: int, row: int, scale_x: int,
                 scale_y: int, file: str, pressed:str, function_when_pressed) -> None:
        super().__init__(screen, col, row, scale_x, scale_y, file)

        self.pressed_file = pressed
        self.function = function_when_pressed

    def check_hover(self):
        """
        Checks if mouse is hovering on object. Given that this is a button, we
        want to change the appearance of it.
        """

        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.flip_appearance(self.pressed_file,1.05)
            return True
        self.flip_appearance(self.file,1)
        return False

    def flip_appearance(self, file, scale):
        """
        Changes the appearance and scale of the button.

        Parameters:
                file: the file that we change into
                scale: the scaling we do to standard size
        """
        self.image = pg.transform.smoothscale(pg.image.load(file), 
                                        (self.screen.get_width()*self.scale_x*scale, self.screen.get_height()*self.scale_y*scale),)
        
        self.image.get_rect().center = (self.screen.get_width()*self.col, self.screen.get_height()*self.row)

    
    def activate(self):
        """
        "Activates" the button, or calls its function and returns output.
        """
        return self.function()
        