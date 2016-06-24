"""
puzzlesolver.py
:created on: 20160624
__author__ = 'Frederic Dupont'
:License: GPL3
"""


__author__ = 'Fred Dupont'


import sys

from . import puzzleconstants as p_const
from . import puzzle


class PuzzleSolver(object):
    """
    class that solves a sudoku puzzle
    takes the clone of a puzzle and solves it
    """
    def __init__(self, puzzle_clone):
        self._puzzle = puzzle_clone



# def main(argv):
#     pass
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
