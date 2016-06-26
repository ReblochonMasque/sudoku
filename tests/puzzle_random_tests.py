"""
sdksolver_stress_unit_tests.py
"stress tests" sdk solver with 10's of thousand valid solved and unsolved puzzles
read from file
:created on: 20160616
__author__ = 'Frederic Dupont'
:License: GPL3
"""

# @TODO: Try to use ddt module --> data driven tests to simplify further

import random
import unittest

from sudoku.puzzle import make_grid_from_string
from tests import get_test_data


class TestFromDataPuzzlesRandomized(unittest.TestCase):
    """stress tests of Puzzle with a large number of solved and unsolved puzzles
    """

    # TODO: add stress tests for invalid solved and unsolved puzzles

    def setUp(self):
        self.path = 'resources/'
        self.picked_tests = list(range(10000))
        random.shuffle(self.picked_tests)
        self.picked_tests = self.picked_tests[:100]

    def test_valid_solved_puzzle(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_solved_data = get_test_data.get_data_from(self.path + 'solved_10000_grids_startwith_123456789.txt')
        self._run_random_data_against_expected(valid_solved_data, len(valid_solved_data))

    def test_valid_unsolved_puzzle_45_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = get_test_data.get_data_from(self.path + 'unsolved_10000_grids_45_numbers.txt')
        self._run_random_data_against_expected(valid_unsolved_data, len(valid_unsolved_data))

    def test_valid_unsolved_puzzle_40_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = get_test_data.get_data_from(self.path + 'unsolved_10000_grids_40_numbers.txt')
        self._run_random_data_against_expected(valid_unsolved_data, len(valid_unsolved_data))

    def test_valid_unsolved_puzzle_35_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = get_test_data.get_data_from(self.path + 'unsolved_10000_grids_35_numbers.txt')
        self._run_random_data_against_expected(valid_unsolved_data, len(valid_unsolved_data))

    def test_valid_unsolved_puzzle_30_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = get_test_data.get_data_from(self.path + 'unsolved_10000_grids_30_numbers.txt')
        self._run_random_data_against_expected(valid_unsolved_data, len(valid_unsolved_data))

    def test_valid_unsolved_puzzle_25_numbers(self):
        """
        uses the solved grids read from a file to test the testing of a valid grid
        """
        valid_unsolved_data = get_test_data.get_data_from(self.path + 'unsolved_10000_grids_25_numbers.txt')
        self._run_random_data_against_expected(valid_unsolved_data, len(valid_unsolved_data))

    def _run_random_data_against_expected(self, data, num_tests):
        """de-duplicate the testing code"""
        for idx in self.picked_tests:
            if idx >= num_tests:
                continue
            else:
                puzzle = make_grid_from_string(data[idx])
                result = puzzle.is_valid()
                self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
