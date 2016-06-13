# -*- coding: utf-8 -*-
"""
sdksolver.py
sudoku solver
Created on Wed Jun  1 15:27:23 2016

@author: fredericdupont
"""

# # Constants used
# SQUARES --> an ordered list of every square_key used to access UNITS, PEERS
# UNITS   --> a dictionary containing the access keys for the rows, cols & boxes
#             of a square {'square_key' : [[square_keys for row],
#                                          [square_keys for col],
#                                          [square_keys for box]]}
# PEERS   --> a dictionary containing the access keys for the peers
#             {'square_key': [peers]}
# DIGITS  --> legal values for a solved square '123456789'

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

    def is_valid_grid(self) -> bool:
        """
        verifies if a grid is valid
        --> proper size -> all squares have a value assigned
                        -> no extra entries
        --> all values assigned to squares are legal <=> are in DIGITS or '0.'
        --> unique values in rows / columns / boxes

        :return: True if is valid, False otherwise
        """
        result = True
        result &= self._contains_all_keys()
        for square in SQUARES:
            pass
        return result

    def _contains_all_keys(self) -> bool:
        """
        checks if self._grid.keys() contains the proper keys
        :return: True if self_grid contains all keys and not more, False otherwise
        """
        temp = sorted(list(self._grid.keys()))
        return temp == SQUARES and len(temp) == len(SQUARES)





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
# @TODO: make a grid of values

if __name__ == '__main__':

    grid = make_grid_from_string(''.join(['.'] * 81))
    print(grid)
    grid.is_valid_grid()
    grid = make_grid_from_string(''.join(['123456789'] * 9))
    print(grid)
