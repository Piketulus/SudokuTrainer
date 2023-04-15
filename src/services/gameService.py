import copy
from math import sqrt
import random
from entities.sudoku import Sudoku
import signal
import pygame

class GameService:
    # logic and generation of game

    def _valid_placement(self, size, grid, row, col, num):
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
    

    def _create_random_solution(self, sudoku):
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
        
        #Randomly shuffle the grid a random number of times while keeping the sudoku in correct form
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
        
    
    def _solve(self, sudoku, row=0, col=0, testUnique=False):
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
            if self._valid_placement(sudoku.size, grid, row, col, i):
                grid[row][col] = i
                if self._solve(sudoku, row, col, testUnique):
                    return True
                grid[row][col] = 0

        return False


    def _create_puzzle(self, sudoku):
        # creates a puzzle from a solved sudoku by trying to remove numbers while keeping the sudoku uniquely solvable
        self._create_random_solution(sudoku)
        
        grid = sudoku.grid

        number_locations = []
        for i in range(sudoku.size):
            number_locations.append(set())
        for i in range(sudoku.size):
            for j in range(sudoku.size):
                number_locations[grid[i][j] - 1].add(i * sudoku.size + j)

        square_set = set(range(sudoku.size * sudoku.size))
        choose_from_set = set(range(sudoku.size * sudoku.size))

        while len(square_set) > 25 + sudoku.difficulty:
            remove = random.choice(list(square_set))
            row = remove // sudoku.size
            col = remove % sudoku.size
            if len(number_locations[grid[row][col] - 1]) == 1:
                continue
            
            number_locations[grid[row][col] - 1].remove(remove)
            grid[row][col] = 0

            testcopy = copy.deepcopy(sudoku)
            if self._solve(testcopy, testUnique=True):
                grid[row][col] = sudoku.solution[row][col]
                if remove in choose_from_set:
                    choose_from_set.remove(remove)
                number_locations[grid[row][col] - 1].add(remove)
                continue

            square_set.remove(remove)
            choose_from_set.remove(remove)
    

    def _handler(signum, frame):
        raise Exception('Action took too much time')


    def generate_sudoku(self, size, difficulty):
        #called from outside the class to generate a sudoku given a size and difficulty
        sudoku = Sudoku(size, difficulty)
        done = False
        signal.signal(signal.SIGALRM, self._handler)
        signal.alarm(5)
        while not done:
            try:
                done = True
                self._create_puzzle(sudoku)
                signal.alarm(0)
            except:
                pygame.event.pump()
                done = False
                signal.alarm(5)
        return sudoku
