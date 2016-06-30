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
        :return: False if an inconsistency is discovered --> makes the puzzle invalid
                 True otherwise
        """
        for square in p_const.SQUARES:
            current_value = self._puzzle.grid[square]
            if current_value not in '.0':
                # this says is there is an inconsistency
                # that means it must return False to signal it
                if self._puzzle.candidates[square] != p_const.VALUE_TO_CANDIDATES[current_value]:
                    return False
                for peer in p_const.PEERS[square]:
                    self._puzzle.candidates[peer] = self._puzzle.candidates[peer].replace(current_value, '.')
        return True

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

    def eliminate_propagate_fill(self):
        """
        Propagates the constraints by successively eliminating, propagating and filling the
        solved squares until all constraints have been propagated. (no more change in the puzzle states)
        ...or the puzzle is solved
        """
        while not self._puzzle.is_solved():
            pre_grid_state = repr(self._puzzle)
            pre_candidates_state = str(self._puzzle)
            self.eliminate_candidates()
            self.propagate()
            self.fill_singles()
            post_grid_state = repr(self._puzzle)
            post_candidates_state = str(self._puzzle)
            if pre_grid_state == post_grid_state and pre_candidates_state == post_candidates_state:
                break
        print(repr(self._puzzle))


#
# def main(argv):
#
#     # Very Hard --> requires search
#     # grid_string = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
#
#     # grid_string = '1...895..5....7819........72.4..8.7.9.71.54.8.8.7..3.531.4..78.4682....3..985...1'
#     # grid_string = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
#     # grid_string = '.82...59....8.1..3..52...78...37842...........27945...91...68..2..7.9....73...95.'
#     # grid_string = '437...189.6.183.......9.536.73..1...9..4.7..1...5..69.124.7.......645.1.356...974'
#
#     # grid_string = '.6..7.4..5......12...1....7..5.4.27..3.....4..19.6.8...4...1...79.6....8..1.3..2.'
#     # solution    = '163275489578496312924183567685349271237518946419762853346821795792654138851937624'
#
#     # grid_string = '7.9..3.85812..6.375.478..1.3.196..5.426..789...52..6.1143.7.56....3..1.8......3..'
#     # solution    = '769123485812456937534789216381964752426517893975238641143872569697345128258691374'
#
#     #grid_string = '31.....78526.9.13.8..6.359228.4.9..1..3.862..6..1.5..3...2.13467.1...8...6...891.'
#     # solution    = '319542678526897134874613592285439761143786259697125483958271346731964825462358917'
#
#     # grid_string = '.1869.....5....71..7..3..62.21863...7..5...365...419.88...72.4..47.18.9.....563..'
#     # solution = '218697453356284719479135862921863574784529136563741928835972641647318295192456387'
#
#     # grid_string = '...12.4.5.4.6..7.8.26......47.5...31.........31...8..9.8..1.......2..5.4..24.79.6'
#     # solution =  '837129465941653728526874193478592631269341857315768249684915372793286514152437986'
#
#     # grid_string = '.5...478...67.95..2.7.5.1.3.2.....6..981.543..3.....7.1.5..7..8..35.26.7.728...5.'
#     # solution =  '359214786816739524247658193721483965698175432534926871165397248983542617472861359'
#
#     # hard puzzle (X wings and requires 5 full iterations to be solved)
#     # grid_string = '4.......1..6.35.24..984.6.7.3....4..9..68.3.5.1..7.2....542.7.32.....54.......1.2'
#     # solution = '423796851786135924159842637538219476972684315614573289865421793291367548347958162'
# #
# #
#     grid2 = make_grid_from_string(grid_string)
#     grid2.parse_grid_candidates()
# #     print(grid2)
# #     print(grid2.print_puzzle())
#     solver = PuzzleSolver(grid2.clone())
#     assert grid2.is_valid()
#     solver.solve()
# #
# #     for idx in range(10):
# #         print('step = ', idx, '\n')
# #
# #         solver.eliminate_candidates()
# #         assert solver._puzzle.is_valid()
# #         solver.propagate()
# #         assert solver._puzzle.is_valid()
# #         solver.fill_singles()
# #         assert solver._puzzle.is_valid()
# #         print(solver._puzzle)
# #         print(solver._puzzle.print_puzzle())
# #     print(repr(solver._puzzle))
# #
# #
# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
