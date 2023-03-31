from .start import Start
from .playSudoku import PlaySudoku

class UI:

    def __init__(self):
        self.startScreen = Start()
        self.sudoku = PlaySudoku()


    def showStart(self):
        self.startScreen.showScreen()


    def hideStart(self):
        self.startScreen.quitScreen()


    def showSudoku9(self):
        self.sudoku.showScreen()


    def hideSudoku9(self):
        self.sudoku.quitScreen()