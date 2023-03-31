from .start import Start
from .sudoku9 import Sudoku9

class UI:

    def __init__(self):
        self.startScreen = Start()
        self.sudoku9 = Sudoku9()


    def showStart(self):
        self.startScreen.showScreen()


    def hideStart(self):
        self.startScreen.quitScreen()


    def showSudoku9(self):
        self.sudoku9.showScreen()


    def hideSudoku9(self):
        self.sudoku9.quitScreen()