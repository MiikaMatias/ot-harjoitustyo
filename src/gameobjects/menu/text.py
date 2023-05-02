import pygame as pg

PERCENTAGE_OF_SCREEN = 0.2
R = 255
G = 255
B = 255


class Text:

    def __init__(self, text: str, row: float, col: float, scale: float, screen: object) -> None:

        pg.font.init()  # you have to call this at the start,
        # if you want to use this module.

        self.screen = screen
        self.scale = scale
        self.row, self.col = row, col

        # we also define some text for a button
        self.scale_factor = self.screen.get_width()*PERCENTAGE_OF_SCREEN
        self.font = pg.font.Font(
            'src/assets/font/Lambda-Regular.ttf', int(self.scale*(self.scale_factor)))
        self.text = text

    def draw(self):
        """
        Draw the text surface
        """
        self.font = pg.font.Font('src/assets/font/Lambda-Regular.ttf',
                                 int(self.scale*(self.scale_factor)))
        text = self.font.render(self.text, 1, (R, G, B))
        text_rect = text.get_rect(
            center=(self.col*self.screen.get_width(), self.row*self.screen.get_height()))
        self.screen.blit(text, text_rect)

    def resize(self):
        self.scale_factor = self.screen.get_width()*PERCENTAGE_OF_SCREEN
