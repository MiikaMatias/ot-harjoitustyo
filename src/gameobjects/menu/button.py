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
                 scale_y: int, file: str, pressed: str, function_when_pressed) -> None:
        super().__init__(screen, col, row, scale_x, scale_y, file)

        self.pressed_file = pressed
        self.function = function_when_pressed
        pg.font.init()  # you have to call this at the start,
        # if you want to use this module.

        # we also define some text for a button
        self.scale_factor = self.screen.get_width()*0.2
        self.font = pg.font.Font(
            'src/assets/font/Lambda-Regular.ttf', int(self.scale_x*(self.scale_factor)))
        self.text = "null"

        # we define sounds too!
        self.click_sound = pg.mixer.Sound(
            "src/assets/sound/sfx/ButtonClick.wav")
        self.click_sound.set_volume(0.05)
        # here we define a cooldown variable for sounds
        self.cooldown_hover = True

    def text_draw(self):
        """
        Draw the text surface
        """
        self.font = pg.font.Font('src/assets/font/Lambda-Regular.ttf',
                                 int(self.scale_x*(self.scale_factor)))
        text = self.font.render(self.text, 1, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.col*self.screen.get_width(), self.row*self.screen.get_height()))
        self.screen.blit(text, text_rect)

    def check_hover(self):
        """
        Checks if mouse is hovering on object. Given that this is a button, we
        want to change the appearance of it.
        """

        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.flip_appearance(self.pressed_file, 1.05)
            return True
        self.flip_appearance(self.file, 1)
        return False

    def flip_appearance(self, file, scale):
        """
        Changes the appearance and scale of the button.

        Parameters:
                file: the file that we change into
                scale: the scaling we do to standard size
        """
        self.image = pg.transform.smoothscale(pg.image.load(file),
                                              (self.screen.get_width()*self.scale_x*scale,
                                               self.screen.get_height()*self.scale_y*scale),)

        self.image.get_rect().center = (self.screen.get_width() *
                                        self.col, self.screen.get_height()*self.row)

    def activate(self):
        """
        "Activates" the button, or calls its function and returns output.
        """
        pg.mixer.Sound.play(self.click_sound)
        return self.function()

    def text_resize(self):
        self.scale_factor = self.screen.get_width()*0.17
