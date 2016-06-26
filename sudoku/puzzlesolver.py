"""
puzzlesolver.py
:created on: 20160624
__author__ = 'Frederic Dupont'
:License: GPL3
"""


__author__ = 'Fred Dupont'


import sys

from sudoku import puzzleconstants as p_const
from sudoku.puzzle import Puzzle, make_grid_from_string


class PuzzleSolver(object):
    """
    class that solves a sudoku puzzle
    takes the clone of a puzzle and solves it
    """
    def __init__(self, puzzle_clone):
        self._puzzle = puzzle_clone

    def eliminate_candidates(self):
        """For each square in the grid that has a single assigned value,
        run through the PEERS and eliminate this value from the candidates
        *** This will have to be redone each time the puzzle is cloned ***
        """
        # print('print(self._puzzle)\n', self._puzzle)
        # print(self._puzzle.print_puzzle())
        for square in p_const.SQUARES:
            current_value = self._puzzle.grid[square]
            if current_value not in '.0':
                assert self._puzzle.candidates[square] == p_const.VALUE_TO_CANDIDATES[current_value]
                for peer in p_const.PEERS[square]:
                    self._puzzle.candidates[peer] = self._puzzle.candidates[peer].replace(current_value, '.')
        # print('print(self._puzzle) AFTER \n', self._puzzle)
        # print(self._puzzle.print_puzzle())













# def main(argv):
#     grid_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#     # grid_string = '1...895..5....7819........72.4..8.7.9.71.54.8.8.7..3.531.4..78.4682....3..985...1'
#     # grid_string = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
#     # grid_string = '.82...59....8.1..3..52...78...37842...........27945...91...68..2..7.9....73...95.'
#     # grid_string = '437...189.6.183.......9.536.73..1...9..4.7..1...5..69.124.7.......645.1.356...974'
#     grid2 = make_grid_from_string(grid_string)
#     grid2.parse_grid_candidates()
#     print(grid2)
#     print(grid2.print_puzzle())
#     solver = PuzzleSolver(grid2.clone())
#
#     for idx in range(1):
#         print('step = ', idx, '\n')
#         print(solver._puzzle)
#         print(solver._puzzle.print_puzzle())
#         solver.eliminate_candidates()
#         print(solver._puzzle)
#         print(solver._puzzle.print_puzzle())
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
