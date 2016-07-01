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

    def _is_solved(self):
        """
        check if the puzzle is solved
        :return: True if solved, False otherwise
        """
        return self._puzzle.is_solved()

    def _is_valid(self):
        """
        check if the puzzle is valid
        :return: True if valid, False otherwise
        """
        return self._puzzle.is_valid()


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
        solved squares until all constraints have been propagated. (no more change in the
        puzzle states)
        ...or the puzzle is solved
        :return: False if an inconsistency is discovered, True otherwise
        """
        while not self._puzzle.is_solved():
            pre_grid_state, pre_candidates_state = repr(self._puzzle), str(self._puzzle)
            if not self.eliminate_candidates():
                return False
            self.propagate()
            self.fill_singles()
            post_grid_state, post_candidates_state = repr(self._puzzle), str(self._puzzle)
            if pre_grid_state == post_grid_state and pre_candidates_state == post_candidates_state:
                break
        print(repr(self._puzzle))
        return True

    def search(self):
        """
        clones the puzzle
        creates a new solver
        assigns the next candidate value to the empty square with the less candidates
        recursively calls solve() on the new puzzle
        :return: a solved puzzle repr()
        """
        pass

    def solve(self):
        """
        manages the operations to conduct in order to solve a puzzla
        :print: the repr of a solved puzzle (as far as could go with constraint propagation)
        :return: nothing at the moment
        """
        self.eliminate_propagate_fill()

        return repr(self._puzzle)




# def main(argv):


# if __name__ == '__main__':
#     sys.exit(main(sys.argv))
