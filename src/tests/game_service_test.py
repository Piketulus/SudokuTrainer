import unittest
from services.game_service import GameService
from entities.sudoku import Sudoku


class GameServiceTest(unittest.TestCase):

    def setUp(self):
        self.gameService = GameService()
        self.sudoku = Sudoku(9, 15)

    def test_valid_placement(self):
        size = 9
        grid = [[5, 0, 3, 8, 0, 6, 1, 2, 0],
                [8, 7, 6, 0, 1, 9, 0, 5, 3],
                [0, 0, 0, 5, 4, 3, 0, 0, 0],
                [7, 6, 5, 1, 0, 0, 0, 0, 0],
                [4, 0, 0, 7, 0, 0, 9, 1, 8],
                [0, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 0, 1],
                [0, 0, 1, 6, 0, 0, 8, 0, 7],
                [9, 0, 0, 0, 0, 1, 5, 0, 0]]
        row = 0
        col = 1
        num = 7
        self.assertFalse(self.gameService._valid_placement(
            size, grid, row, col, num))
        row = 0
        col = 4
        num = 7
        self.assertTrue(self.gameService._valid_placement(
            size, grid, row, col, num))

    def test_create_random_solution_is_different(self):
        sudoku1 = Sudoku(9, 15)
        sudoku2 = Sudoku(9, 15)
        self.gameService._create_random_solution(sudoku1)
        self.gameService._create_random_solution(sudoku2)
        self.assertNotEqual(sudoku1.solution, sudoku2.solution)

    def test_create_random_solution_is_valid(self):
        self.gameService._create_random_solution(self.sudoku)
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                num = self.sudoku.solution[i][j]
                self.sudoku.solution[i][j] = 0
                self.assertTrue(self.gameService._valid_placement(
                    self.sudoku.size, self.sudoku.solution, i, j, num))
                self.sudoku.solution[i][j] = num

    def test_solve(self):
        self.sudoku.grid = [[2, 0, 3, 0, 4, 1, 0, 5, 7],
                            [7, 0, 1, 0, 0, 8, 0, 0, 0],
                            [4, 0, 6, 0, 0, 0, 1, 3, 0],
                            [0, 3, 5, 0, 0, 6, 0, 0, 0],
                            [0, 7, 9, 4, 8, 5, 2, 1, 0],
                            [0, 2, 4, 1, 3, 0, 6, 9, 5],
                            [0, 0, 2, 7, 1, 0, 0, 0, 0],
                            [0, 0, 0, 8, 0, 2, 0, 6, 1],
                            [5, 0, 0, 0, 0, 0, 7, 0, 0]]
        self.sudoku.solution = [[2, 9, 3, 6, 4, 1, 8, 5, 7],
                                [7, 5, 1, 3, 2, 8, 9, 4, 6],
                                [4, 8, 6, 5, 7, 9, 1, 3, 2],
                                [1, 3, 5, 2, 9, 6, 4, 7, 8],
                                [6, 7, 9, 4, 8, 5, 2, 1, 3],
                                [8, 2, 4, 1, 3, 7, 6, 9, 5],
                                [3, 6, 2, 7, 1, 4, 5, 8, 9],
                                [9, 4, 7, 8, 5, 2, 3, 6, 1],
                                [5, 1, 8, 9, 6, 3, 7, 2, 4]]
        self.gameService._solve(self.sudoku)
        self.assertEqual(self.sudoku.solution, self.sudoku.grid)

    def test_create_puzzle_grid_and_solution_match(self):
        self.gameService._create_puzzle(self.sudoku)
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] != 0:
                    self.assertEqual(
                        self.sudoku.solution[i][j], self.sudoku.grid[i][j])

    def test_create_puzzle_solution_is_valid(self):
        self.gameService._create_puzzle(self.sudoku)
        self.gameService._solve(self.sudoku)
        self.assertEqual(self.sudoku.solution, self.sudoku.grid)

    def test_generate_sudoku_difficulty(self):
        sudoku = self.gameService.generate_sudoku(9, 14)
        count = 0
        for i in range(sudoku.size):
            for j in range(sudoku.size):
                if sudoku.grid[i][j] != 0:
                    count += 1
        self.assertEqual(count, 39)
