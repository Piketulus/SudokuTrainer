import copy
import signal
from math import sqrt
import random
import pygame
from entities.sudoku import Sudoku


class GameService:
    """
    Class responsible for generating sudoku puzzle and handling their logic.
    """

    def _valid_placement(self, size, grid, row, col, num):
        """
         Checks if num is valid to place in row col. 
         This is used to check if a certain value ( grid ) can be placed in a cell ( row col )

         Args:
                 size: Size of the grid
                 grid: the sudoku grid (2d list)
                 row: Row index of the cell to place in
                 col: Column index of the cell to place in
                 num: Number to be placed in the cell

         Returns: 
                 True if num is valid False if not
        """
        # check if num is valid in row
        for i in range(size):
            if grid[row][i] == num:
                return False

        # check if num is valid in col
        for i in range(size):
            if grid[i][col] == num:
                return False

        # check if num is valid in box
        start_row = row - row % int(sqrt(size))
        start_col = col - col % int(sqrt(size))
        for i in range(int(sqrt(size))):
            for j in range(int(sqrt(size))):
                if grid[i + start_row][j + start_col] == num:
                    return False

        return True

    def _create_random_solution(self, sudoku):
        """
         Creates a random solution for the sudoku by shuffling.

         Args:
                 sudoku: The Sudoku object to be manipulated
        """

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

        # Randomly shuffle the grid a random number
        # of times while keeping the sudoku in correct form
        for _ in range(random.randint(20, 100)):
            block = 0
            for _ in range(boxsize):
                rows = random.sample(range(block, block + boxsize), 2)
                columns = random.sample(range(block, block + boxsize), 2)
                # swap two rows in the grid
                grid[rows[0]], grid[rows[1]] = grid[rows[1]], grid[rows[0]]
                # swap two columns in the grid
                for i in range(size):
                    grid[i][columns[0]], grid[i][columns[1]
                                                 ] = grid[i][columns[1]], grid[i][columns[0]]
                block += boxsize

            # swap two row blocks in the grid
            blocks = random.sample(range(0, size, boxsize), 2)
            for i in range(boxsize):
                grid[blocks[0] + i], grid[blocks[1] +
                                          i] = grid[blocks[1] + i], grid[blocks[0] + i]

            # swap two column blocks in the grid
            blocks = random.sample(range(0, size, boxsize), 2)
            for i in range(boxsize):
                for j in range(size):
                    grid[j][blocks[0] + i], grid[j][blocks[1] +
                                            i] = grid[j][blocks[1] + i], grid[j][blocks[0] + i]

        sudoku.grid = copy.deepcopy(grid)
        sudoku.solution = copy.deepcopy(grid)

    def _solve(self, sudoku, row=0, col=0, test_unique=False):
        """
         Solves a sudoku using backtracking. This is a recursive function 
         that tries to find a solution starting in the given row and column.

         Args:
                 sudoku: The Sudoku object to be solved
                 row: The row of the sudoku to start with
                 col: The column of the sudoku to start with
                 test_unique: If True will test for multiple solutions

         Returns: 
                 True if there is a solution False if not. 
                 With test_unique, returns True if there are multiple solutions.
        """
        # solves a sudoku using backtracking
        grid = sudoku.grid

        while grid[row][col] != 0:
            col += 1
            if col == sudoku.size:
                row += 1
                col = 0
            if row == sudoku.size:
                if test_unique and sudoku.solution == grid:
                    return False
                return True

        for i in range(1, sudoku.size + 1):
            if self._valid_placement(sudoku.size, grid, row, col, i):
                grid[row][col] = i
                if self._solve(sudoku, row, col, test_unique):
                    return True
                grid[row][col] = 0

        return False

    def _create_puzzle(self, sudoku):
        """
         Creates a puzzle from a solved sudoku by trying to 
         remove numbers while keeping the sudoku uniquely solvable.

         Args:
                 sudoku: The Sudoku object to create the puzzle in
        """

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
            if self._solve(testcopy, test_unique=True):
                grid[row][col] = sudoku.solution[row][col]
                if remove in choose_from_set:
                    choose_from_set.remove(remove)
                number_locations[grid[row][col] - 1].add(remove)
                continue

            square_set.remove(remove)
            choose_from_set.remove(remove)

    def _handler(self, signum, frame):
        """
         Signal handler for signals. This is called in response to 
         SIGALRM and will raise : exc : ` TimeoutError `.

         Args:
                 signum: The signal that was received
                 frame: The stack frame of the signal
        """
        raise TimeoutError

    def generate_sudoku(self, size, difficulty):
        """
         Generate a sudoku of the given size and difficulty. 
         This is a blocking call until the puzzle is created or a timeout occurs.

         Args:
                 size: The size of the sudoku.
                 difficulty: The difficulty of the sudoku.

         Returns: 
                 An instance of the Sudoku class with the generated puzzle.
        """
        sudoku = Sudoku(size, difficulty)
        done = False
        signal.signal(signal.SIGALRM, self._handler)
        signal.alarm(5)
        while not done:
            try:
                done = True
                self._create_puzzle(sudoku)
                signal.alarm(0)
            except TimeoutError:
                pygame.event.pump()
                done = False
                signal.alarm(5)
        return sudoku
