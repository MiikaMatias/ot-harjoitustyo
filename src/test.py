import unittest
from tests.gameboard_test import TestGameboard

"""
This is a simple script that runs all tests at once. 
"""

def run_tests():
    """Special testing function for ease of use purposes."""
    
    runner = unittest.TextTestRunner(verbosity=2)
    print('Testing gameboard')
    runner.run(unittest.makeSuite(TestGameboard))
    print()

if __name__ == "__main__":
    run_tests()