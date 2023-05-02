"""
Game logic
"""

# pylint: disable=too-many-branches
# pylint: disable=too-many-statements
# here the representation of rules as branches
# is intuitively quite clear (get_state())
# so I feel no need to have pylint complain about it

import numpy as np


class GameOfLife():
    """
    This object represents the game of life in memory. It is an n by n array
    of three different states[2,0,1] for each of it's elements. These elements
    abide by game of life rules, wherein the 2 represents player 1 and 1 represents player 2.

    This object will be connected to the pygame GUI.
    """

    def __init__(self, col: int, row: int):
        """
        Initialize the Game of Life instance. We use numpy for the gameboard
        because it is just better than an ordinary list in python, due to
        nondynamic typing, extended functionality and such.

                    Parameters:
                            col (int): width of screen
                            row (int): height of the screen
        """
        self.__width = col
        self.__height = row

        self.p1_score = 0
        self.p2_score = 0

        self.gameboard = np.array(
            [np.array([0 for _ in range(col)]) for _ in range(row)])

        # this is what the next turn will become
        # set by flyby
        self.next_turn_state = np.array(
            [np.array([0 for _ in range(col)]) for _ in range(row)])

    def set_cell(self, col: int, row: int, state: int):
        """
        Set cell to a specific value, either 2,0 or 1

                    Parameters:
                            row (int): j coordinate, starts from 1
                            col (int): i coordinate, starts from 1
                            state (int): 2,0,1
        """
        if state in [2, 0, 1]:
            self.gameboard[(row - 1), (col - 1)] = state
        else:
            raise ValueError(
                f"State of {state} is invalid, must be in [2,0,1]")

    def get_state(self, current: int, ones: int, twos: int) -> int:
        """
        This function returns the future state of a cell based
        on it's surrounding elements

            Parameters:
                current: int defining what the current cell is
                ones: surrounding ones
                twos: surrounding twos

            Output:
                an integer defining the next state
        """
        ret = 0

        if current == 1:
            if twos > ones:     # first priority: do enemies outnumber allies; score to enemy
                self.p2_score += 2
                ret = 0
            elif ones >= 4:     # second priority: are there too many allies
                ret = 0
            elif ones <= 1:     # third priority: are there too few allies
                ret = 0
            else:               # if not, set to alive; get score
                self.p1_score += 1
                ret = 1
        elif current == 2:      # same goes here
            if ones > twos:
                self.p1_score += 2
                ret = 0
            elif twos >= 4:
                ret = 0
            elif twos <= 1:
                ret = 0
            else:
                self.p2_score += 1
                ret = 2
        else:
            if ones == 3 and twos == 3:  # contested empty square?
                ret = 0
            elif ones == 3:
                ret = 1
            elif twos == 3:
                ret = 2

        return ret

    def cells_in_radius(self, x_coord: int, y_coord: int) -> tuple[int, int]:
        """
        Detects how many 1 and 2 cells are nearby. Returns a tuple

                    Parameters:
                            j (int): j coordinate, starts from 1
                            i (int): i coordinate, starts from 1

                    Returns:
                            (ones (int),twos (int)) (tuple): ones and twos tuple
        """
        x_coord, y_coord = (x_coord - 1), (y_coord - 1)

        # this is what we return
        ones = 0
        twos = 0

        if self.gameboard[y_coord, x_coord] == 1:
            ones -= 1
        if self.gameboard[y_coord, x_coord] == 2:
            twos -= 1

        # let's "do the thang"
        # we filter out impossible coordinates
        possible_column_coordinates = list(filter(lambda x: 0 <= x < self.__width,
                                                  [x_coord - 1, x_coord, x_coord + 1]))
        possible_row_coordinates = list(
            filter(lambda x: 0 <= x < self.__height, [y_coord - 1, y_coord, y_coord + 1]))

        # go through the matrix
        for column in possible_column_coordinates:
            for row in possible_row_coordinates:
                ones += self.gameboard[row, column] == 1
                twos += self.gameboard[row, column] == 2

        return ones, twos

    def flyby(self):
        """
        Runs through the whole board and creates the next turn into next_turn_state.
        Then replaces the current boardstate with that, and resets the next_turn_state.
        """
        for j in range(0, self.__width):
            for i in range(0, self.__height):
                current = self.gameboard[i, j]
                ones, twos = self.cells_in_radius(j + 1, i + 1)
                self.next_turn_state[i, j] = self.get_state(
                    current, ones, twos)

        self.gameboard = self.next_turn_state

        # we reset the next turn state
        self.next_turn_state = np.array(
            [np.array([0 for _ in range(self.__width)]) for _ in range(self.__height)])

    def __repr__(self) -> str:
        return str(self.gameboard)
