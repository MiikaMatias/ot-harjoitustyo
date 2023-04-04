import unittest
import numpy as np
from logic.gameboard import GameOfLife

class TestGameboard(unittest.TestCase):
    def setUp(self):
        self.gameboard = GameOfLife(4,4)

    def test_repr(self):
        self.assertEqual(str(self.gameboard), str(np.array([np.array([0 for _ in range(4)]) for _ in range(4)])))

    def test_set_cell(self):
        self.gameboard.set_cell(1,1,1)
        a = np.array([[1,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]])
        self.assertEqual(True, np.array_equal(self.gameboard.gameboard, a))

    def test_find_friends_corner_top(self):
        self.gameboard.set_cell(1,1,1)
        self.gameboard.set_cell(1,2,1)
        self.gameboard.set_cell(2,2,1)
        a = np.array([[1,1,0,0],
                      [0,1,0,0],    # visual aid
                      [0,0,0,0],
                      [0,0,0,0]])
        self.assertEqual((2,0), self.gameboard.cells_in_radius(2,2))

    def test_find_friends_corner_bot(self):
        self.gameboard.set_cell(4,4,1)
        self.gameboard.set_cell(4,3,1)
        self.gameboard.set_cell(3,4,1)
        a = np.array([[0,0,0,0],
                      [0,0,0,0],    # visual aid
                      [0,0,0,1],
                      [0,0,1,1]])
        self.assertEqual((2,0), self.gameboard.cells_in_radius(4,4))

    def test_find_friends_center(self):
        self.gameboard.set_cell(2,2,1)
        self.gameboard.set_cell(3,3,1)
        self.gameboard.set_cell(3,2,1)
        self.gameboard.set_cell(4,4,1)
        a = np.array([[0,0,0,0],
                      [0,1,1,0],    # visual aid
                      [0,0,1,0],
                      [0,0,0,1]])
        self.assertEqual((3,0), self.gameboard.cells_in_radius(3,3))

    def test_find_enemies_corner_top(self):
        self.gameboard.set_cell(1,1,2)
        self.gameboard.set_cell(1,2,2)
        self.gameboard.set_cell(2,2,1)
        a = np.array([[2,2,0,0],
                      [0,1,0,0],    # visual aid
                      [0,0,0,0],
                      [0,0,0,0]])
        self.assertEqual((0,2), self.gameboard.cells_in_radius(2,2))

    def test_find_enemies_corner_bot(self):
        self.gameboard.set_cell(4,4,1)
        self.gameboard.set_cell(4,3,2)
        self.gameboard.set_cell(3,4,2)
        a = np.array([[0,0,0,0],
                      [0,0,0,0],    # visual aid
                      [0,0,0,2],
                      [0,0,2,1]])
        self.assertEqual((0,2), self.gameboard.cells_in_radius(4,4))

    def test_find_enemies_center(self):
        self.gameboard.set_cell(2,2,2)
        self.gameboard.set_cell(3,3,1)
        self.gameboard.set_cell(3,2,2)
        self.gameboard.set_cell(4,4,2)
        a = np.array([[0,0,0,0],
                      [0,2,2,0],    # visual aid
                      [0,0,1,0],
                      [0,0,0,2]])
        self.assertEqual((0,3), self.gameboard.cells_in_radius(3,3))

    def test_find_friends_and_enemies(self):
        self.gameboard.set_cell(2,2,1)
        self.gameboard.set_cell(3,3,1)
        self.gameboard.set_cell(3,2,2)
        self.gameboard.set_cell(4,4,2)
        a = np.array([[0,0,0,0],
                      [0,2,2,0],    # visual aid
                      [0,0,1,0],
                      [0,0,0,2]])
        self.assertEqual((1,2), self.gameboard.cells_in_radius(3,3))

