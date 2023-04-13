import pygame
from services.gameService import GameService
from .button import Button
from .playSudoku import PlaySudoku

class Start:

    def __init__(self):
        pygame.init()
        self.current_screen = "start"
        self.objects = []
        self.screen = pygame.display.set_mode((550, 700))
        pygame.display.set_caption("Sudoku")
        self.font = pygame.font.SysFont("comicsans", 30)

    def _start(self):

        if self.current_screen == "start":
            self._start_screen()

        elif self.current_screen == "playSudoku":
            gameService = GameService()
            self.screen.fill((255,255,255))
            self.screen.blit(self.font.render("Generating your sudoku,", 1, (0, 0, 0)), (100, 200))
            self.screen.blit(self.font.render("please wait...", 1, (0, 0, 0)), (180, 300))
            pygame.display.flip()
            sudoku = gameService.generate_sudoku(9, 55)
            play = PlaySudoku(sudoku)
            play.draw(self.screen)
            self.objects = play._objects

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if self.current_screen == "playSudoku":
                    if event.type == pygame.KEYUP:
                        if play._selected != None:
                            row = (play._selected.y - 52) // 50
                            col = (play._selected.x - 52) // 50
                            if event.key == pygame.K_1:
                                play._selected.text = "1"
                                play._sudoku.update_grid(row, col, 1)
                            elif event.key == pygame.K_2:
                                play._selected.text = "2"
                                play._sudoku.update_grid(row, col, 2)
                            elif event.key == pygame.K_3:
                                play._selected.text = "3"
                                play._sudoku.update_grid(row, col, 3)
                            elif event.key == pygame.K_4:
                                play._selected.text = "4"
                                play._sudoku.update_grid(row, col, 4)
                            elif event.key == pygame.K_5:
                                play._selected.text = "5"
                                play._sudoku.update_grid(row, col, 5)
                            elif event.key == pygame.K_6:
                                play._selected.text = "6"
                                play._sudoku.update_grid(row, col, 6)
                            elif event.key == pygame.K_7:
                                play._selected.text = "7"
                                play._sudoku.update_grid(row, col, 7)
                            elif event.key == pygame.K_8:
                                play._selected.text = "8"
                                play._sudoku.update_grid(row, col, 8)
                            elif event.key == pygame.K_9:
                                play._selected.text = "9"
                                play._sudoku.update_grid(row, col, 9)
                            elif event.key == pygame.K_BACKSPACE:
                                play._selected.text = ""
                                play._sudoku.update_grid(row, col, 0)
            for obj in self.objects:
                obj.draw(self.screen)
                obj.process()
            if self.current_screen == "playSudoku":
                if play._selected != None:
                    play._selected.color = (200, 200, 200)
                    
                if play._sudoku.is_solved() and play.solved == False:
                    play.solved_graphic(self.screen)

            pygame.display.flip()


    def show_screen(self):
        self._start()


    def quit_screen(self):
        pygame.quit()
    

    def _start_screen(self):
        self.objects = []
        self.screen.fill((255,192,203))
        start_button = Button(100, 100, 200, 50, "Start", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self._sudoku_screen)
        self.objects.append(start_button)


    def _sudoku_screen(self):
        self.current_screen = "playSudoku"
        self._start()

    