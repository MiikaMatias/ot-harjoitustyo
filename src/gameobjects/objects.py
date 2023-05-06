"""
This file defines all gameobjects. The main gameplay loop imports
those objects from here. Almost all of the work happens in the objects
defined by this script.
"""

import numpy as np
from gui.display import Display
from gameobjects.menu.button import Button
from gameobjects.menu.text import Text
from gameobjects.game.tile import Tile
from gameobjects.game.board import Board
from gameobjects.game.score import Scoreboard
from logic.gameboard import GameOfLife
from settings.volume import VolumeObject


# Display is an object that manages the pygame screen;
# it is used to draw items and navigate resolution.
screen = Display(800, 800)
surface = screen.get_surface()

# we set up screens here; these are managed by the main loop
menu = []
settings = []
pre_game = []
game = []

# text objects
title = Text("Game Of Life", 0.1, 0.5, 0.4, surface)

volume_text = Text("", 0.4, 0.5, 0.4, surface)

rules_1 = Text("Rules:", 0.1, 0.1, 0.4, surface)
rules_2 = Text("1) Place tiles!", 0.2, 0.25, 0.4, surface)
rules_3 = Text("2) State changes!", 0.3, 0.314, 0.4, surface)
rules_4 = Text("3) Most points win!", 0.4, 0.325, 0.4, surface)

score_1 = Text("0", 0.9, 0.1, 0.4, surface)
score_1.rgb = (64, 164, 244)
score_2 = Text("0", 0.9, 0.9, 0.4, surface)
score_2.rgb = (176, 62, 80)

title_rounds = Text("3", 0.03, 0.5, 0.3, surface)
title_rounds.rgb = (64, 164, 244)
rounds = Text("1/10", 0.1, 0.5, 0.4, surface)

victory_text = Text("", 0.03, 0.5, 0.3, surface)
versus = Text("VS", 0.5, 0.5, 0.5, surface)
hops_next_end_turn = Text("1", 0.07, 0.59, 0.175, surface)
hops_next_end_turn.rgb = (125, 125, 125)
# text objects

# volume is between 0 and 0.1; modified through settings
volume = VolumeObject(50, volume_text)

# the lambda functions are the message given to the main loop after
# pressing a button, or an increase in volume that talks directly to
# volume

menu_play_button = Button(surface, 0.5, 0.30, 0.45, 0.45,
                          lambda: "pregame")
menu_play_button.text.text = "Play"
menu_options_button = Button(surface, 0.5, 0.45, 0.35, 0.35,
                             lambda: "settings")
menu_options_button.text.text = "Options"
menu_quit_button = Button(surface, 0.5, 0.58, 0.35, 0.35,
                          lambda: "quit")
menu_quit_button.text.text = "Quit"

settings_menu_button = Button(surface, 0.5, 0.20, 0.45, 0.45,
                              lambda: "menu")
settings_menu_button.text.text = "Main Menu"
settings_volup_button = Button(surface, 0.7, 0.50, 0.45, 0.45,
                               lambda: "+")
settings_volup_button.text.text = "+"
settings_voldown_button = Button(surface, 0.3, 0.50, 0.45, 0.45,
                                 lambda: "-")
settings_voldown_button.text.text = "-"


pregame_menu_button = Button(surface, 0.1, 0.90, 0.25, 0.25,
                             lambda: "menu")
pregame_menu_button.text.text = "Main Menu"
pregame_game_button = Button(surface, 0.8, 0.1, 0.6, 0.6,
                             lambda: "game")
pregame_game_button.text.text = "Start!"
# buttons

# tiles for a 10x10 grid
tiles = [Tile(surface, x, y, 1, 1) for x in np.arange(
    0.2, 0.9, 0.07) for y in np.arange(0.2, 0.9, 0.07)]
# tiles

# scenes are fleshed out here; now the main loop can choose which scene;
# group of objects it wants to access and draw through the display object
# at any given point
menu = [title,
        menu_play_button, menu_options_button, menu_quit_button
        ]

settings = [settings_menu_button, settings_volup_button, settings_voldown_button,
            volume_text]

pre_game = [rules_1, rules_2, rules_3, rules_4,
            pregame_menu_button, pregame_game_button]

game = [score_1, score_2, rounds, title_rounds, hops_next_end_turn,
        *tiles]

victory = [victory_text, score_1, score_2, versus,
           pregame_menu_button]
# scenes

# Here we define communicator object board for the internal game logic
# (GameOfLife) and the communicator object betweeen scores (ScoreBoard)
# and text objects on the screen
# The main gameplay loop only talks to game logic through Board/Scoreboard
board = Board(tiles, GameOfLife(10, 10), Scoreboard(
    score_1,
    score_2,
    rounds,
    title_rounds,
    hops_next_end_turn,
    victory_text))
