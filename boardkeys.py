# -*- coding: utf-8 -*-
"""
boardkeys.py
A general sudoku solver
Created on Mon May 30 17:00:20 2016
@author: fredericdupont
"""

class Board(object):
    """
    represents a sudoku board with rows in CAPITAL and cols in lower case, and
    provides the necessary data structures and access keys to manipulate it
        for a 9x9 board:
            --> rows are A to I
            --> cols are a to i

    Board repr:
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
        """
        assert size == 9
        self._size = size
        self._rows = [chr(ord('A')+_) for _ in range(self._size)]
        self._cols = [chr(ord('a')+_) for _ in range(self._size)]
        self._squares = Board._cross(self._rows, self._cols)
        self._unitlist = [Board._cross(self._rows, col) for col in self._cols] +\
                         [Board._cross(row, self._cols) for row in self._rows] +\
                         [Board._cross(row, col) for row in ('ABC', 'DEF', 'GHI')
                          for col in ('abc', 'def', 'ghi')]
        self._units = {square:[unit for unit in self._unitlist if square in unit]
                       for square in self._squares}
        self._peers = {square:set(sum(self._units[square], [])) - set([square])
                       for square in self._squares}
#        print(self._rows)
#        print(self._cols)
#        [print(square, end=' ') for square in self._squares]
#        print(self._squares)
#        [print(unit, end=' ') for unit in self._unitlist]
#        print(self._units)
#        print(self._peers)


    @staticmethod
    def _cross(seq_a, seq_b):
        """returns a list containing the cross products of elts in seq_a
        and elts in seq_b
        """
        return [a+b for a in seq_a for b in seq_b]


#class Solver(object):
#    """
#    attempts to solve a sudoku board
#    """
#    pass
#
#
#class Strategies(Solver):
#    """
#    implements various solving strategies
#    """
#    pass



if __name__ == '__main__':

    Board()
