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

# this suggestion does not work with pygame; allow it and see for yourself
# pylint: disable=no-member

# this suggestion is not useful either, pygame locals
# import does not work unless done as a wild card for some
# reason
# pylint: disable=wildcard-import

# this suggestion is poor to implement here due
# to the nature of a pygame game loop
# pylint: disable=too-many-nested-blocks

# same goes for this one; it is better to define all variables here
# for my purposes, instead of doing it from an external file, as the amount
# of game objects will be relatively small; if you disagree, do inform me
# pylint: disable=too-many-locals

# On the same topic, the pygame gameloop is just gonna have to include many branches.
# Abstracting a lot of it away would subtract from meaningful development time,
# as I'd have to hop around different files instead of looking at the gameloop.
# pylint: disable=too-many-branches
# pylint: disable=too-many-statements

import sys

import pygame as pg
# numpy is needed for np.arange
import numpy as np
from pygame.locals import *  # pylint: disable=unused-wildcard-import
from gui.display import Display
from gameobjects.menu.button import Button
from gameobjects.menu.text import Text
from gameobjects.game.tile import Tile
from gameobjects.game.board import Board
from logic.gameboard import GameOfLife
from gameobjects.game.score import Scoreboard


def main():
    """
    Main loop
    """
    pg.init()
    running = True

    # We set up a Display instance initially
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
    screen = Display(800, 800)
    surface = screen.get_surface()

    # we set up screens here, explained further below
    menu = []
    settings = []
    pre_game = []
    game = []
    active_scene = menu

    # Game Objects!
    # Here we define every game object we will use
    # There are valid arguments for moving this stuff into an external file,
    # but as the amount of non-trivial (copied; tiles, probably abstracted into a
    # larger class later) game objects we need to define seems to be small (<20),
    # I'm personally fine holding these here at the moment. If the instructor
    # deems this as bad practice, then they can tell me.
    #
    # This also makes scene management more pleasant, as we can modify scenes while
    # referring to the actual gameobjects above. On the reader's side I think this
    # is quite clear and easy to understand too; first we have game objects, then
    # we define screens and where they belong;
    # we can even highlight objects and see them in scenes!
    # --------------------------------------------------------

# text
    title = Text("Game Of Life", 0.1,0.5,0.4, surface)

    rules_1 = Text("Rules:", 0.1,0.1,0.4, surface)
    rules_2 = Text("1) Place tiles!", 0.2,0.25,0.4, surface)
    rules_3 = Text("2) Press Go!", 0.3,0.225,0.4, surface)
    rules_4 = Text("3) Most points win!", 0.4,0.325,0.4, surface)

    score_1 = Text("0", 0.9,0.1,0.4, surface)
    score_1.rgb = (64,164,244)
    score_2 = Text("0", 0.9,0.9,0.4, surface)
    score_2.rgb = (176,62,80)

    title_rounds = Text("3", 0.03,0.5,0.3, surface)
    title_rounds.rgb = (64,164,244)
    rounds = Text("10", 0.1,0.5,0.4, surface)
# text

# buttons
    long_buttons = "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/"
    game = "src/assets/game_items/"

    menu_play_button = Button(surface, 0.5, 0.30, 0.45, 0.45,
                              f"{long_buttons}CGB02-green_L_btn.png",
                              f"{long_buttons}CGB02-blue_L_btn.png",
                              lambda: "pregame")
    menu_play_button.text.text = "Play"

    menu_options_button = Button(surface, 0.5, 0.45, 0.35, 0.35,
                                 f"{long_buttons}CGB02-green_L_btn.png",
                                 f"{long_buttons}CGB02-blue_L_btn.png",
                                 lambda: "settings")
    menu_options_button.text.text = "Options"

    menu_quit_button = Button(surface, 0.5, 0.58, 0.35, 0.35,   
                              f"{long_buttons}CGB02-green_L_btn.png",
                              f"{long_buttons}CGB02-blue_L_btn.png",
                              lambda: "quit")
    menu_quit_button.text.text = "Quit"

    settings_menu_button = Button(surface, 0.5, 0.20, 0.45, 0.45,
                                  f"{long_buttons}CGB02-green_L_btn.png",
                                  f"{long_buttons}CGB02-blue_L_btn.png",
                                  lambda: "menu")
    settings_menu_button.text.text = "Main Menu"

    pregame_menu_button = Button(surface, 0.1, 0.90, 0.25, 0.25,
                                 f"{long_buttons}CGB02-green_L_btn.png",
                                 f"{long_buttons}CGB02-blue_L_btn.png",
                                 lambda: "menu")
    pregame_menu_button.text.text = "Main Menu"

    pregame_game_button = Button(surface, 0.8, 0.1, 0.6, 0.6,
                                 f"{long_buttons}CGB02-green_L_btn.png",
                                 f"{long_buttons}CGB02-blue_L_btn.png",
                                 lambda: "game")
    pregame_game_button.text.text = "Start!"
# buttons

# tiles
    tiles = [Tile(surface, x, y, 1, 1) for x in np.arange(
        0.2, 0.9, 0.07) for y in np.arange(0.2, 0.9, 0.07)]
# tiles

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
    # At the moment the strength of this implementation seems to lie in it's simplicity;
    # we can check the parameters and traits of a gameobject above, and then simply
    # smack in down into a scene, run the game and see it there. This also speaks for
    # defining gameobjects in the main script, and not in a separate file. Of course
    # in a hypothetical world where this project is scaled in a manner where we get
    # to 20+ game objects, this would be undoable. However I'm not living in that world
    #  > : ^ ) (yet)

    menu = [title,
            menu_play_button, menu_options_button, menu_quit_button
            ]

    settings = [settings_menu_button]

    pre_game = [rules_1, rules_2, rules_3, rules_4,
                pregame_menu_button, pregame_game_button]

    game = [score_1, score_2, rounds, title_rounds,
            *tiles]

    active_scene = menu

    # --------------------------------------------------------

    # gamelogic !
    # --------------------------------------------------------
    # This guy holds all of the game logic within in. For more information check the
    # logic module from /src/logic.

    gamelogic = GameOfLife(10, 10)

    scoreboard = Scoreboard(score_1, score_2, rounds, title_rounds)
    board = Board(tiles, gamelogic, scoreboard)

    # --------------------------------------------------------

    # Game loop!
    # --------------------------------------------------------
    # This is the main gameplay loop
    # Each line of this code is ran for every frame
    # A lot of the underlying complexity of the implementation
    # is hidden behind methods such as resize()

    pg.mixer.music.set_volume(0.04)
    pg.mixer.music.load('src/assets/sound/music/Menu_soundtrack.wav')
    pg.mixer.music.play(-1)

    while running:
        # this resets the screen
        screen.get_surface().fill((130, 190, 40))

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
                elif event.key == pg.K_SPACE:
                    board.fetch_next()
            elif event.type == pg.VIDEORESIZE:
                for image in active_scene:
                    if isinstance(image, Button):
                        image.resize(event.dict['size'][0], event.dict['size'][1])
                    elif isinstance(image, Text):
                        image.resize()
            elif event.type == pg.MOUSEBUTTONUP:
                for image in active_scene:
                    if isinstance(image, Button):
                        if image.check_hover():
                            activation = image.activate()
                            if activation == "pregame":
                                active_scene = pre_game
                            elif activation == "quit":
                                running = False
                            elif activation == "settings":
                                active_scene = settings
                            elif activation == "menu":
                                active_scene = menu
                            elif activation == "game":
                                active_scene = game
                    elif isinstance(image, Tile):
                        if image.check_hover():
                            if board.set(*image.coords, True):
                                if board.check_turn_end():
                                    active_scene = menu
                                    board.reset()

        # and lastly we check for special cases in respect
        # to the current active scene
        if active_scene == menu:
            menu_play_button.check_hover()
            menu_options_button.check_hover()
            menu_quit_button.check_hover()
        elif active_scene == settings:
            settings_menu_button.check_hover()
        elif active_scene == pre_game:
            pregame_menu_button.check_hover()
            pregame_game_button.check_hover()
        elif active_scene == game:
            for obj in game:
                if isinstance(obj, Tile):
                    obj.check_hover()

        pg.display.update()

    # --------------------------------------------------------

    # and finally we quit the game
    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
