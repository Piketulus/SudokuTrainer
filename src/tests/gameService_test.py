import unittest
from services.gameService import GameService

class GameServiceTest(unittest.TestCase):
    
    def setUp(self):
        self.gameService = GameService()

    def test_validPlacement(self):
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
        self.assertFalse(self.gameService.validPlacement(size, grid, row, col, num))
        row = 0
        col = 4
        num = 7
        self.assertTrue(self.gameService.validPlacement(size, grid, row, col, num))