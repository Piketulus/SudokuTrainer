import pygame
from services.gameService import GameService
from .button import Button
from .drawSudoku import DrawSudoku
import sys

class UI:

    def __init__(self):
        pygame.init()
        self._current_screen = "start"
        self._objects = []
        self._screen = pygame.display.set_mode((550, 700))
        pygame.display.set_caption("Sudoku")
        self._font = pygame.font.SysFont("comicsans", 30)
        self.clock = pygame.time.Clock()

    def _run(self):
        self._objects = []

        if self._current_screen == "start":
            self._draw_start_screen()

        elif self._current_screen == "playSudoku":
            gameService = GameService()
            self._screen.fill((255,255,255))
            self._screen.blit(self._font.render("Generating your sudoku,", 1, (0, 0, 0)), (100, 200))
            self._screen.blit(self._font.render("please wait...", 1, (0, 0, 0)), (180, 300))
            pygame.display.flip()
            sudoku = gameService.generate_sudoku(9, 53)
            play = DrawSudoku(sudoku)
            play.draw(self._screen)
            self._objects.append(Button(400, 550, 100, 50, "Quit", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self._start_screen, True))

        pygame.display.flip()

        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self._current_screen == "playSudoku":
                    if event.type == pygame.KEYUP:
                        if play.selected != None:
                            row = (play.selected.y - 52) // 50
                            col = (play.selected.x - 52) // 50
                            play.undo_stack.append((play.selected, play.selected.text, row, col))
                            if event.key == pygame.K_1:
                                play.selected.text = "1"
                                play.sudoku.update_grid(row, col, 1)
                            elif event.key == pygame.K_2:
                                play.selected.text = "2"
                                play.sudoku.update_grid(row, col, 2)
                            elif event.key == pygame.K_3:
                                play.selected.text = "3"
                                play.sudoku.update_grid(row, col, 3)
                            elif event.key == pygame.K_4:
                                play.selected.text = "4"
                                play.sudoku.update_grid(row, col, 4)
                            elif event.key == pygame.K_5:
                                play.selected.text = "5"
                                play.sudoku.update_grid(row, col, 5)
                            elif event.key == pygame.K_6:
                                play.selected.text = "6"
                                play.sudoku.update_grid(row, col, 6)
                            elif event.key == pygame.K_7:
                                play.selected.text = "7"
                                play.sudoku.update_grid(row, col, 7)
                            elif event.key == pygame.K_8:
                                play.selected.text = "8"
                                play.sudoku.update_grid(row, col, 8)
                            elif event.key == pygame.K_9:
                                play.selected.text = "9"
                                play.sudoku.update_grid(row, col, 9)
                            elif event.key == pygame.K_BACKSPACE:
                                play.selected.text = ""
                                play.sudoku.update_grid(row, col, 0)
            for obj in self._objects:
                obj.draw(self._screen)
                obj.process()
            if self._current_screen == "playSudoku":
                for obj in play.objects:
                    obj.draw(self._screen)
                    obj.process()
                if play.selected != None:
                    play.selected.color = (200, 200, 200)
                if play.sudoku.is_solved() and play.solved == False:
                    play.solved_graphic(self._screen)
            
            pygame.display.flip()


    def show_screen(self):
        self._run()


    def quit_screen(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    

    def _draw_start_screen(self):
        self._screen.fill((255,192,203))
        self._objects.append(Button(175, 100, 200, 50, "Start", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self._sudoku_screen))
        self._objects.append(Button(175, 550, 200, 50, "Quit", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self.quit_screen))


    def _start_screen(self):
        self._current_screen = "start"
        self._run()


    def _sudoku_screen(self):
        self._current_screen = "playSudoku"
        self._run()

    