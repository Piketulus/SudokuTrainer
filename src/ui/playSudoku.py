from math import sqrt
import pygame
from .button import Button

class PlaySudoku:

    def __init__(self, sudoku):
        self._sudoku = sudoku
        self._objects = []
        self._selected = None


    def _draw_lines(self, screen):
        #draws the lines of the sudoku grid and the 3x3 boxes
        for i in range(self._sudoku.size + 1):
            if i % (int(sqrt(self._sudoku.size))) == 0:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 3)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 3)
            else:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 1)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 1)
    

    def _draw_boxes(self):
        #draws the boxes in the grid that can be clicked on 
        for i in range(self._sudoku.size):
            for j in range(self._sudoku.size):
                if self._sudoku.grid[i][j] == 0:
                    usable = True
                    bold = False
                else:
                    usable = False
                    bold = True
                self._objects.append(Button(52 + j * 50, 52 + i * 50, 48, 48, "", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30, bold), self._select, usable))
    

    def _draw_numbers(self):
        #draws the numbers in the grid in the buttons
        for i in range(self._sudoku.size):
            for j in range(self._sudoku.size):
                if self._sudoku.grid[i][j] != 0:
                    self._objects[i * self._sudoku.size + j].text = str(self._sudoku.grid[i][j])
    

    def _select(self):
        mousepos = pygame.mouse.get_pos()
        self._selected = self._objects[((mousepos[1] - 50) // 50 * self._sudoku.size) + ((mousepos[0] - 50) // 50)]
        

    def draw(self, screen):
        screen.fill((255, 255, 255))
        self._draw_lines(screen)
        self._draw_boxes()
        self._draw_numbers()