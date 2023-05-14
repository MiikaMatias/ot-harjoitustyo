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

# Some modifications to pylint, mostly due to the specifics of pygame

# This suggestion does not work with pygame; allow it and see for yourself.
# Could be that I just don't understand it too.
# pylint: disable=no-member

# this suggestion is not useful either, pygame locals
# import does not work unless done as a wild card for some
# reason
# pylint: disable=wildcard-import

# this suggestion is poor to implement here due
# to the nature of a pygame game loop; I think nested blocks
# are fine in it, as instead of abstracting stuff behind functions
# we can see what's going on directly; maybe if more complexity is added,
# refactoring could be in order.
# pylint: disable=too-many-nested-blocks

# same goes for this one; it is better to define all variables here
# for my purposes, instead of doing it from an external file, as the amount
# of game objects will be relatively small; if you disagree, do inform me.
# I do think that if the project is extended, moving these locals to an external
# file would be smart.
# pylint: disable=too-many-locals

# On the same topic, the pygame gameloop is just gonna have to include many branches.
# Abstracting a lot of it away would subtract from meaningful development time,
# as I'd have to hop around different files instead of looking at the gameloop.
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements

import sys

import pygame as pg
# numpy is needed for np.arange
from pygame.locals import *  # pylint: disable=unused-wildcard-import
# This file contains definitions for all
# objects we will use during the loop
import gameobjects.objects as o
from gameobjects.menu.button import Button
from gameobjects.menu.text import Text
from gameobjects.game.tile import Tile


def main():
    """
    Main loop
    """
    pg.init()
    running = True

    # The function of the gameloop is to manage objects
    # in the active scene; nothing else.

    # We set active scene to be menu in the start; we change
    # it at the press of buttons.
    active_scene = o.menu

    while running:
        # this resets the screen
        o.screen.get_surface().fill((130, 190, 40))

        # we run common, essential functions for
        # all images, such as draw
        for image in active_scene:
            image.draw()

        # then we check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            elif event.type == pg.VIDEORESIZE:
                for image in active_scene:
                    if isinstance(image, Button):
                        image.resize(*event.dict['size'])
                    elif isinstance(image, Text):
                        image.resize()
            elif event.type == pg.MOUSEBUTTONUP:
                for image in active_scene:
                    if isinstance(image, Button):
                        if image.check_hover():
                            activation = image.activate()
                            if activation == "pregame":
                                active_scene = o.pre_game
                            elif activation == "quit":
                                running = False
                            elif activation == "settings":
                                active_scene = o.settings
                            elif activation == "menu":
                                o.board.reset()
                                active_scene = o.menu
                            elif activation == "game":
                                active_scene = o.game
                            elif activation == "+":
                                o.volume.change_vol(10)
                            elif activation == "-":
                                o.volume.change_vol(-10)
                    elif isinstance(image, Tile):
                        if image.check_hover():
                            if o.board.set(*image.coords, True):
                                if o.board.check_turn_end():
                                    pg.time.delay(2000)
                                    active_scene = o.victory

        # and lastly we check if the cursor is hovering over a button
        # in order to activate highlighting
        for obj in active_scene:
            if isinstance(obj, (Tile, Button)):
                obj.check_hover()

        pg.display.update()

    # --------------------------------------------------------

    # and finally we quit the game when the loop ends
    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
