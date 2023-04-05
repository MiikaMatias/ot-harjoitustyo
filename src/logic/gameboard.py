import numpy as np


class GameOfLife():
    """
    This object represents the game of life in memory. It is an n by n array of three different states 
    [2,0,1] for each of it's elements. These elements abide by game of life rules, wherein the 2 represents 
    player 1 and 1 represents player 2. 

    This object will be connected to the pygame GUI. 
    """

    def __init__(self, x:int, y:int):
        """
        Initialize the Game of Life instance. We use numpy for the gameboard because it is just better
        than an ordinary list in python, due to nondynamic typing, extended functionality and such.

                    Parameters:
                            x (int): width of screen
                            y (int): height of the screen
        """
        self.width = x
        self.height = y
        self.gameboard = np.array([np.array([0 for _ in range(x)]) for _ in range(y)])

        # this is what the next turn will become
        # set by flyby
        self.next_turn_state = np.array([np.array([0 for _ in range(x)]) for _ in range(y)])

    def set_cell(self, x:int,y:int, state:int):
        """
        Set cell to a specific value, either 2,0 or 1

                    Parameters:
                            x (int): x coordinate, starts from 1
                            y (int): y coordinate, starts from 1
                            state (int): 2,0,1
        """
        if state in [2,0,1]:
            self.gameboard[(y-1),(x-1)] = state
        else:
            raise Exception(f"State of {state} is invalid, must be in [2,0,1]")
        
    def cells_in_radius(self, x_coord:int, y_coord:int):
        """
        Detects how many 1 and 2 cells are nearby. Returns a tuple

                    Parameters:
                            x (int): x coordinate, starts from 1
                            y (int): y coordinate, starts from 1
                    
                    Returns:
                            (ones (int),twos (int)) (tuple): ones and twos tuple
        """
        x_coord,y_coord = (x_coord-1),(y_coord-1)

        # this is what we return
        ones = 0
        twos = 0

        if self.gameboard[y_coord, x_coord] == 1:
            ones -= 1
        if self.gameboard[y_coord, x_coord] == 2:
            twos -= 1

        # do the thang.... 
        if x_coord == 0:
            if y_coord == 0:
                for y in [0,1]:
                    for x in [0,1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1
            elif y_coord == self.height -1:                
                for y in [self.height-2,self.height-1]:
                        for x in [0,1]:
                            look_at = self.gameboard[y,x]
                            if look_at == 2:
                                twos += 1
                            elif look_at == 1:
                                ones += 1                             
            else:
                for y in [y_coord-1,y_coord,y_coord+1]:
                        for x in [0,1]:
                            look_at = self.gameboard[y,x]
                            if look_at == 2:
                                twos += 1
                            elif look_at == 1:
                                ones += 1             
        elif x_coord == self.width-1:
            if y_coord == 0:
                for y in [0,1]:
                    for x in [self.width-2,self.width-1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1        
            elif y_coord == self.height -1:
                for y in [self.height-2,self.height-1]:
                    for x in [self.width-2,self.width-1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1
            else:
                for y in [y_coord-1,y_coord,y_coord+1]:
                    for x in [self.width-2,self.width-1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1
        else:
            if y_coord == 0:
                for y in [0,1]:
                    for x in [x_coord-1,x_coord,x_coord+1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1 
            elif y_coord == self.height -1:
                for y in [self.height-2,self.height-1]:
                    for x in [x_coord-1,x_coord,x_coord+1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1
            else:
                for y in [y_coord-1,y_coord,y_coord+1]:
                    for x in [x_coord-1,x_coord,x_coord+1]:
                        look_at = self.gameboard[y,x]
                        if look_at == 2:
                            twos += 1
                        elif look_at == 1:
                            ones += 1

        return ones,twos
    
    def flyby(self):
        """
        Runs through the whole board and creates the next turn into next_turn_state. 
        Then replaces the current boardstate with that. 
        """
        for x in range(0,self.width):
            for y in range(0,self.height):
                current = self.gameboard[y,x]
                ones,twos = self.cells_in_radius(x+1,y+1)
                if current == 1:
                    if ones >= 4:
                        self.next_turn_state[y,x] = 0
                    elif ones <= 1:
                        self.next_turn_state[y,x] = 0
                    else:
                        self.next_turn_state[y,x] = 1
                else:
                    if ones == 3:
                        self.next_turn_state[y,x] = 1
        self.gameboard = self.next_turn_state

        # we reset the next turn state    
        self.next_turn_state = np.array([np.array([0 for _ in range(self.width)]) for _ in range(self.height)])

    def __repr__(self):
        return str(self.gameboard)



if __name__ == '__main__':
    gol = GameOfLife(12,12)
    gol.set_cell(1,3,1)
    gol.set_cell(2,4,1)
    gol.set_cell(3,4,1)
    gol.set_cell(3,3,1)
    gol.set_cell(3,2,1)


    for _ in range(10):
        print(gol)
        gol.flyby()
