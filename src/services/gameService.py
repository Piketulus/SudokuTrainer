import copy
from math import sqrt
import random
from entities.sudoku import Sudoku

class GameService:
    # logic and generation of game

    def __init__(self):
        pass


    def validPlacement(self, size, grid, row, col, num):
        # check if num is valid in row
        for i in range(size):
            if grid[row][i] == num:
                return False

        # check if num is valid in col
        for i in range(size):
            if grid[i][col] == num:
                return False

        # check if num is valid in box
        startRow = row - row % int(sqrt(size))
        startCol = col - col % int(sqrt(size))
        for i in range(int(sqrt(size))):
            for j in range(int(sqrt(size))):
                if grid[i + startRow][j + startCol] == num:
                    return False

        return True


    def createRandomSolution(self, sudoku):
        size = sudoku.size
        boxsize = int(sqrt(size))
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
        for i in range(random.randint(20, 100)):
            block = 0
            for j in range(boxsize):
                if random.randint(0, 1) == 1:
                    rows = random.sample(range(block, block + boxsize), 2)
                    columns = random.sample(range(block, block + boxsize), 2)
                    #swap two rows in the grid
                    grid[rows[0]], grid[rows[1]] = grid[rows[1]], grid[rows[0]]
                    #swap two columns in the grid
                    for k in range(size):
                        grid[k][columns[0]], grid[k][columns[1]] = grid[k][columns[1]], grid[k][columns[0]]
                block += boxsize
            
            if random.randint(0, 1) == 1:
                #swap two row blocks in the grid
                blocks = random.sample(range(0, size, boxsize), 2)
                for k in range(boxsize):
                    grid[blocks[0] + k], grid[blocks[1] + k] = grid[blocks[1] + k], grid[blocks[0] + k]
            
            if random.randint(0, 1) == 1:
                #swap two column blocks in the grid
                blocks = random.sample(range(0, size, boxsize), 2)
                for k in range(boxsize):
                    for l in range(size):
                        grid[l][blocks[0] + k], grid[l][blocks[1] + k] = grid[l][blocks[1] + k], grid[l][blocks[0] + k]

        sudoku.grid = copy.deepcopy(grid)
        sudoku.solution = copy.deepcopy(grid)
        
    
    def solve(self, sudoku, row=0, col=0, testUnique=False):
        # solves a sudoku using backtracking
        grid = sudoku.grid
        while grid[row][col] != 0:
            col += 1
            if col == sudoku.size:
                row += 1
                col = 0
            if row == sudoku.size:
                if testUnique:
                    if sudoku.solution == grid:
                        return False
                return True
        for i in range(1, sudoku.size + 1):
            if self.validPlacement(sudoku.size, grid, row, col, i):
                grid[row][col] = i
                if self.solve(sudoku, row, col, testUnique):
                    return True
                grid[row][col] = 0
        return False


    def createGame(self, sudoku):

        self.createRandomSolution(sudoku)
        
        grid = sudoku.grid
        squareSet = set(range(0, 80))

        while len(squareSet) > 20 + (sudoku.difficulty * 4):
            remove = random.choice(list(squareSet))
            squareSet.remove(remove)
            row = remove // sudoku.size
            col = remove % sudoku.size
            grid[row][col] = 0

        testcopy = copy.deepcopy(sudoku)
        while self.solve(testcopy, testUnique=True):
            row = 0
            col = 0
            while testcopy.grid[row][col] == testcopy.solution[row][col]:
                col += 1
                if col == sudoku.size:
                    row += 1
                    col = 0
                if row == sudoku.size:
                    break
            grid[row][col] = sudoku.solution[row][col]
            testcopy = copy.deepcopy(sudoku)