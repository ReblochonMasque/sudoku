# -*- coding: utf-8 -*-
"""
sdksolver.py
sudoku solver
Created on Wed Jun  1 15:27:23 2016

@author: fredericdupont
"""

# # Constants used
# SQUARES = _board_.squares    # an ordered list of the squares
# UNITS = _board_.units        # a dictionary with a square as key
# PEERS = _board_.peers        # a dictionary with a square as key
# DIGITS = _board_.digits      # '123456789'

from boardkeys import SQUARES, UNITS, PEERS, DIGITS


class Grid(object):
    """
    represents a sudoku grid as a dictionary of {squares: values}
    """
    def __init__(self):
        self._grid = None

    def from_string(self, chars):
        """
        :param chars: a string containing the values of a sudoku grid, in a row/col order
        :return: a sudoku grid build from the input values and checked for validity
                 but not for uniqueness of solution
        """
        self._grid = {key: value for key, value in zip(SQUARES, chars)}
        return self

def make_grid_from_string(values):
    """
    converts a string of values into a sudoku grid dictionary {square:char}
    using a DIGIT for value and '0' or '.' for empties
    ignores everything else
    """
    _grid = Grid()
    chars = [char for char in values if char in DIGITS or char in '0.']
    assert len(chars) == 81, "the grid has an incorrect size"
    return _grid.from_string(chars)

# @TODO: test validity of grid

if __name__ == '__main__':

    grid = make_grid_from_string(''.join(['.'] * 81))
    print(grid)
    grid = make_grid_from_string(''.join(['123456789'] * 9))
    print(grid)
