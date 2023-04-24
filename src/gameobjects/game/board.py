"""
This gameobject is probably going to be the most important one out of all of them.
The game of life will be played on a singular gameobject that consists of multiple cells.
This gameobject is represented by an n by n array GameOfLife instance, and communicates 
between the pygame gui and this array.
"""

from logic.gameboard import GameOfLife


class Board():
    """
    Represents an NxN gameboard.
    """

    def __init__(self, tiles: list, game_logic: GameOfLife) -> None:
        self.tiles = tiles
        self.tile_amount = len(tiles)
        self.logic = game_logic
        self.current_player = 1
        self.size = 10

        for column in range(self.size):
            for row in range(self.size):
                i = row*self.size + column
                self.tiles[i].coords = (row, column)

        # we modify the default file of the tile through these
        self.sprite_dead = "src/assets/game_items/tile000_l.png"
        self.sprite_player_1 = "src/assets/game_items/tile001_l.png"
        self.sprite_player_2 = "src/assets/game_items/tile003_l.png"

    def set(self, i: int, j: int):
        """
        Sets a tile to live for either player 1, 2 or 0 for intra
        class purposes; depending on self.current_player.
        Utilises ranges 1-N.

            Args: 
                i: the row coordinate
                j: the column coordinate
        """

        # here we set the cell in logic
        self.logic.set_cell(i+1, j+1, self.current_player)

        # get tile
        target_tile = self.tiles[i*self.size+j]

        if self.current_player == 0:
            target_tile.file = self.sprite_dead
        elif self.current_player == 1:
            target_tile.file = self.sprite_player_1
        else:
            target_tile.file = self.sprite_player_2

        self.end_turn()

    def fetch_next(self):
        """
        Gets the next state of the board; sets all tiles accordingly
        """
        self.logic.flyby()

        for i in range(self.size):
            for j in range(self.size):
                self.current_player = self.logic.gameboard[i, j]
                self.set(j, i)

    def end_turn(self):
        """
        Swaps player
        """
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
