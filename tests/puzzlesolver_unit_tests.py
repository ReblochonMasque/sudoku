"""
puzzlesolver_unit_tests.py
:created on: 20160624
__author__ = 'Frederic Dupont'
:License: GPL3
"""

# import sys

import unittest

from sudoku.puzzle import Puzzle, make_grid_from_string
from sudoku.puzzleconstants import DIGITS, SQUARES
from sudoku.puzzlesolver import PuzzleSolver


class TestPuzzleSolver(unittest.TestCase):

    def test_PuzzleSolver_object(self):
        """tests if a PuzzleSolver object is created
        """
        puzzle_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        puzzle = make_grid_from_string(puzzle_string)
        puzzle_clone = puzzle.clone()
        solver = PuzzleSolver(puzzle_clone)
        self.assertIsInstance(solver, PuzzleSolver)

    def setUp(self):
        grid_string_0 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.grid_0 = make_grid_from_string(grid_string_0)
        self.grid_0.parse_grid_candidates()

        grid_string_1 = '1...895..5....7819........72.4..8.7.9.71.54.8.8.7..3.531.4..78.4682....3..985...1'
        self.grid_1 = make_grid_from_string(grid_string_1)
        self.grid_1.parse_grid_candidates()

        grid_string_2 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.grid_2 = make_grid_from_string(grid_string_2)
        self.grid_2.parse_grid_candidates()

        grid_string_3 = '.82...59....8.1..3..52...78...37842...........27945...91...68..2..7.9....73...95.'
        self.grid_3 = make_grid_from_string(grid_string_3)
        self.grid_3.parse_grid_candidates()

        grid_string_4 = '437...189.6.183.......9.536.73..1...9..4.7..1...5..69.124.7.......645.1.356...974'
        self.grid_4 = make_grid_from_string(grid_string_4)
        self.grid_4.parse_grid_candidates()





if __name__ == '__main__':
    unittest.main()
