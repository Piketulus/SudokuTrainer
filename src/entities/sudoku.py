class Sudoku:
    """
    Class representing a Sudoku puzzle.

    Attributes:
        size (int): The size of the Sudoku puzzle.
        solution (list): The solution of the Sudoku puzzle.
        difficulty (str): The difficulty of the Sudoku puzzle.
        solved (bool): Whether the Sudoku puzzle is solved.
    """

    def __init__(self, size, solution=None, difficulty=0, solved=False):
        self.size = size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.solution = solution
        self.difficulty = difficulty
        self.solved = solved

    def __str__(self):
        return f"Grid: {self.grid} Size: {self.size} Solution: {self.solution} Difficulty: {self.difficulty} Solved: {self.solved}"