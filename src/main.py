"""
This script is responsible of the primary gameloop. The loop occurs in main.

Some design principles of this project:

    - I will be recapsulating a lot of the functionality of the original pygame
      library in order to make stuff more interesting and train myself to think
      about stuff from first principles e.g. how will I plan out the architecture
      of a project instead of just executing through a ready lib. Hence you will
      see files like gameobject.py and image.py where I've basically redefined some
      of the things that already happen in pygame, and made them nicer to work with (for me)
    
    - The definition document did state that I will be implementing online functionality.
      This will probably not be the case, as I will focus on working on a clean project.
"""
import sys

import pygame as pg
from gui.display import Display
from gui.image import Image
from logic.gameboard import GameOfLife

 # this suggestion is weird
 # pylint: disable=no-member
 # this suggestion is poor to implement here due
 # to the nature of a pygame game loop
 # pylint: disable=too-many-nested-blocks

def main():
    """
    Main loop
    """
    pg.init()

    running = True

    # We set up a display initially
    # I hope that segregating the display and screen into
    # a single class will allow for abstracting complexity
    # in a neat way in the future.
    #
    # It is smart to note that the display size is dynamic.
    # This means every game object can't be sized absolutely, but
    # instead in terms of width and height of the screen.
    #
    # Access to a gameobject occurs through the attribute
    #
    #       screen.surface
    #
    screen = Display(800, 600)
    surface = screen.get_surface()

    # Screens!
    # --------------------------------------------------------
    # The way this project works with changing screens is done through an
    # array of gameobjects that can be turned on or off.
    #
    # An example would be transferring from main menu to the primary game
    #   1) wait for player to press menu
    #   2) iterate through all menu items and turn off their rendering, collision etc.
    #   3) iterate through all items from the game and turn on their respective features
    #
    # We've now transferred state! No idea if this implementation is good or not but we'll see

    menu = []       # pylint: disable=unused-variable
    settings = []   # pylint: disable=unused-variable
    pre_game = []   # pylint: disable=unused-variable
    game = []       # pylint: disable=unused-variable

    # --------------------------------------------------------

    # Gameboard !
    # This guy holds all of the game logic within in. For more information check the
    # logic module from /src/logic.

    gameboard = GameOfLife(5,5)  # pylint: disable=unused-variable

    # --------------------------------------------------------

    button = Image(surface, 1, 1, 1.1, 0.8,
                   "src/assets/menu_items/main_menu/Talon_buttons/PlayButton.png")

    # each cycle of this function is known as a frame
    while running:

        # sample rectangle
        button.draw(0.5, 0.3)

        for event in pg.event.get():

            # These conditionals handle exit
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # probably modified in the future
                    # to trigger menu instead
                    running = False

        # update display
        pg.display.flip()

    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
