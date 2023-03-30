#main
from entities.sudoku import Sudoku
from services.gameService import GameService
import time

if __name__ == "__main__":
    start = time.time()
    sudoku = Sudoku(9, 15)
    gameService = GameService()
    gameService.createGame(sudoku)
    print(sudoku)
    count = 0
    for i in range(sudoku.size):
        for j in range(sudoku.size):
            if sudoku.grid[i][j] != 0:
                count += 1
    print("Number of numbers in the grid: " + str(count))
    #gameService.solve(sudoku)
    #print(sudoku)
    end = time.time()
    print("time:", end-start, "s")