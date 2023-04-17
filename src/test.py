"""
This is a simple script that runs all tests at once.
"""
import unittest
from tests.gameboard_test import TestGameboard


def run_tests():
    """
    Testing function for ease of use purposes.
    """

    runner = unittest.TextTestRunner(verbosity=2)
    print('Testing gameboard')
    runner.run(unittest.makeSuite(TestGameboard))
    print()


if __name__ == "__main__":
    run_tests()
