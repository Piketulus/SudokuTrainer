from math import sqrt
import pygame
import datetime
from .button import Button


class DrawSudoku:

    # draws and creates the elements of the sudoku playing screen

    def __init__(self, sudoku, start_screen, save_time_popup, difficulty):
        self.sudoku = sudoku
        self.objects = []
        self.undo_stack = []
        self.selected = None
        self._font = pygame.font.SysFont("comicsans", 30)
        self.solved = False
        self._minutes = 0
        self._seconds = 0
        self._milliseconds = 0
        self._start_screen = start_screen
        self._save_time_popup = save_time_popup
        self._difficulty = difficulty

    def solved_graphic(self, screen):
        # displays the solved screen
        self.selected.color = (255, 255, 255)
        self.selected.draw(screen)
        self.selected = None
        
        for object in self.objects[:-1]:
            object.text = ""
            object.draw(screen)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.wait(50)
        
        self.objects = self.objects[-1:]
        screen.fill((255, 192, 203), (0, 0, 550, 545))

        if self._difficulty == 15:
            screen.blit(pygame.image.load("dokumentaatio/kuvat/secret.jpg"), (125, 50))

        screen.blit(pygame.font.SysFont("comicsans", 60).render("Solved!", 1, (0, 200, 0)), (170, 200))
        self.objects.append(Button(50, 550, 150, 50, "Save Time", (255, 255, 255), (200, 200, 200), (
            0, 0, 0), pygame.font.SysFont("comicsans", 30), self._save_time, True))
        
        pygame.display.flip()
        self.solved = True

    def _save_time(self):
        date = datetime.datetime.now()
        time = self._minutes * 60 + self._seconds + self._milliseconds / 1000
        self._save_time_popup(time, self._difficulty, date)

    def _draw_lines(self, screen):
        # draws the lines of the sudoku grid and the 3x3 boxes
        for i in range(self.sudoku.size + 1):
            if i % (int(sqrt(self.sudoku.size))) == 0:
                pygame.draw.line(screen, (0, 0, 0),
                                 (50 + i * 50, 50), (50 + i * 50, 500), 3)
                pygame.draw.line(screen, (0, 0, 0),
                                 (50, 50 + i * 50), (500, 50 + i * 50), 3)
            else:
                pygame.draw.line(screen, (0, 0, 0),
                                 (50 + i * 50, 50), (50 + i * 50, 500), 1)
                pygame.draw.line(screen, (0, 0, 0),
                                 (50, 50 + i * 50), (500, 50 + i * 50), 1)

    def _draw_boxes(self):
        # draws the boxes in the grid that can be clicked on
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] == 0:
                    usable = True
                    bold = False
                else:
                    usable = False
                    bold = True
                self.objects.append(Button(52 + j * 50, 52 + i * 50, 48, 48, "", (255, 255, 255), (200,
                                    200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30, bold), self._select, usable))

    def _draw_numbers(self):
        # draws the numbers in the grid in the buttons
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] != 0:
                    self.objects[i * self.sudoku.size +
                                 j].text = str(self.sudoku.grid[i][j])

    def _select(self):
        mousepos = pygame.mouse.get_pos()
        index = ((mousepos[1] - 50) // 50 *
                 self.sudoku.size) + ((mousepos[0] - 50) // 50)
        self.selected = self.objects[index]

    def _undo(self):
        if len(self.undo_stack) > 0:
            box, number, row, col = self.undo_stack.pop()
            box.text = number
            if number == "":
                number = 0
            else:
                number = int(number)
            self.sudoku.update_grid(row, col, number)

    def update_time(self, screen, time):
        # updates the time on the screen
        if self._milliseconds > 1000:
            self._seconds += 1
            self._milliseconds -= 1000
        if self._seconds > 60:
            self._minutes += 1
            self._seconds -= 60
        self._milliseconds += time
        secs = self._seconds
        if secs < 10:
            secs = "0" + str(secs)
        screen.fill((255, 192, 203), (190, 620, 360, 40))
        time_text = self._font.render(
            f"Time: {self._minutes}:{secs}", 1, (0, 0, 0))
        screen.blit(time_text, (190, 620))

    def draw(self, screen):
        # draws the sudoku grid and the buttons onto the given screen, called from outside the class
        screen.fill((255, 192, 203))
        screen.fill((255, 255, 255), (50, 50, 451, 451))
        self._draw_lines(screen)
        self._draw_boxes()
        self._draw_numbers()
        self.objects.append(Button(50, 550, 100, 50, "Undo", (255, 255, 255), (200, 200, 200), (
            0, 0, 0), pygame.font.SysFont("comicsans", 30), self._undo, True))
        self.objects.append(Button(400, 550, 100, 50, "Quit", (255, 255, 255), (
            200, 200, 200), (0, 0, 0), self._font, self._start_screen, True))
