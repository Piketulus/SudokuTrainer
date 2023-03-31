from .start import Start
from .playSudoku import PlaySudoku

class UI:

    def __init__(self):
        self.start_screen = Start()
        self.sudoku = PlaySudoku()


    def show_start(self):
        self.start_screen.show_screen()


    def hide_start(self):
        self.start_screen.quit_screen()


    def show_play_sudoku(self):
        self.sudoku.show_screen()


    def hide__play_sudoku(self):
        self.sudoku.quit_screen()