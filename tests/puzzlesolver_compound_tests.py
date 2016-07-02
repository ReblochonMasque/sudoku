"""
puzzlesolver_compound_tests.py
:created on: 20160701
__author__ = 'Frederic Dupont'
:License: GPL3
"""

import unittest

from sudoku.puzzle import Puzzle, make_grid_from_string
# from sudoku.puzzleconstants import DIGITS, SQUARES
from sudoku.puzzlesolver import PuzzleSolver


class TestPuzzleSolver(unittest.TestCase):

    def setUp(self):

        # Very Hard --> require search
        self.g1 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        self.partial_s1 = '4.....8.5.3..........7......2.....6.....8.4...4..1.......6.3.7.5.32.1...1.4......'
        self.s1 = ''

        self.g2 = '1...895..5....7819........72.4..8.7.9.71.54.8.8.7..3.531.4..78.4682....3..985...1'
        self.partial_s2 = '172.895.454..2781989.5142.7254938176937165428681742395315496782468271953729853641'
        self.s2 = ''

        # Not so hard - no search needed
        self.g3 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
        self.s3 = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'

        self.g4 = '.82...59....8.1..3..52...78...37842...........27945...91...68..2..7.9....73...95.'
        self.s4 = '382467591796851243145293678561378429439612785827945316914526837258739164673184952'

        self.g5 = '437...189.6.183.......9.536.73..1...9..4.7..1...5..69.124.7.......645.1.356...974'
        self.s5 = '437256189569183742812794536673921458985467321241538697124379865798645213356812974'

        self.g6 = '.6..7.4..5......12...1....7..5.4.27..3.....4..19.6.8...4...1...79.6....8..1.3..2.'
        self.s6 = '163275489578496312924183567685349271237518946419762853346821795792654138851937624'

        self.g7 = '7.9..3.85812..6.375.478..1.3.196..5.426..789...52..6.1143.7.56....3..1.8......3..'
        self.s7 = '769123485812456937534789216381964752426517893975238641143872569697345128258691374'

        self.g8 = '31.....78526.9.13.8..6.359228.4.9..1..3.862..6..1.5..3...2.13467.1...8...6...891.'
        self.s8 = '319542678526897134874613592285439761143786259697125483958271346731964825462358917'

        self.g9 = '.1869.....5....71..7..3..62.21863...7..5...365...419.88...72.4..47.18.9.....563..'
        self.s9 = '218697453356284719479135862921863574784529136563741928835972641647318295192456387'

        self.g10 = '...12.4.5.4.6..7.8.26......47.5...31.........31...8..9.8..1.......2..5.4..24.79.6'
        self.s10 = '837129465941653728526874193478592631269341857315768249684915372793286514152437986'

        self.g11 = '.5...478...67.95..2.7.5.1.3.2.....6..981.543..3.....7.1.5..7..8..35.26.7.728...5.'
        self.s11 = '359214786816739524247658193721483965698175432534926871165397248983542617472861359'

        # hard puzzle (X wings and requires 5 full iterations to be solved, but no search)
        self.g12 = '4.......1..6.35.24..984.6.7.3....4..9..68.3.5.1..7.2....542.7.32.....54.......1.2'
        self.s12 = '423796851786135924159842637538219476972684315614573289865421793291367548347958162'


    #-----------------TEST SOLVE--------------------------------------
    @staticmethod
    def _apply_solve(puzzle_string):
        """
        :return: a tuple containing
                 the result of the solve() on the provided string,
                 and a repr of the "solved" puzzle
        """
        grid = make_grid_from_string(puzzle_string)
        grid.parse_grid_candidates()
        solver = PuzzleSolver(grid.clone())
        result = solver.solve()
        return result

    # def test_solve_g1(self):
    #     puzzle_string, expected_string = self.g1, self.s1
    #     resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
    #     self.assertEqual(expected_string, resulting_string)
    #
    # def test_solve_g2(self):
    #     puzzle_string, expected_string = self.g2, self.s2
    #     resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
    #     self.assertEqual(expected_string, resulting_string)

    def test_solve_g3(self):
        puzzle_string, expected_string = self.g3, self.s3
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g4(self):
        puzzle_string, expected_string = self.g4, self.s4
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g5(self):
        puzzle_string, expected_string = self.g5, self.s5
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g6(self):
        puzzle_string, expected_string = self.g6, self.s6
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g7(self):
        puzzle_string, expected_string = self.g7, self.s7
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g8(self):
        puzzle_string, expected_string = self.g8, self.s8
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g9(self):
        puzzle_string, expected_string = self.g9, self.s9
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g10(self):
        puzzle_string, expected_string = self.g10, self.s10
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g11(self):
        puzzle_string, expected_string = self.g11, self.s11
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)

    def test_solve_g12(self):
        puzzle_string, expected_string = self.g12, self.s12
        resulting_string = TestPuzzleSolver._apply_solve(puzzle_string)
        self.assertEqual(expected_string, resulting_string)



    #-----------------TEST ELIMINATE_PROPAGATE_FILL-----------------------
    @staticmethod
    def _apply_eliminate_propagate_fill(puzzle_string):
        """
        :return: a tuple containing
                 the result of eliminate_propagate_fill() on the provided string,
                 and a repr of the "solved" puzzle
        """
        grid = make_grid_from_string(puzzle_string)
        grid.parse_grid_candidates()
        solver = PuzzleSolver(grid.clone())
        result = solver.eliminate_propagate_fill()
        return result, repr(solver._puzzle)

    def test_eliminate_propagate_fill_g1(self):
        puzzle_string, expected_string = self.g1, self.partial_s1
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g2(self):
        puzzle_string, expected_string = self.g2, self.partial_s2
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g3(self):
        puzzle_string, expected_string = self.g3, self.s3
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g4(self):
        puzzle_string, expected_string = self.g4, self.s4
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g5(self):
        puzzle_string, expected_string = self.g5, self.s5
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g6(self):
        puzzle_string, expected_string = self.g6, self.s6
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g7(self):
        puzzle_string, expected_string = self.g7, self.s7
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g8(self):
        puzzle_string, expected_string = self.g8, self.s8
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g9(self):
        puzzle_string, expected_string = self.g9, self.s9
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g10(self):
        puzzle_string, expected_string = self.g10, self.s10
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g11(self):
        puzzle_string, expected_string = self.g11, self.s11
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)

    def test_eliminate_propagate_fill_g12(self):
        puzzle_string, expected_string = self.g12, self.s12
        result, resulting_string = TestPuzzleSolver._apply_eliminate_propagate_fill(puzzle_string)
        self.assertTrue(result)
        self.assertEqual(expected_string, resulting_string)


if __name__ == '__main__':
    unittest.main()
