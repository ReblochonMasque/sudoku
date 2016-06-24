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



if __name__ == '__main__':
    unittest.main()
