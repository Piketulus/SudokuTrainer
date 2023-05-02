import pygame
from services.game_service import GameService
from .draw_sudoku import DrawSudoku
from .draw_screens import DrawScreens
import sys


class UI:
    """
    Class that handles the pygame window and the game loop.
    """

    def __init__(self, save_time, show_statistics_view):
        """
         Constructor for the game UI class.

         Args:
                 save_time: function to display the save time popup.
                 show_statistics_view: function to display the statistics view.
        """
        pygame.init()
        self._current_screen = "start"
        self._screen = pygame.display.set_mode((550, 700))
        pygame.display.set_caption("Sudoku")
        self._font = pygame.font.SysFont("comicsans", 30)
        self._clock = pygame.time.Clock()
        self._game_difficulty = 0
        self.drawer = DrawScreens(self._increase_difficulty, self._decrease_difficulty,
                                  self._sudoku_screen, self._quit_screen, self._game_difficulty,
                                  show_statistics_view)
        self._save_time = save_time

    def _run(self):
        # runs the main pygame window loop, drawing the current screen and handling events

        if self._current_screen == "start":
            self.drawer.draw_start_screen(self._screen)

        elif self._current_screen == "playSudoku":
            gameService = GameService()
            self.drawer.draw_wait_screen(self._screen)
            sudoku = gameService.generate_sudoku(9, 15 - self._game_difficulty)
            self._clock.tick(30)
            play = DrawSudoku(sudoku, self._start_screen,
                              self._save_time, self._game_difficulty)
            play.draw(self._screen)

        pygame.display.flip()

        while True:
            self._clock.tick(30)
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if self._current_screen == "playSudoku":
                        if event.type == pygame.KEYUP:
                            if play.selected != None:
                                row = (play.selected.y - 52) // 50
                                col = (play.selected.x - 52) // 50
                                play.undo_stack.append(
                                    (play.selected, play.selected.text, row, col))
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
            except:
                pygame.quit()
                sys.exit()
            if self._current_screen == "start":
                try:
                    for obj in self.drawer.objects:
                        obj.draw(self._screen)
                        obj.process()
                    self._screen.fill((255, 192, 203), (250, 270, 40, 40))
                    self._screen.blit(self._font.render(
                        str(self._game_difficulty), 1, (0, 0, 0)), (250, 270))
                except:
                    pygame.quit()
                    sys.exit()
            if self._current_screen == "playSudoku":
                try:
                    for obj in play.objects:
                        obj.draw(self._screen)
                        obj.process()
                    if play.selected != None:
                        play.selected.color = (200, 200, 200)
                    if not play.sudoku.is_solved():
                        play.update_time(self._screen, self._clock.get_time())
                    if play.sudoku.is_solved() and play.solved == False:
                        play.solved_graphic(self._screen)
                except:
                    pygame.quit()
                    sys.exit()

            try:
                pygame.display.flip()
            except:
                pygame.quit()
                sys.exit()

    def show_screen(self):
        """
         Show the screen of the game
        """
        self._run()

    def _quit_screen(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def _increase_difficulty(self):
        if self._game_difficulty < 15:
            self._game_difficulty += 1

    def _decrease_difficulty(self):
        if self._game_difficulty > 0:
            self._game_difficulty -= 1

    def _start_screen(self):
        self._current_screen = "start"
        self._run()

    def _sudoku_screen(self):
        self._current_screen = "playSudoku"
        self._run()
