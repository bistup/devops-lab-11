import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_valid_sudoku_1(self):
        sudoku = [
            0, 0, 4, 0, 5, 0, 0, 0, 0,
            9, 0, 0, 7, 3, 4, 6, 0, 0,
            0, 0, 3, 0, 2, 1, 0, 4, 9,
            0, 3, 5, 0, 9, 0, 4, 8, 0,
            0, 9, 0, 0, 0, 0, 0, 3, 0,
            0, 7, 6, 0, 1, 0, 9, 2, 0,
            3, 1, 0, 9, 7, 0, 2, 0, 0,
            0, 0, 9, 1, 8, 2, 0, 0, 3,
            0, 0, 0, 0, 6, 0, 1, 0, 0
        ]
        expected_solution = [
            2, 6, 4, 8, 5, 9, 3, 1, 7,
            9, 8, 1, 7, 3, 4, 6, 5, 2,
            7, 5, 3, 6, 2, 1, 8, 4, 9,
            1, 3, 5, 2, 9, 7, 4, 8, 6,
            8, 9, 2, 5, 4, 6, 7, 3, 1,
            4, 7, 6, 3, 1, 8, 9, 2, 5,
            3, 1, 8, 9, 7, 5, 2, 6, 4,
            6, 4, 9, 1, 8, 2, 5, 7, 3,
            5, 2, 7, 4, 6, 3, 1, 9, 8
        ]
        solution = solve_sudoku(sudoku)
        self.assertEqual(solution, expected_solution)
        print("Test valid_sudoku_1 solved:")
        for i in range(9):
            print(solution[i * 9:i * 9 + 9])

    def test_valid_sudoku_2(self):
        sudoku = [
            5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        expected_solution = [
            5, 3, 4, 6, 7, 8, 9, 1, 2,
            6, 7, 2, 1, 9, 5, 3, 4, 8,
            1, 9, 8, 3, 4, 2, 5, 6, 7,
            8, 5, 9, 7, 6, 1, 4, 2, 3,
            4, 2, 6, 8, 5, 3, 7, 9, 1,
            7, 1, 3, 9, 2, 4, 8, 5, 6,
            9, 6, 1, 5, 3, 7, 2, 8, 4,
            2, 8, 7, 4, 1, 9, 6, 3, 5,
            3, 4, 5, 2, 8, 6, 1, 7, 9
        ]
        solution = solve_sudoku(sudoku)
        self.assertEqual(solution, expected_solution)
        print("Test valid_sudoku_2 solved:")
        for i in range(9):
            print(solution[i * 9:i * 9 + 9])

    def test_invalid_sudoku(self):
        sudoku = [
            5, 5, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9
        ]
        solution = solve_sudoku(sudoku)
        self.assertIsNone(solution)
        print("Test invalid_sudoku returned None as expected.")

    def test_empty_sudoku(self):
        sudoku = [0] * 81
        expected_solution = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            4, 5, 6, 7, 8, 9, 1, 2, 3,
            7, 8, 9, 1, 2, 3, 4, 5, 6,
            2, 3, 4, 5, 6, 7, 8, 9, 1,
            5, 6, 7, 8, 9, 1, 2, 3, 4,
            8, 9, 1, 2, 3, 4, 5, 6, 7,
            3, 4, 5, 6, 7, 8, 9, 1, 2,
            6, 7, 8, 9, 1, 2, 3, 4, 5,
            9, 1, 2, 3, 4, 5, 6, 7, 8
        ]
        solution = solve_sudoku(sudoku)
        self.assertEqual(solution, expected_solution)
        print("Test empty_sudoku solved:")
        for i in range(9):
            print(solution[i * 9:i * 9 + 9])

    def test_almost_solved_sudoku(self):
        sudoku = [
            1, 2, 3, 4, 5, 6, 7, 8, 0,
            4, 5, 6, 7, 8, 9, 1, 2, 3,
            7, 8, 9, 1, 2, 3, 4, 5, 6,
            2, 3, 4, 5, 6, 7, 8, 9, 1,
            5, 6, 7, 8, 9, 1, 2, 3, 4,
            8, 9, 1, 2, 3, 4, 5, 6, 7,
            3, 4, 5, 6, 7, 8, 9, 1, 2,
            6, 7, 8, 9, 1, 2, 3, 4, 5,
            9, 1, 2, 3, 4, 5, 6, 7, 8
        ]
        expected_solution = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            4, 5, 6, 7, 8, 9, 1, 2, 3,
            7, 8, 9, 1, 2, 3, 4, 5, 6,
            2, 3, 4, 5, 6, 7, 8, 9, 1,
            5, 6, 7, 8, 9, 1, 2, 3, 4,
            8, 9, 1, 2, 3, 4, 5, 6, 7,
            3, 4, 5, 6, 7, 8, 9, 1, 2,
            6, 7, 8, 9, 1, 2, 3, 4, 5,
            9, 1, 2, 3, 4, 5, 6, 7, 8
        ]
        solution = solve_sudoku(sudoku)
        self.assertEqual(solution, expected_solution)
        print("Test almost_solved_sudoku solved:")
        for i in range(9):
            print(solution[i * 9:i * 9 + 9])

    def test_invalid_input(self):
        sudoku = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
            4, 5, 6, 7, 8, 9, 1, 2, 3,
            7, 8, 9, 1, 2, 3, 4, 5, 6,
            2, 3, 4, 5, 6, 7, 8, 9, 1,
            5, 6, 7, 8, 9, 1, 2, 3, 4,
            8, 9, 1, 2, 3, 4, 5, 6, 7,
            3, 4, 5, 6, 7, 8, 9, 1, 2,
            6, 7, 8, 9, 1, 2, 3, 4, 5,
            9, 1, 2, 3, 4, 5, 6, 7, 8, 9  # Invalid row with duplicate 9
        ]
        solution = solve_sudoku(sudoku)
        self.assertIsNone(solution)
        print("Test invalid_input returned None as expected.")

if __name__ == '__main__':
    unittest.main()