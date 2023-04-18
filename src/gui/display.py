import pygame
from pygame.locals import *
# pylint: disable=wildcard-import


class Display():

    """
    The purpose of this class is to contain the complexity of the
    underlying display object.
    """

    def __init__(self, width, height):
        """
        Set the initial size of the screen object.

                Parameters:
                        width (int): width of screen
                        height (int): height of the screen
        """
        self.screen_width = width
        self.screen_height = height

        # Here we apply certain pygame locals that make things possible:
        #       HWSURFACE: Use hardware to store surface instead of memory in software.
        #                  Decreases bandwidth. However not necessarily supported by all
        #                  video cards, so if stuff gets all wacky we should disable this
        #       DOUBLEBUF: Doublebuffering applies a separate memory block for
        #                  all draw routines, which reduces graphical artifacts
        #                  such as flickering
        #       RESIZEABLE: Makes the screen dynamically resize
        # source: https://stackoverflow.com/questions/29135147/what-do-hwsurface-and-doublebuf-do

        self.surface = pygame.display.set_mode((width, height),
                                               HWSURFACE | DOUBLEBUF | RESIZABLE)

        pygame.display.set_caption("Game of Life")

    def get_surface(self):
        """
        Getter method for the surface object.

                Returns:
                        self.surface (pygame.surface.Surface): surface object
        """
        return self.surface
