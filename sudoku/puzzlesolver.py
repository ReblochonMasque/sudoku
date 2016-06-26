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
        for square in p_const.SQUARES:
            current_value = self._puzzle.grid[square]
            if current_value not in '.0':
                assert self._puzzle.candidates[square] == p_const.VALUE_TO_CANDIDATES[current_value]
                for peer in p_const.PEERS[square]:
                    self._puzzle.candidates[peer] = self._puzzle.candidates[peer].replace(current_value, '.')

    def propagate(self):
        """if a UNIT has only one possible place for a value,
         assign this value there, and adjust the candidates for this place
        """
        for unit in p_const.UNIT_LISTS:
            for digit in p_const.DIGITS:
                result = []
                for square in unit:
                    if digit in self._puzzle.candidates[square]:
                        result.append(square)
                if len(result) == 1:
                    self._puzzle.grid[result[0]] = digit
                    self._puzzle.candidates[result[0]] = p_const.VALUE_TO_CANDIDATES[digit]

    def fill_singles(self):
        """
        completes a unit that is missing only one value
        by updating the grid and the candidates values
        """
        for unit in p_const.UNIT_LISTS:
            result = []
            res_string = [str(_) for _ in range(1, 10)]
            for square in unit:
                val = self._puzzle.grid[square]
                if val in '.0':
                    result.append(square)
                else:
                    res_string[int(val) - 1] = '.'
            if len(result) == 1:
                self._puzzle.grid[result[0]] = p_const.CANDIDATES_TO_VALUE[''.join(res_string)]
                self._puzzle.candidates[result[0]] = ''.join(res_string)





#
# def main(argv):
#     # grid_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#     grid_string = '1...895..5....7819........72.4..8.7.9.71.54.8.8.7..3.531.4..78.4682....3..985...1'
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
#
#         solver.eliminate_candidates()
#         solver.propagate()
#         print(solver._puzzle)
#         print(solver._puzzle.print_puzzle())
#         solver.fill_singles()
#         print(solver._puzzle)
#         print(solver._puzzle.print_puzzle())
#
#
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
