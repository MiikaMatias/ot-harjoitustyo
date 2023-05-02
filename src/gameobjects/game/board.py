"""
This gameobject is probably going to be the most important one out of all of them.
The game of life will be played on a singular gameobject that consists of multiple cells.
This gameobject is represented by an n by n array GameOfLife instance, and communicates
between the pygame gui and this array.
"""

from logic.gameboard import GameOfLife
from gameobjects.game.score import Scoreboard


class Board():
    """
    Represents an NxN gameboard.
    """

    def __init__(self, tiles: list, game_logic: GameOfLife,
                 score: Scoreboard) -> None:
        self.__scoreboard = score
        self.__tiles = tiles
        self.__logic = game_logic

        self.current_player = 1
        self.__to_place = 3       # this variable gives the squares left

        self.__rounds = 10        # represents rounds left

        self.size = 10

        for column in range(self.size):
            for row in range(self.size):
                i = row * self.size + column
                self.__tiles[i].coords = (row, column)

        # we modify the default file of the tile through these
        self.sprite_dead = "src/assets/game_items/tile000_l.png"
        self.sprite_player_1 = "src/assets/game_items/tile001_l.png"
        self.sprite_player_2 = "src/assets/game_items/tile003_l.png"

    def set(self, i: int, j: int, can_be_rejected=False) -> bool:
        """
        Sets a tile to live for either player 1, 2 or 0 for intra
        class purposes; depending on self.current_player.
        Utilises ranges 1-N.

            Args:
                i: integer, the row coordinate
                j: integer, the column coordinate
                can_be_rejected: boolean, block from overwriting cells directly

            Returns:
                bool if valid move
        """

        if can_be_rejected and self.__logic.gameboard[j, i] != 0:
            return False

        self.__scoreboard.update(self.__logic.p1_score, self.__logic.p2_score,
                                 self.__rounds, self.__to_place)

        # here we set the cell in logic
        self.__logic.set_cell(i + 1, j + 1, self.current_player)

        # get tile
        target_tile = self.__tiles[i * self.size + j]

        if self.current_player == 0:
            target_tile.file = self.sprite_dead
        elif self.current_player == 1:
            target_tile.file = self.sprite_player_1
        else:
            target_tile.file = self.sprite_player_2

        return True

    def fetch_next(self):
        """
        Gets the next state of the board; sets all tiles accordingly
        """

        self.__logic.flyby()

        old_player = self.current_player

        for i in range(self.size):
            for j in range(self.size):
                self.current_player = self.__logic.gameboard[i, j]
                self.set(j, i)

        self.current_player = old_player

    def end_round(self):
        """
        Swaps player, continues round if __to_place == 1
        reduces __to_place by one otherwise
        """
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
            self.__rounds -= 1
            self.fetch_next()
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

        return self.__rounds == 0

    def reset(self):
        self.__logic.reset_board()
        self.__logic.p1_score = 0
        self.__logic.p2_score = 0
        self.__rounds = 10
        self.__scoreboard.update(self.__logic.p1_score, self.__logic.p2_score,
                                 self.__rounds, self.__to_place)
        self.fetch_next()
