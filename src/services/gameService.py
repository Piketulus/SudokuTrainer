import random
from entities.sudoku import Sudoku

class GameService:
    # logic and generation of game

    def __init__(self):
        pass

    def validPlacement(self, grid, row, col, num):
        # check if num is valid in row
        for i in range(9):
            if grid[row][i] == num:
                return False

        # check if num is valid in col
        for i in range(9):
            if grid[i][col] == num:
                return False

        # check if num is valid in 3x3 box
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False

        return True

    def createRandomSudoku(self, sudoku):
        # Baseline Sudoku with numbers filled in
        grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        
        #Randomly shuffle the grid a random number of times
        for i in range(1):#random.randint(20, 100)):
            block = 0
            for j in range(3):
                if random.randint(0, 1) == 1:
                    rows = random.sample(range(block, block + 3), 2)
                    columns = random.sample(range(block, block + 3), 2)
                    #swap two rows in the grid
                    grid[rows[0]], grid[rows[1]] = grid[rows[1]], grid[rows[0]]
                    #swap two columns in the grid
                    for k in range(9):
                        grid[k][columns[0]], grid[k][columns[1]] = grid[k][columns[1]], grid[k][columns[0]]
                block += 3
            
            if random.randint(0, 1) == 1:
                #swap two row blocks in the grid
                blocks = random.sample(range(0, 9, 3), 2)
                for k in range(3):
                    grid[blocks[0] + k], grid[blocks[1] + k] = grid[blocks[1] + k], grid[blocks[0] + k]
            
            if random.randint(0, 1) == 1:
                #swap two column blocks in the grid
                blocks = random.sample(range(0, 9, 3), 2)
                for k in range(3):
                    for l in range(9):
                        grid[l][blocks[0] + k], grid[l][blocks[1] + k] = grid[l][blocks[1] + k], grid[l][blocks[0] + k]

        sudoku.solution = grid


        
    
    def solve(self, Sudoku):
        # solve the sudoku using backtracking
        grid = Sudoku.grid
        pass


if __name__ == "__main__":
    sudoku = Sudoku(9)
    gameService = GameService()
    gameService.createRandomSudoku(sudoku)
    print(sudoku)