# -*- coding: utf-8 -*-
"""
sdksolver_unit_tests.py
Unit Tests for sdksolver

Created on Wed Jun  1 15:30:52 2016

@author: fredericdupont
"""

import unittest
from sdksolver import Grid, make_grid_from_string


class TestGrid(unittest.TestCase):

    def setUp(self):
        # self.grid0 = Grid()
        pass

    # @TODO: test if grid is valid

    def test_grid_instance(self):
        grid0 = Grid()
        self.assertIsInstance(grid0, Grid)

    def test_grid_instance_from_chars_linear(self):
        chars0 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        grid0_from_chars = Grid().from_string(chars0)
        self.assertIsInstance(grid0_from_chars, Grid)

    def test_grid_instance_from_chars_block(self):
        chars1 = """
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""
        grid1_from_chars = Grid().from_string(chars1)
        self.assertIsInstance(grid1_from_chars, Grid)

    def test_grid_instance_from_chars_formatted(self):
        chars2 = """
4 . . |. . . |8 . 5
. 3 . |. . . |. . .
. . . |7 . . |. . .
------+------+------
. 2 . |. . . |. 6 .
. . . |. 8 . |4 . .
. . . |. 1 . |. . .
------+------+------
. . . |6 . 3 |. 7 .
5 . . |2 . . |. . .
1 . 4 |. . . |. . .
"""
        grid2_from_chars = Grid().from_string(chars2)
        self.assertIsInstance(grid2_from_chars, Grid)

    def test_grid_instance_factory_from_string1(self):
        my_string0 = '4.... /.8.5.3..## :; ...slskfj.....7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        grid0_from_string = make_grid_from_string(my_string0)
        self.assertIsInstance(grid0_from_string, Grid)

    def test_grid_instance_factory_from_string_block(self):
        my_string1 = """
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""
        grid1_from_string = make_grid_from_string(my_string1)
        self.assertIsInstance(grid1_from_string, Grid)

    def test_grid_instance_factory_from_string_formatted(self):
        my_string2 = """
4 . . |. . . |8 . 5
. 3 . |. . . |. . .
. . . |7 . . |. . .
------+------+------
. 2 . |. . . |. 6 .
. . . |. 8 . |4 . .
. . . |. 1 . |. . .
------+------+------
. . . |6 . 3 |. 7 .
5 . . |2 . . |. . .
1 . 4 |. . . |. . .
"""
        grid2_from_string = make_grid_from_string(my_string2)
        self.assertIsInstance(grid2_from_string, Grid)

if __name__ == '__main__':
    unittest.main()
