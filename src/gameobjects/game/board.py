"""
This gameobject is probably going to be the most important one out of all of them.
The game of life will be played on a singular gameobject that consists of multiple cells.
This gameobject is represented by an n by n array GameOfLife instance, and communicates
between the pygame gui and this array.
"""

from math import sqrt
import pygame as pg
from logic.gameboard import GameOfLife
from gameobjects.game.score import Scoreboard

PATH_TO_FILES = "src/assets/game_items/"


class Board():
    """
    Represents an NxN gameboard. Talks to game logic and the gui,
    and communicates between them. Also tracks rounds, score and such.
    """

    def __init__(self, tiles: list, game_logic: GameOfLife,
                 score: Scoreboard) -> None:
        self.__scoreboard = score
        self.__tiles = tiles
        self.logic = game_logic

        self.__to_place = 3       # this variable gives the squares left
        self.__rounds = 1         # represents rounds

        for column in range(self.logic.size):
            for row in range(self.logic.size):
                i = row * self.logic.size + column
                self.__tiles[i].coords = (row, column)

        # we modify the default file of the tile through these
        self.sprites = ("tile000_l.png",
                        "tile001_l.png",
                        "tile003_l.png")

    def set(self, i: int, j: int, can_be_rejected=False) -> bool:
        """
        Sets a tile to live for either player 1, 2 or 0 for intra
        class purposes; depending on self.logic.current_player.
        Utilises ranges 1-N.

            Args:
                i: integer, the row coordinate
                j: integer, the column coordinate
                can_be_rejected: boolean, block from overwriting cells directly

            Returns:
                bool if valid move
        """

        if can_be_rejected and self.logic.gameboard[j, i] != 0:
            return False

        self.__scoreboard.update(self.logic.p1_score, self.logic.p2_score,
                                 self.__rounds, self.__to_place)

        # here we set the cell in logic
        self.logic.set_cell(i + 1, j + 1, self.logic.current_player)

        # get tile
        target_tile = self.__tiles[i * self.logic.size + j]

        if self.logic.current_player == 0:
            target_tile.file = PATH_TO_FILES + self.sprites[0]
        elif self.logic.current_player == 1:
            target_tile.file = PATH_TO_FILES + self.sprites[1]
        else:
            target_tile.file = PATH_TO_FILES + self.sprites[2]

        return True

    def fetch_next(self):
        """
        Gets the next state of the board; sets all tiles accordingly
        """

        self.logic.flyby()

        old_player = self.logic.current_player

        for i in range(self.logic.size):
            for j in range(self.logic.size):
                self.logic.current_player = self.logic.gameboard[i, j]
                self.set(j, i)

        self.logic.current_player = old_player

    def end_round(self):
        """
        Swaps player, continues round if __to_place == 1
        reduces __to_place by one otherwise
        """
        if self.logic.current_player == 1:
            self.logic.current_player = 2
        else:
            self.logic.current_player = 1
            last = pg.time.get_ticks()
            cooldown = 200
            todo = int(sqrt(self.__rounds))
            self.__rounds += 1
            while todo != 0:
                if pg.time.get_ticks() - last >= cooldown:
                    self.fetch_next()
                    self.draw_tiles()
                    pg.display.update()
                    last = pg.time.get_ticks()
                    todo -= 1

        self.__to_place = 3

    def check_turn_end(self) -> bool:
        """
        Used to manage turn end timer

            Returns
                True if game over
                False if game not over
        """
        if self.__to_place == 1:
            self.end_round()
        else:
            self.__to_place -= 1

        game_over = self.__rounds == 11

        if game_over:
            self.__scoreboard.victory_state(
                self.logic.p1_score, self.logic.p2_score)
        return game_over

    def reset(self):
        self.__scoreboard.game_state()
        self.logic.reset_board()
        self.logic.p1_score = 0
        self.logic.p2_score = 0
        self.__rounds = 1
        self.__scoreboard.update(self.logic.p1_score, self.logic.p2_score,
                                 self.__rounds, self.__to_place)
        self.fetch_next()

    def draw_tiles(self):
        """
        Draw tiles on the screen.
        """
        for tile in self.__tiles:
            tile.flip_appearance(tile.file, 1)
            tile.draw()
