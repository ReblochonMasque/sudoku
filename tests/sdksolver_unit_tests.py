# -*- coding: utf-8 -*-
"""
sdksolver_unit_tests.py
Unit Tests for sdksolver

Created on Wed Jun  1 15:30:52 2016

@author: fredericdupont
"""

import unittest
from boardkeys import DIGITS
from sdksolver import Grid, make_grid_from_string
import test_data


class TestGrid(unittest.TestCase):

    def setUp(self):
        valid_grid_0_chars = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.valid_grid_0 = make_grid_from_string(valid_grid_0_chars)

    def test_is_valid_grid_0(self):
        """ tests is a valid grid is valid
        """
        result = self.valid_grid_0.is_valid_grid()
        self.assertTrue(result)

    # TODO: refactor with context manager?
    def test_is_invalid_grid_long_string(self):
        """ tests an invalid grid formed with a string that is either too long or too short
        """
        invalid_long_grid_chars = '12.4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        # longer by '12.' at the start
        result = True
        try:
            Grid().from_string(invalid_long_grid_chars)
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
            Grid().from_string(invalid_short_grid_chars)
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

    def test_non_uniques_in_rows(self):
        """ tests if all values in a row are unique
        """
        chars_repeats_in_row = '4..4..8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        #                       ^  ^
        invalid_grid = Grid().from_string(chars_repeats_in_row)
        invalid_result = invalid_grid.is_valid_grid()
        self.assertFalse(invalid_result)

    def test_non_uniques_in_cols(self):
        """ tests if all values in a column are unique
        """
        chars_repeats_in_col = '4.....8.5.3..........7.....42.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        #                       ^                          ^
        invalid_grid = Grid().from_string(chars_repeats_in_col)
        invalid_result = invalid_grid.is_valid_grid()
        self.assertFalse(invalid_result)

    def test_non_uniques_in_boxes(self):
        """ tests if all values in a box are unique
        """
        chars_repeats_in_box = '4.....8.543..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        #                       ^        ^
        invalid_grid = Grid().from_string(chars_repeats_in_box)
        invalid_result = invalid_grid.is_valid_grid()
        self.assertFalse(invalid_result)

    # --- BASIC TESTS FOR VALUES -------------------------------------

    def test_values_keys_match_grid_keys(self):
        """tests that the keys of _grid and _values are the same
        """
        result = self.valid_grid_0.possible_values
        expected = {'Gh': '123456789', 'Fe': '123456789', 'Ab': '123456789', 'Db': '123456789', 'Ei': '123456789', 'Ba': '123456789', 'Ac': '123456789', 'Eh': '123456789', 'Ih': '123456789', 'He': '123456789', 'Eg': '123456789', 'Hd': '123456789', 'Bi': '123456789', 'Cg': '123456789', 'Cc': '123456789', 'Hi': '123456789', 'Af': '123456789', 'Aa': '123456789', 'Ia': '123456789', 'Bg': '123456789', 'Gf': '123456789', 'Ai': '123456789', 'Hb': '123456789', 'Ae': '123456789', 'Fa': '123456789', 'Ge': '123456789', 'Hh': '123456789', 'Cd': '123456789', 'Ha': '123456789', 'Fi': '123456789', 'Hf': '123456789', 'Gg': '123456789', 'De': '123456789', 'Df': '123456789', 'Hg': '123456789', 'Dd': '123456789', 'Da': '123456789', 'Ga': '123456789', 'Ic': '123456789', 'Bc': '123456789', 'Ci': '123456789', 'Dh': '123456789', 'Bd': '123456789', 'Di': '123456789', 'Bf': '123456789', 'Id': '123456789', 'Cb': '123456789', 'Gd': '123456789', 'Hc': '123456789', 'Gi': '123456789', 'Ch': '123456789', 'Ee': '123456789', 'Ea': '123456789', 'Ff': '123456789', 'Fg': '123456789', 'Fc': '123456789', 'Bb': '123456789', 'Ie': '123456789', 'If': '123456789', 'Ad': '123456789', 'Eb': '123456789', 'Gb': '123456789', 'Ib': '123456789', 'Cf': '123456789', 'Ef': '123456789', 'Ig': '123456789', 'Dg': '123456789', 'Ah': '123456789', 'Ed': '123456789', 'Fb': '123456789', 'Gc': '123456789', 'Fd': '123456789', 'Bh': '123456789', 'Ce': '123456789', 'Ag': '123456789', 'Dc': '123456789', 'Ii': '123456789', 'Ec': '123456789', 'Ca': '123456789', 'Fh': '123456789', 'Be': '123456789'}
        self.assertEqual(result.keys(), expected.keys())

    def test_values_in_possible_values_match_digits(self):
        """tests that the keys of _grid and _values are the same
        """
        result = self.valid_grid_0.possible_values.values()
        self.assertTrue(all(res == DIGITS for res in result))


    # --- BASIC TESTS FOR GRID CLASS FORMATION -------------------------------------

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
