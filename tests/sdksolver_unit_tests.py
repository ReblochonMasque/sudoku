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
        valid_grid_0_chars = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.valid_grid_0 = make_grid_from_string(valid_grid_0_chars)


    # TODO: test if grid is valid
    def test_is_valid_grid_0(self):
        """ tests is a valid grid is valid
        """
        result = self.valid_grid_0.is_valid_grid()
        self.assertTrue(result)

    # TODO: refactor with context manager?
    def test_is_invalid_grid_long_string(self):
        """ tests an invalid grid formed with a string that is either too long or too short
        """
        invalid_long_grid_chars = '1234.4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        # longer by '1234.' at the start
        result = True
        try:
            invalid_long_grid = Grid().from_string(invalid_long_grid_chars)
            result = False
        except ValueError:
            pass
        finally:
            self.assertTrue(result)

    # TODO: refactor with context manager?
    def test_is_invalid_grid_short_string(self):
        """ tests an invalid grid formed with a string that is either too long or too short
        """
        invalid_short_grid_chars = '8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        # shorter by '4.....' removed from the start
        result = True
        try:
            invalid_short_grid = Grid().from_string(invalid_short_grid_chars)
            result = False
        except ValueError:
            pass
        finally:
            self.assertTrue(result)

    def test_is_invalid_grid_illegal_chars(self):
        """ tests an invalid grid that contains illegal characters
        (must be constructed via Grid.from_string i/o factory function that checks the validity of input string)
        """
        invalid_grid_chars = 'z.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        invalid_grid = Grid().from_string(invalid_grid_chars)
        invalid_result = invalid_grid.is_valid_grid()
        self.assertFalse(invalid_result)


#--- BASIC TESTS FOR GRID CLASS FORMATION -------------------------------------

    def test_grid_instance(self):
        grid0 = Grid()
        self.assertIsInstance(grid0, Grid)

    def test_grid_instance_from_chars_linear(self):
        chars0 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        grid0_from_chars = Grid().from_string(chars0)
        self.assertIsInstance(grid0_from_chars, Grid)

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
