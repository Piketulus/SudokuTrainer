class Sudoku:
    """
    Class representing a Sudoku puzzle.

    Attributes:
        size (int): The size of the Sudoku puzzle.
        grid (list): The grid of the Sudoku puzzle.
        solution (list): The solution of the Sudoku puzzle.
        difficulty (int): The difficulty of the Sudoku puzzle (0-15, 0 being the most difficult)
    """

    def __init__(self, size, difficulty=0):
        self.size = size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.solution = None
        self.difficulty = difficulty

    def isSolved(self):
        return self.grid == self.solution


    def updateGrid(self, row, col, value):
        self.grid[row][col] = value


    def __str__(self):
        # Print the Sudoku information in a readable format
        grid = ""
        for i in range(self.size):
            for j in range(self.size):
                grid += str(self.grid[i][j]) + " "
            grid += "\n"

        solved = ""
        for i in range(self.size):
            for j in range(self.size):
                solved += str(self.solution[i][j]) + " "
            solved += "\n"
            
        return "Sudoku Puzzle:\n" + grid + "\nSolved Sudoku:\n" + solved + "\nDifficulty: " + str(self.difficulty)