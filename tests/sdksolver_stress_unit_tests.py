"""
sdksolver_stress_unit_tests.py
"stress tests" sdk solver with 10's of thousand valid solved and unsolved puzzles
read from file
:created on: 20160616
__author__ = 'Frederic Dupont'
:License: GPL3
"""

import unittest
from sdksolver import make_grid_from_string
import test_data


class TestStressGrid(unittest.TestCase):
    """stress tests of Grid with a large number of solved and unsolved puzzles
    """

    # TODO: add stress tests for invalid solved and unsolved puzzles

    def test_valid_solved_puzzle(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'solved_10000_grids_startwith_123456789.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

    def test_valid_unsolved_puzzle_45_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'unsolved_10000_grids_45_numbers.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

    def test_valid_unsolved_puzzle_40_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'unsolved_10000_grids_40_numbers.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

    def test_valid_unsolved_puzzle_35_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'unsolved_10000_grids_35_numbers.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

    def test_valid_unsolved_puzzle_30_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'unsolved_10000_grids_30_numbers.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

    def test_valid_unsolved_puzzle_25_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        path = '../resources/'
        valid_solved_data = test_data.get_data_from(path + 'unsolved_10000_grids_25_numbers.txt')
        for valid_puzzle in valid_solved_data:
            puzzle = make_grid_from_string(valid_puzzle)
            result = puzzle.is_valid_grid()
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
