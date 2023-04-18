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
from gameobjects.menu.button import Button
from logic.gameboard import GameOfLife
from pygame.locals import *
# pylint: disable=undefined-variable


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

    # we set up screens here, explained further below
    menu = []
    settings = []
    pre_game = []
    game = []
    active_scene = menu

    # Game Objects!
    # Here we define every game object we may use
    # --------------------------------------------------------
    menu_play_button = Button(surface, 0.5, 0.30, 0.45, 0.45,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "pregame")
    menu_play_button.text = "Play"

    menu_options_button = Button(surface, 0.5, 0.45, 0.35, 0.35,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "settings")
    menu_options_button.text = "Options"

    menu_quit_button = Button(surface, 0.5, 0.58, 0.35, 0.35,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "quit")
    menu_quit_button.text = "Quit"


    settings_menu_button = Button(surface, 0.5, 0.20, 0.45, 0.45,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "menu")
    settings_menu_button.text = "Main Menu"

    pregame_menu_button = Button(surface, 0.1, 0.90, 0.25, 0.25,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "menu")
    pregame_menu_button.text = "Main Menu"

    pregame_game_button = Button(surface, 0.8, 0.1, 0.6, 0.6,
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-green_L_btn.png",
                   "src/assets/menu_items/main_menu/CasualGameButtonsVol02/PNG/long/CGB02-blue_L_btn.png",
                   lambda: "game")
    pregame_game_button.text = "Start!"

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

    menu = [menu_play_button, menu_options_button, menu_quit_button]
    settings = [settings_menu_button]
    pre_game = [pregame_menu_button, pregame_game_button]
    game = []
    active_scene = menu
    # --------------------------------------------------------

    # Gameboard !
    # --------------------------------------------------------
    # This guy holds all of the game logic within in. For more information check the
    # logic module from /src/logic.

    gameboard = GameOfLife(6,6)  # pylint: disable=unused-variable

    # --------------------------------------------------------

    # Game loop!
    # --------------------------------------------------------
    # This is the main gameplay loop
    # Each line of this code is ran for every frame
    # A lot of the underlying complexity of the implementation
    # is hidden behind custom functions such as resize()

    pg.mixer.music.set_volume(0.04)
    pg.mixer.music.load('src/assets/sound/music/Menu_soundtrack.wav')
    pg.mixer.music.play(-1)

    while running:
        # this resets the screen
        screen.get_surface().fill((130,190,40))

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
                    image.resize(event.dict['size'][0], event.dict['size'][1])    
                    if isinstance(image, Button):
                        image.text_resize()
            elif event.type == pg.MOUSEBUTTONUP:
                for image in active_scene:
                    if isinstance(image,Button):
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
                            for image in active_scene:
                                image.resize(screen.get_surface().get_width(),
                                             screen.get_surface().get_height())
                                if isinstance(image, Button):
                                    image.text_resize()
                            print(active_scene)

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
            pass

        pg.display.update()

    # --------------------------------------------------------

    # and finally we quit the game
    pg.quit()
    sys.exit()


if __name__ == '__main__':
    main()
