# -*- coding: utf-8 -*-
"""
boardkeys_unit_tests.py

Tests that the base infrastructure of keys and addresses on a board is good

Created on Mon May 30 17:01:26 2016

@author: fredericdupont
"""

import unittest
from boardkeys import Board


class Test_Board(unittest.TestCase):


    def setUp(self):
        """
        Boards of size=9: board1, board2
        """
        self.board1 = Board()
        self.board2 = Board(9)
        self.square_reference = ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai', \
                                 'Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi', \
                                 'Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci', \
                                 'Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di', \
                                 'Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei', \
                                 'Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi', \
                                 'Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi', \
                                 'Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi', \
                                 'Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii']

    def test_an_object_Board_is_created(self):
        board_1 = Board()
        self.assertIsInstance(board_1, Board)
        board_2 = Board(9)
        self.assertIsInstance(board_2, Board)
        self.assertIsInstance(self.board1, Board)
        self.assertIsInstance(self.board2, Board)

    def test_ROWS(self):
        """do ROWS contain the proper values
        """
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.assertEqual(self.board1._rows, rows)
        self.assertEqual(self.board2._rows, rows)

    def test_COLS(self):
        """do COLS contain the proper values
        """
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.assertEqual(self.board1._cols, cols)
        self.assertEqual(self.board1._cols, cols)

    def test_SQUARES(self):
        """do SQUARES contain the proper values
        """
        self.assertEqual(self.board1._squares, self.square_reference)
        self.assertEqual(self.board1._squares, self.square_reference)

    def test_UNITS(self):
        """do UNITS contain the proper values
        """
        units = {'Hd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ge': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ci': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Bg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Ga': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'If': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ch': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Fa': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Bf': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Bd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Db': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Cb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ib': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Eb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Cc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ec': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Dc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Gg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Gf': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Dh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Be': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'De': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Ie': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Hf': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ha': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Cd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Cg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Hh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Fi': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Gd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ah': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Gi': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Ad': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Ac': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ef': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Dd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Aa': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ei': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Fd': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Ai': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Di': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Fh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Ii': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Bh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Gc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Gb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Fg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Hb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Hc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Da': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Bb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Df': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Ic': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Ba': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ce': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Ag': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Cf': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Ed': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Fc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Eg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Ab': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Bc': [['Ac', 'Bc', 'Cc', 'Dc', 'Ec', 'Fc', 'Gc', 'Hc', 'Ic'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Ig': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Id': [['Ad', 'Bd', 'Cd', 'Dd', 'Ed', 'Fd', 'Gd', 'Hd', 'Id'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Ih': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Ff': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Fe': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Ca': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ca', 'Cb', 'Cc', 'Cd', 'Ce', 'Cf', 'Cg', 'Ch', 'Ci'], ['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']],\
                 'Eh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Ee': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Dd', 'De', 'Df', 'Ed', 'Ee', 'Ef', 'Fd', 'Fe', 'Ff']],\
                 'Bi': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ba', 'Bb', 'Bc', 'Bd', 'Be', 'Bf', 'Bg', 'Bh', 'Bi'], ['Ag', 'Ah', 'Ai', 'Bg', 'Bh', 'Bi', 'Cg', 'Ch', 'Ci']],\
                 'Af': [['Af', 'Bf', 'Cf', 'Df', 'Ef', 'Ff', 'Gf', 'Hf', 'If'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']],\
                 'Dg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Da', 'Db', 'Dc', 'Dd', 'De', 'Df', 'Dg', 'Dh', 'Di'], ['Dg', 'Dh', 'Di', 'Eg', 'Eh', 'Ei', 'Fg', 'Fh', 'Fi']],\
                 'Gh': [['Ah', 'Bh', 'Ch', 'Dh', 'Eh', 'Fh', 'Gh', 'Hh', 'Ih'], ['Ga', 'Gb', 'Gc', 'Gd', 'Ge', 'Gf', 'Gg', 'Gh', 'Gi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Ea': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ea', 'Eb', 'Ec', 'Ed', 'Ee', 'Ef', 'Eg', 'Eh', 'Ei'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'He': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gd', 'Ge', 'Gf', 'Hd', 'He', 'Hf', 'Id', 'Ie', 'If']],\
                 'Hi': [['Ai', 'Bi', 'Ci', 'Di', 'Ei', 'Fi', 'Gi', 'Hi', 'Ii'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Fb': [['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Hb', 'Ib'], ['Fa', 'Fb', 'Fc', 'Fd', 'Fe', 'Ff', 'Fg', 'Fh', 'Fi'], ['Da', 'Db', 'Dc', 'Ea', 'Eb', 'Ec', 'Fa', 'Fb', 'Fc']],\
                 'Ia': [['Aa', 'Ba', 'Ca', 'Da', 'Ea', 'Fa', 'Ga', 'Ha', 'Ia'], ['Ia', 'Ib', 'Ic', 'Id', 'Ie', 'If', 'Ig', 'Ih', 'Ii'], ['Ga', 'Gb', 'Gc', 'Ha', 'Hb', 'Hc', 'Ia', 'Ib', 'Ic']],\
                 'Hg': [['Ag', 'Bg', 'Cg', 'Dg', 'Eg', 'Fg', 'Gg', 'Hg', 'Ig'], ['Ha', 'Hb', 'Hc', 'Hd', 'He', 'Hf', 'Hg', 'Hh', 'Hi'], ['Gg', 'Gh', 'Gi', 'Hg', 'Hh', 'Hi', 'Ig', 'Ih', 'Ii']],\
                 'Ae': [['Ae', 'Be', 'Ce', 'De', 'Ee', 'Fe', 'Ge', 'He', 'Ie'], ['Aa', 'Ab', 'Ac', 'Ad', 'Ae', 'Af', 'Ag', 'Ah', 'Ai'], ['Ad', 'Ae', 'Af', 'Bd', 'Be', 'Bf', 'Cd', 'Ce', 'Cf']]}

        for key in self.square_reference:
            self.assertEqual(self.board1._units[key], units[key])
            self.assertEqual(self.board2._units[key], units[key])
        key_set_reference = set(self.square_reference)
        key_set = set(self.board1._units.keys())
        self.assertEqual(key_set, key_set_reference)
        key_set = set(self.board2._units.keys())
        self.assertEqual(key_set, key_set_reference)

    def test_PEERS(self):
        """do PEERS contain the proper values
        """
        peers = {'Hd': {'If', 'Ge', 'Id', 'Hb', 'He', 'Hi', 'Hc', 'Gf', 'Hf', 'Ed', 'Ie', 'Cd', 'Ha', 'Gd', 'Hh', 'Ad', 'Bd', 'Dd', 'Hg', 'Fd'},\
                 'Ge': {'If', 'Hd', 'Be', 'Gc', 'Ga', 'Gb', 'Id', 'He', 'Ce', 'Gf', 'Hf', 'Fe', 'De', 'Ie', 'Gd', 'Ee', 'Gi', 'Gg', 'Gh', 'Ae'},\
                 'Ci': {'Di', 'Ii', 'Bh', 'Bg', 'Ch', 'Ca', 'Hi', 'Cc', 'Ce', 'Ag', 'Cf', 'Ei', 'Cd', 'Cg', 'Fi', 'Cb', 'Ah', 'Bi', 'Gi', 'Ai'},\
                 'Bg': {'Be', 'Bh', 'Ci', 'Fg', 'Ch', 'Bf', 'Bb', 'Ba', 'Ag', 'Eg', 'Bc', 'Cg', 'Ig', 'Ah', 'Bi', 'Gg', 'Bd', 'Dg', 'Hg', 'Ai'},\
                 'Ga': {'Ge', 'Gc', 'Gb', 'Hb', 'Da', 'Ca', 'Ic', 'Ba', 'Ia', 'Gf', 'Hc', 'Ib', 'Ha', 'Gd', 'Fa', 'Gi', 'Gg', 'Gh', 'Ea', 'Aa'},\
                 'If': {'Hd', 'Ge', 'Ii', 'Id', 'Bf', 'Df', 'Ic', 'He', 'Gf', 'Ia', 'Ib', 'Ih', 'Cf', 'Hf', 'Ie', 'Ig', 'Gd', 'Ff', 'Af', 'Ef'},\
                 'Ch': {'Bh', 'Ci', 'Bg', 'Ca', 'Cc', 'Ce', 'Ih', 'Ag', 'Cf', 'Dh', 'Fh', 'Cd', 'Cg', 'Ah', 'Hh', 'Eh', 'Cb', 'Bi', 'Gh', 'Ai'},\
                 'Fa': {'Ga', 'Fg', 'Db', 'Da', 'Ca', 'Eb', 'Ba', 'Ia', 'Ec', 'Dc', 'Fe', 'Fh', 'Ha', 'Fi', 'Ff', 'Ea', 'Aa', 'Fb', 'Fc', 'Fd'},\
                 'Bf': {'If', 'Be', 'Bh', 'Bg', 'Bb', 'Df', 'Ba', 'Gf', 'Ce', 'Cf', 'Hf', 'Bc', 'Cd', 'Ff', 'Bi', 'Af', 'Ad', 'Bd', 'Ef', 'Ae'},\
                 'Bd': {'Hd', 'Be', 'Bh', 'Bg', 'Id', 'Bf', 'Bb', 'Ba', 'Ce', 'Cf', 'Ed', 'Bc', 'Cd', 'Gd', 'Bi', 'Af', 'Ad', 'Dd', 'Fd', 'Ae'},\
                 'Db': {'Di', 'Gb', 'Hb', 'Da', 'Bb', 'Eb', 'Df', 'Ec', 'Ib', 'Dc', 'Dh', 'Ab', 'De', 'Cb', 'Fa', 'Dg', 'Ea', 'Dd', 'Fc', 'Fb'},\
                 'Cb': {'Ci', 'Gb', 'Ch', 'Hb', 'Db', 'Bb', 'Eb', 'Ca', 'Cc', 'Ba', 'Ce', 'Ib', 'Cf', 'Ac', 'Ab', 'Bc', 'Cd', 'Cg', 'Aa', 'Fb'},\
                 'Ib': {'If', 'Ii', 'Gc', 'Ga', 'Gb', 'Id', 'Hb', 'Db', 'Bb', 'Eb', 'Ic', 'Ia', 'Ih', 'Hc', 'Ab', 'Ie', 'Ha', 'Ig', 'Cb', 'Fb'},\
                 'Eb': {'Gb', 'Hb', 'Db', 'Da', 'Bb', 'Ec', 'Ib', 'Dc', 'Ed', 'Eg', 'Ei', 'Ab', 'Cb', 'Fa', 'Eh', 'Ee', 'Ef', 'Ea', 'Fc', 'Fb'},\
                 'Cc': {'Ci', 'Gc', 'Ch', 'Bb', 'Ca', 'Ic', 'Ba', 'Ec', 'Hc', 'Dc', 'Ce', 'Cf', 'Ac', 'Ab', 'Bc', 'Cd', 'Cg', 'Cb', 'Fc', 'Aa'},\
                 'Ec': {'Gc', 'Db', 'Da', 'Eb', 'Cc', 'Ic', 'Hc', 'Dc', 'Ed', 'Ac', 'Ei', 'Bc', 'Eg', 'Fa', 'Eh', 'Ee', 'Ef', 'Ea', 'Fc', 'Fb'},\
                 'Dc': {'Di', 'Gc', 'Db', 'Da', 'Df', 'Eb', 'Cc', 'Ic', 'Ec', 'Hc', 'Ac', 'Dh', 'Bc', 'De', 'Fa', 'Dg', 'Ea', 'Dd', 'Fc', 'Fb'},\
                 'Gg': {'Ge', 'Ii', 'Gc', 'Bg', 'Ga', 'Gb', 'Fg', 'Hi', 'Gf', 'Ag', 'Ih', 'Eg', 'Cg', 'Ig', 'Gd', 'Hh', 'Gi', 'Dg', 'Gh', 'Hg'},\
                 'Gf': {'If', 'Hd', 'Ge', 'Gc', 'Ga', 'Gb', 'Id', 'Bf', 'Df', 'He', 'Cf', 'Hf', 'Ie', 'Gd', 'Ff', 'Gi', 'Af', 'Gg', 'Ef', 'Gh'},\
                 'Dh': {'Di', 'Bh', 'Ch', 'Fg', 'Db', 'Da', 'Df', 'Ih', 'Dc', 'Ei', 'Fh', 'De', 'Eg', 'Fi', 'Ah', 'Hh', 'Eh', 'Dg', 'Gh', 'Dd'},\
                 'Be': {'Ge', 'Bh', 'Bg', 'Bf', 'Bb', 'He', 'Ba', 'Ce', 'Cf', 'Fe', 'De', 'Ie', 'Bc', 'Cd', 'Ee', 'Bi', 'Af', 'Ad', 'Bd', 'Ae'},\
                 'De': {'Di', 'Ge', 'Be', 'Db', 'Da', 'Df', 'He', 'Ce', 'Dc', 'Ed', 'Dh', 'Fe', 'Ie', 'Ff', 'Ee', 'Dg', 'Ef', 'Dd', 'Fd', 'Ae'},\
                 'Ie': {'If', 'Hd', 'Ge', 'Ii', 'Be', 'Id', 'He', 'Ic', 'Ce', 'Ia', 'Ib', 'Ih', 'Gf', 'Hf', 'Fe', 'De', 'Ig', 'Gd', 'Ee', 'Ae'},\
                 'Hf': {'If', 'Hd', 'Ge', 'Id', 'Hb', 'Bf', 'Df', 'He', 'Hi', 'Gf', 'Hc', 'Cf', 'Ie', 'Ha', 'Gd', 'Ff', 'Hh', 'Af', 'Ef', 'Hg'},\
                 'Ha': {'Hd', 'Gc', 'Ga', 'Gb', 'Hb', 'Da', 'Ca', 'He', 'Ba', 'Hi', 'Ia', 'Hc', 'Ib', 'Ic', 'Hf', 'Fa', 'Hh', 'Ea', 'Hg', 'Aa'},\
                 'Cd': {'Hd', 'Ci', 'Be', 'Id', 'Ch', 'Bf', 'Ca', 'Cc', 'Ce', 'Cf', 'Ed', 'Cg', 'Gd', 'Cb', 'Af', 'Ad', 'Bd', 'Dd', 'Fd', 'Ae'},\
                 'Cg': {'Ci', 'Bh', 'Bg', 'Fg', 'Ch', 'Ca', 'Cc', 'Ce', 'Ag', 'Cf', 'Eg', 'Cd', 'Ig', 'Cb', 'Ah', 'Bi', 'Gg', 'Dg', 'Hg', 'Ai'},\
                 'Hh': {'Hd', 'Ii', 'Bh', 'Ch', 'Hb', 'He', 'Hi', 'Hc', 'Ih', 'Hf', 'Dh', 'Fh', 'Ha', 'Ig', 'Ah', 'Eh', 'Gi', 'Gg', 'Gh', 'Hg'},\
                 'Fi': {'Di', 'Ii', 'Ci', 'Fg', 'Hi', 'Dh', 'Eg', 'Fh', 'Fe', 'Ei', 'Ff', 'Fa', 'Eh', 'Bi', 'Gi', 'Dg', 'Fc', 'Fb', 'Fd', 'Ai'},\
                 'Gd': {'If', 'Hd', 'Ge', 'Gc', 'Ga', 'Gb', 'Id', 'He', 'Gf', 'Hf', 'Ed', 'Ie', 'Cd', 'Gi', 'Ad', 'Bd', 'Gg', 'Gh', 'Dd', 'Fd'},\
                 'Ah': {'Ai', 'Bh', 'Ci', 'Bg', 'Ch', 'Ih', 'Ag', 'Ac', 'Dh', 'Fh', 'Ab', 'Cg', 'Hh', 'Eh', 'Bi', 'Af', 'Ad', 'Gh', 'Aa', 'Ae'},\
                 'Gi': {'Di', 'Ge', 'Ii', 'Ci', 'Gc', 'Ga', 'Gb', 'Hi', 'Gf', 'Ih', 'Ei', 'Ig', 'Fi', 'Gd', 'Hh', 'Bi', 'Gg', 'Gh', 'Hg', 'Ai'},\
                 'Ad': {'Ai', 'Hd', 'Be', 'Id', 'Bf', 'Ce', 'Ag', 'Cf', 'Ed', 'Ac', 'Ab', 'Cd', 'Gd', 'Ah', 'Af', 'Bd', 'Dd', 'Aa', 'Fd', 'Ae'},\
                 'Ac': {'Ai', 'Gc', 'Bb', 'Ca', 'Cc', 'Ic', 'Ba', 'Ec', 'Hc', 'Dc', 'Ag', 'Ab', 'Bc', 'Ah', 'Cb', 'Af', 'Ad', 'Fc', 'Aa', 'Ae'},\
                 'Ef': {'If', 'Bf', 'Df', 'Eb', 'Gf', 'Ec', 'Cf', 'Hf', 'Ed', 'Fe', 'Eg', 'De', 'Ei', 'Ff', 'Eh', 'Ee', 'Af', 'Ea', 'Dd', 'Fd'},\
                 'Dd': {'Di', 'Hd', 'Id', 'Db', 'Da', 'Df', 'Dc', 'Ed', 'Dh', 'Fe', 'De', 'Cd', 'Gd', 'Ff', 'Ee', 'Ad', 'Bd', 'Dg', 'Ef', 'Fd'},\
                 'Aa': {'Ai', 'Ga', 'Da', 'Bb', 'Ca', 'Cc', 'Ba', 'Ia', 'Ag', 'Ac', 'Ab', 'Bc', 'Ha', 'Fa', 'Ah', 'Cb', 'Af', 'Ad', 'Ea', 'Ae'},\
                 'Ei': {'Di', 'Ii', 'Ci', 'Fg', 'Eb', 'Hi', 'Ec', 'Ed', 'Dh', 'Eg', 'Fh', 'Fi', 'Eh', 'Ee', 'Bi', 'Gi', 'Ef', 'Dg', 'Ea', 'Ai'},\
                 'Fd': {'Hd', 'Id', 'Fg', 'Df', 'Ed', 'Fe', 'Fh', 'De', 'Cd', 'Fi', 'Gd', 'Ff', 'Fa', 'Ee', 'Ad', 'Bd', 'Ef', 'Dd', 'Fc', 'Fb'},\
                 'Ai': {'Di', 'Ae', 'Ii', 'Ci', 'Bh', 'Bg', 'Ch', 'Hi', 'Ag', 'Ac', 'Ab', 'Ei', 'Cg', 'Fi', 'Ah', 'Bi', 'Gi', 'Af', 'Ad', 'Aa'},\
                 'Di': {'Ii', 'Ci', 'Fg', 'Db', 'Da', 'Df', 'Hi', 'Dc', 'Eg', 'Dh', 'De', 'Fh', 'Ei', 'Fi', 'Eh', 'Bi', 'Gi', 'Dg', 'Dd', 'Ai'},\
                 'Fh': {'Di', 'Bh', 'Ch', 'Fg', 'Ih', 'Eg', 'Ei', 'Dh', 'Fe', 'Fi', 'Ff', 'Ah', 'Hh', 'Eh', 'Fa', 'Dg', 'Gh', 'Fc', 'Fb', 'Fd'},\
                 'Ii': {'Di', 'If', 'Ci', 'Id', 'Hi', 'Ic', 'Ia', 'Ib', 'Ih', 'Ei', 'Ie', 'Ig', 'Fi', 'Hh', 'Bi', 'Gi', 'Gg', 'Gh', 'Hg', 'Ai'},\
                 'Bh': {'Be', 'Bg', 'Ci', 'Ch', 'Bf', 'Bb', 'Ba', 'Ih', 'Ag', 'Dh', 'Fh', 'Bc', 'Cg', 'Ah', 'Hh', 'Eh', 'Bi', 'Bd', 'Gh', 'Ai'},\
                 'Gc': {'Ge', 'Ga', 'Gb', 'Hb', 'Cc', 'Ic', 'Ec', 'Hc', 'Dc', 'Gf', 'Ia', 'Ib', 'Ac', 'Bc', 'Ha', 'Gd', 'Gi', 'Gg', 'Gh', 'Fc'},\
                 'Gb': {'Ge', 'Gc', 'Ga', 'Hb', 'Db', 'Bb', 'Eb', 'Ic', 'Gf', 'Ib', 'Hc', 'Ia', 'Ab', 'Ha', 'Gd', 'Cb', 'Gi', 'Gg', 'Gh', 'Fb'},\
                 'Fg': {'Di', 'Bg', 'Ag', 'Dh', 'Ei', 'Fh', 'Eg', 'Fe', 'Cg', 'Ig', 'Fi', 'Ff', 'Fa', 'Eh', 'Gg', 'Dg', 'Hg', 'Fc', 'Fb', 'Fd'},\
                 'Hb': {'Hd', 'Gc', 'Ga', 'Gb', 'Db', 'Bb', 'Eb', 'He', 'Hi', 'Ic', 'Hc', 'Ib', 'Ia', 'Hf', 'Ab', 'Ha', 'Cb', 'Hh', 'Hg', 'Fb'},\
                 'Hc': {'Hd', 'Gc', 'Ga', 'Gb', 'Hb', 'Cc', 'Ic', 'He', 'Ec', 'Ib', 'Dc', 'Hf', 'Hi', 'Ia', 'Ac', 'Bc', 'Ha', 'Hh', 'Hg', 'Fc'},\
                 'Da': {'Di', 'Ga', 'Db', 'Ca', 'Df', 'Eb', 'Ba', 'Ia', 'Ec', 'Dc', 'Dh', 'De', 'Ha', 'Fa', 'Dg', 'Ea', 'Dd', 'Aa', 'Fb', 'Fc'},\
                 'Bb': {'Be', 'Bh', 'Bg', 'Gb', 'Hb', 'Bf', 'Db', 'Eb', 'Ca', 'Cc', 'Ba', 'Ib', 'Ac', 'Ab', 'Bc', 'Cb', 'Bi', 'Bd', 'Aa', 'Fb'},\
                 'Df': {'Di', 'If', 'Bf', 'Db', 'Da', 'Gf', 'Dc', 'Cf', 'Hf', 'Ed', 'Fe', 'Dh', 'De', 'Ff', 'Ee', 'Af', 'Ef', 'Dg', 'Dd', 'Fd'},\
                 'Ic': {'If', 'Ii', 'Gc', 'Ga', 'Gb', 'Id', 'Hb', 'Cc', 'Ec', 'Hc', 'Dc', 'Ia', 'Ib', 'Ih', 'Ac', 'Bc', 'Ie', 'Ha', 'Ig', 'Fc'},\
                 'Ba': {'Be', 'Bh', 'Bg', 'Ga', 'Bf', 'Da', 'Bb', 'Ca', 'Cc', 'Ia', 'Ac', 'Ab', 'Bc', 'Ha', 'Fa', 'Cb', 'Bi', 'Bd', 'Ea', 'Aa'},\
                 'Ce': {'Ge', 'Be', 'Ci', 'Ch', 'Bf', 'Ca', 'He', 'Cc', 'Cf', 'Fe', 'De', 'Ie', 'Cd', 'Cg', 'Cb', 'Ee', 'Af', 'Ad', 'Bd', 'Ae'},\
                 'Ag': {'Ai', 'Bh', 'Ci', 'Bg', 'Fg', 'Ch', 'Ac', 'Eg', 'Ab', 'Cg', 'Ig', 'Ah', 'Bi', 'Af', 'Gg', 'Ad', 'Dg', 'Hg', 'Aa', 'Ae'},\
                 'Cf': {'If', 'Ci', 'Be', 'Ch', 'Bf', 'Df', 'Ca', 'Cc', 'Gf', 'Ce', 'Hf', 'Cd', 'Cg', 'Ff', 'Cb', 'Af', 'Ad', 'Bd', 'Ef', 'Ae'},\
                 'Ed': {'Hd', 'Id', 'Eb', 'Df', 'Ec', 'Fe', 'Eg', 'De', 'Ei', 'Cd', 'Gd', 'Ff', 'Eh', 'Ee', 'Ad', 'Bd', 'Ef', 'Ea', 'Dd', 'Fd'},\
                 'Fc': {'Gc', 'Fg', 'Db', 'Da', 'Eb', 'Cc', 'Ic', 'Ec', 'Hc', 'Dc', 'Ac', 'Fe', 'Bc', 'Fh', 'Fi', 'Ff', 'Fa', 'Ea', 'Fb', 'Fd'},\
                 'Eg': {'Di', 'Bg', 'Fg', 'Eb', 'Ec', 'Ag', 'Ed', 'Dh', 'Fh', 'Ei', 'Cg', 'Ig', 'Fi', 'Eh', 'Ee', 'Gg', 'Dg', 'Ef', 'Ea', 'Hg'},\
                 'Ab': {'Ai', 'Gb', 'Hb', 'Db', 'Bb', 'Eb', 'Ca', 'Cc', 'Ba', 'Ib', 'Ag', 'Ac', 'Bc', 'Cb', 'Ah', 'Af', 'Ad', 'Aa', 'Fb', 'Ae'},\
                 'Bc': {'Be', 'Gc', 'Bg', 'Bh', 'Bf', 'Bb', 'Ca', 'Cc', 'Ic', 'Ba', 'Ec', 'Hc', 'Dc', 'Ac', 'Ab', 'Cb', 'Bi', 'Bd', 'Fc', 'Aa'},\
                 'Ig': {'If', 'Ii', 'Bg', 'Fg', 'Id', 'Ic', 'Hi', 'Ia', 'Ag', 'Ib', 'Ih', 'Eg', 'Ie', 'Cg', 'Hh', 'Gi', 'Gg', 'Dg', 'Gh', 'Hg'},\
                 'Id': {'If', 'Hd', 'Ge', 'Ii', 'He', 'Ic', 'Ia', 'Ib', 'Ih', 'Gf', 'Hf', 'Ed', 'Ie', 'Cd', 'Ig', 'Gd', 'Ad', 'Bd', 'Dd', 'Fd'},\
                 'Ih': {'If', 'Ii', 'Bh', 'Ch', 'Id', 'Ic', 'Hi', 'Ia', 'Ib', 'Dh', 'Fh', 'Ie', 'Ig', 'Ah', 'Hh', 'Eh', 'Gi', 'Gg', 'Gh', 'Hg'},\
                 'Ff': {'If', 'Fg', 'Bf', 'Df', 'Gf', 'Cf', 'Ed', 'Hf', 'Fe', 'Fh', 'De', 'Fi', 'Fa', 'Ee', 'Af', 'Ef', 'Dd', 'Fc', 'Fb', 'Fd'},\
                 'Fe': {'Ge', 'Be', 'Fg', 'Df', 'He', 'Ce', 'Ed', 'De', 'Ie', 'Fh', 'Fi', 'Ff', 'Fa', 'Ee', 'Ef', 'Dd', 'Fc', 'Fb', 'Fd', 'Ae'},\
                 'Ca': {'Ci', 'Ga', 'Ch', 'Da', 'Bb', 'Cc', 'Ba', 'Ia', 'Ce', 'Cf', 'Ac', 'Ab', 'Bc', 'Ha', 'Cd', 'Cg', 'Fa', 'Cb', 'Ea', 'Aa'},\
                 'Eh': {'Di', 'Bh', 'Ch', 'Fg', 'Eb', 'Ec', 'Ih', 'Ed', 'Dh', 'Ei', 'Fh', 'Eg', 'Fi', 'Ah', 'Hh', 'Ee', 'Ef', 'Gh', 'Ea', 'Dg'},\
                 'Ee': {'Ge', 'Be', 'Eb', 'Df', 'He', 'Ce', 'Ec', 'Ed', 'Eg', 'Ei', 'De', 'Ie', 'Fe', 'Ff', 'Eh', 'Ef', 'Ea', 'Dd', 'Fd', 'Ae'},\
                 'Bi': {'Di', 'Ii', 'Ci', 'Be', 'Bg', 'Bh', 'Ch', 'Bf', 'Bb', 'Hi', 'Ba', 'Ag', 'Ei', 'Bc', 'Cg', 'Fi', 'Ah', 'Gi', 'Bd', 'Ai'},\
                 'Af': {'Ai', 'If', 'Be', 'Bf', 'Df', 'Gf', 'Ag', 'Ce', 'Cf', 'Hf', 'Ac', 'Ab', 'Cd', 'Ff', 'Ah', 'Ad', 'Bd', 'Ef', 'Aa', 'Ae'},\
                 'Dg': {'Di', 'Bg', 'Fg', 'Db', 'Da', 'Df', 'Ag', 'Dc', 'Eg', 'Ei', 'De', 'Fh', 'Dh', 'Cg', 'Ig', 'Fi', 'Eh', 'Gg', 'Hg', 'Dd'},\
                 'Gh': {'Ge', 'Ii', 'Bh', 'Gc', 'Ga', 'Gb', 'Ch', 'Hi', 'Gf', 'Ih', 'Dh', 'Fh', 'Ig', 'Gd', 'Ah', 'Hh', 'Eh', 'Gi', 'Gg', 'Hg'},\
                 'Ea': {'Ga', 'Db', 'Da', 'Ca', 'Eb', 'Ba', 'Ia', 'Ec', 'Dc', 'Ed', 'Eg', 'Ei', 'Ha', 'Fa', 'Eh', 'Ee', 'Ef', 'Fc', 'Aa', 'Fb'},\
                 'He': {'If', 'Hd', 'Ge', 'Be', 'Id', 'Hb', 'Hi', 'Ce', 'Hc', 'Gf', 'Hf', 'Fe', 'De', 'Ie', 'Ha', 'Gd', 'Hh', 'Ee', 'Hg', 'Ae'},\
                 'Hi': {'Di', 'Hd', 'Ii', 'Ci', 'Hb', 'He', 'Hc', 'Ih', 'Hf', 'Ei', 'Ha', 'Ig', 'Fi', 'Hh', 'Bi', 'Gi', 'Gg', 'Gh', 'Hg', 'Ai'},\
                 'Fb': {'Gb', 'Fg', 'Hb', 'Db', 'Da', 'Bb', 'Eb', 'Ec', 'Ib', 'Dc', 'Fe', 'Ab', 'Fh', 'Fi', 'Ff', 'Cb', 'Fa', 'Ea', 'Fc', 'Fd'},\
                 'Ia': {'If', 'Ii', 'Gc', 'Ga', 'Gb', 'Id', 'Hb', 'Da', 'Ca', 'Ic', 'Ba', 'Ib', 'Ih', 'Hc', 'Ie', 'Ha', 'Ig', 'Fa', 'Ea', 'Aa'},\
                 'Hg': {'Hd', 'Ii', 'Bg', 'Fg', 'Hb', 'He', 'Hi', 'Hc', 'Ag', 'Ih', 'Hf', 'Eg', 'Ha', 'Cg', 'Ig', 'Hh', 'Gi', 'Gg', 'Dg', 'Gh'},\
                 'Ae': {'Ge', 'Be', 'Bf', 'He', 'Ce', 'Ag', 'Cf', 'Ac', 'Ab', 'De', 'Ie', 'Fe', 'Cd', 'Ah', 'Ee', 'Af', 'Ad', 'Bd', 'Aa', 'Ai'}}
        for key in self.square_reference:
            self.assertEqual(self.board1._peers[key], peers[key])
            self.assertEqual(self.board2._peers[key], peers[key])
        key_set_reference = set(self.square_reference)
        key_set = set(self.board1._peers.keys())
        self.assertEqual(key_set, key_set_reference)
        key_set = set(self.board2._peers.keys())
        self.assertEqual(key_set, key_set_reference)

    def testprinted_output(self):
        """
        compares the printed output to a reference string
        """
        reference_string = """   a  b  c    d  e  f    g  h  i  \n\
A  Aa Ab Ac | Ad Ae Af | Ag Ah Ai \n\
B  Ba Bb Bc | Bd Be Bf | Bg Bh Bi \n\
C  Ca Cb Cc | Cd Ce Cf | Cg Ch Ci \n\
   ---------+----------+--------- \n\
D  Da Db Dc | Dd De Df | Dg Dh Di \n\
E  Ea Eb Ec | Ed Ee Ef | Eg Eh Ei \n\
F  Fa Fb Fc | Fd Fe Ff | Fg Fh Fi \n\
   ---------+----------+--------- \n\
G  Ga Gb Gc | Gd Ge Gf | Gg Gh Gi \n\
H  Ha Hb Hc | Hd He Hf | Hg Hh Hi \n\
I  Ia Ib Ic | Id Ie If | Ig Ih Ii \n\n"""
        result = self.board1.output(self.board1._squares)
        self.assertEqual(result, reference_string)

#    def test_various_board_sizes(self):
#        """Not implemented - must revert to a 9x9 board
#        """
#        board = Board(16)
#        self.assertIsInstance(board, Board)


if __name__ == '__main__':
    unittest.main()
