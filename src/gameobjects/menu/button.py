"""
Contains the Button gameobject
"""
import pygame as pg
from gui.image import Image
from .text import Text

PATH_TO_FILES = "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/"


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

    def __init__(self, screen, col: float, row: float, scale_x: int,
                 scale_y: int, function_when_pressed) -> None:
        super().__init__(screen, col, row, scale_x, scale_y,
                         f"{PATH_TO_FILES}CGB02-green_L_btn.png")

        self.pressed_file = f"{PATH_TO_FILES}CGB02-blue_L_btn.png"
        self.function = function_when_pressed

        # we also define some text for a button
        self.text = Text("null", row, col, self.scale_x, self.screen)

        # we define sounds too!
        self.click_sound = pg.mixer.Sound(
            "src/assets/sound/sfx/ButtonClick.wav")
        self.click_sound.set_volume(0.05)
        # here we define a cooldown variable for sounds
        self.cooldown_hover = True

    def draw(self):
        """
        Draws the Button in game based on the values of self.rect
        """
        self.rect.center = (self.screen.get_width() * self.col,
                            self.screen.get_height() * self.row)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.text.draw()

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
                                              (self.screen.get_width() * self.scale_x * scale,
                                               self.screen.get_height() * self.scale_y * scale),)

        self.image.get_rect().center = (self.screen.get_width() *
                                        self.col, self.screen.get_height() * self.row)

    def activate(self):
        """
        "Activates" the button, or calls its function and returns output.
        """
        pg.mixer.Sound.play(self.click_sound)
        return self.function()
