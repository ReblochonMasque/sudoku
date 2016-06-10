# -*- coding: utf-8 -*-
"""
sdksolver.py
sudoku solver
Created on Wed Jun  1 15:27:23 2016

@author: fredericdupont
"""

from boardkeys import SQUARES, UNITS, PEERS

# @todo: move DIGITS constant to boardkeys.py
DIGITS = '123456789'


class SDKSolver(object):
    """
    A general sudoku solver
    """
    pass


class SDKGrid(object):
    """
    represents a sudoku grid
    """
    def __init__(self):
        self._grid = None


def make_grid_from_string(values):
    """
    converts a string of values into a sudoku grid dictionary {square:char}
    using a DIGIT for value and '0' or '.' for empties
    ignores everything else
    """
    chars = [char for char in values if char in DIGITS or char in '0.']
    assert len(chars) == 81
    return {key: value for key, value in zip(SQUARES, chars)}



if __name__ == '__main__':

    grid = make_grid_from_string(''.join(['.'] * 81))
    print(grid)
    grid = make_grid_from_string(''.join(['123456789'] * 9))
    print(grid)
