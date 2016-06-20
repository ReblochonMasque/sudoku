# -*- coding: utf-8 -*-
"""
puzzleconstants.py
Sudoku board representation - keys and addresses
Created on Mon May 30 17:00:20 2016
@author: fredericdupont
"""

import math


class _PuzzleConstants(object):
    """
    represents a sudoku board with rows in CAPITAL and cols in lower case, and
    provides the data structures and access keys to manipulate it
        for a 9x9 board:
            --> rows are A to I
            --> cols are a to i

    _PuzzleConstants repr:
       a  b  c    d  e  f    g  h  i
    A  Aa Ab Ac | Ad Ae Af | Ag Ah Ai
    B  Ba Bb Bc | Bd Be Bf | Bg Bh Bi
    C  Ca Cb Cc | Cd Ce Cf | Cg Ch Ci
       ---------+----------+---------
    D  Da Db Dc | Dd De Df | Dg Dh Di
    E  Ea Eb Ec | Ed Ee Ef | Eg Eh Ei
    F  Fa Fb Fc | Fd Fe Ff | Fg Fh Fi
       ---------+----------+---------
    G  Ga Gb Gc | Gd Ge Gf | Gg Gh Gi
    H  Ha Hb Hc | Hd He Hf | Hg Hh Hi
    I  Ia Ib Ic | Id Ie If | Ig Ih Ii


    Units are the lists of squares representing the ROW, COL and BOX of a SQUARE
    Units of Ce (3 lists of 9 = 27)
                   ROW                             BOX                             COL
       a  b  c    d  e  f    g  h  i   a  b  c    d  e  f    g  h  i   a  b  c    d  e  f    g  h  i
    A           |          |                    | Ad Ae Af |                    |    Ae    |
    B           |          |                    | Bd Be Bf |                    |    Be    |
    C  Ca Cb Cc | Cd Ce Cf | Cg Ch Ci           | Cd Ce Cf |                    |    Ce    |
       ---------+----------+---------  ---------+----------+---------  ---------+----------+--------
    D           |          |                    |          |                    |    De    |
    E           |          |                    |          |                    |    Ee    |
    F           |          |                    |          |                    |    Fe    |
       ---------+----------+---------  ---------+----------+---------  ---------+----------+--------
    G           |          |                    |          |                    |    Ge    |
    H           |          |                    |          |                    |    He    |
    I           |          |                    |          |                    |    Ie    |

    Peers are the set of squares sharing the same UNIT with a SQUARE.
    Every peer must have a different value than the square in reference
    Peers of Ce (20)
       a  b  c    d  e  f    g  h  i
    A           | Ad Ae Af |
    B           | Bd Be Bf |
    C  Ca Cb Cc | Cd    Cf | Cg Ch Ci
       ---------+----------+---------
    D           |    De    |
    E           |    Ee    |
    F           |    Fe    |
       ---------+----------+---------
    G           |    Ge    |
    H           |    He    |
    I           |    Ie    |

    """

    def __init__(self, size=9):
        """
        various sizes not handled
        @todo: implement different sizes sudoku boards (16/25/36/49/64/81/100)
        @todo: REFACTOR -> why @property getters don't work?
        """
        assert size == 9
        self._size = size
        self._digits = ''.join([str(idx) for idx in range(1, 10)])
        # self._size_root = math.sqrt(self._size)
        self._rows = [chr(ord('A')+_) for _ in range(self._size)]
        self._cols = [chr(ord('a')+_) for _ in range(self._size)]
        self._squares = _PuzzleConstants._cross(self._rows, self._cols)

        self._unitlist = [_PuzzleConstants._cross(self._rows, col) for col in self._cols] + \
                         [_PuzzleConstants._cross(row, self._cols) for row in self._rows] + \
                         [_PuzzleConstants._cross(row, col) for row in ('ABC', 'DEF', 'GHI')
                          for col in ('abc', 'def', 'ghi')]

        self._units = {square: [unit for unit in self._unitlist if square in unit]
                       for square in self._squares}
        self._peers = {square: set(sum(self._units[square], [])) - {square}   # set()
                       for square in self._squares}

#        print(self._rows)
#        print(self._cols)
#        [print(square, end=' ') for square in self._squares]
#        print(self._squares)
#        [print(unit, end=' ') for unit in self._unitlist]
#        print(self._units)
#        print(self._peers)

    @property
    def digits(self):
        """getter"""
        return self._digits

    @property
    def squares(self):
        """getter"""
        return self._squares

    @property
    def units(self):
        """getter"""
        return self._units

    @property
    def peers(self):
        """getter"""
        return self._peers

    @staticmethod
    def _cross(seq_a, seq_b):
        """returns a list containing the cross products of elts in seq_a
        and elts in seq_b
        """
        return [a+b for a in seq_a for b in seq_b]

    def output(self, coll):
        """pretty prints a collection of square keys
        """
        result = ['   '] + [col + '    '
                            if not (idx + 1) % math.sqrt(self._size) and (idx + 1) % self._size
                            else col + '  '
                            for idx, col in enumerate(self._cols)] + ['\n']

        for idx, square in enumerate(self._squares):
            if square in coll:
                elt = square
            else:
                elt = '. '

            if not idx % self._size:
                result.append(self._rows[idx // self._size] + '  ')
            result.append(elt + ' ')

            if not (idx + 1) % math.sqrt(self._size) and (idx + 1) % self._size:
                result += '| '

            if not (idx + 1) % self._size:
                result.append('\n')

            if not (idx + 1) % (self._size * math.sqrt(self._size)) \
                    and idx < self._size**2 - self._size:
                result.append('   ---------+----------+--------- \n')

        result.append('\n')
        return ''.join(result)


PUZZLE_C = _PuzzleConstants()
# Constants used by other modules
SQUARES = PUZZLE_C.squares      # an ordered list of every square_key
                                # used to access UNITS, PEERS

UNITS = PUZZLE_C.units          # a dictionary containing the access keys for the rows, cols & boxes
                                # of a square {'square_key' : [[square_keys for row],
                                #                              [square_keys for col],
                                #                              [square_keys for box]]}

PEERS = PUZZLE_C.peers          # a dictionary containing the access keys for the peers
                                # {'square_key': [peers]}

DIGITS = PUZZLE_C.digits        # legal values for a solved square '123456789'


# if __name__ == '__main__':
#    pass

    # _puzzle = _PuzzleConstants()
    # print(_puzzle.output(SQUARES))
    # for squ in SQUARES[65:]:
    #     print(_puzzle.output(PEERS[squ]))
    # print(_puzzle.output(PEERS['Bd']))
