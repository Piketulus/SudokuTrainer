from math import sqrt
import pygame
from .button import Button

class DrawSudoku:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.objects = []
        self.undo_stack = []
        self.selected = None
        self._font = pygame.font.SysFont("comicsans", 30)
        self.solved = False


    def solved_graphic(self, screen):
        #displays the solved screen
        self.selected.color = (255, 255, 255)
        self.selected.draw(screen)
        self.selected = None
        for object in self.objects:
            object.text = ""
            object.draw(screen)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.wait(50)
        self.objects = []
        screen.fill((255, 255, 255))
        screen.blit(self._font.render("Solved!", 1, (0, 255, 0)), (225, 100))
        pygame.display.flip()
        self.solved = True
    

    def _draw_lines(self, screen):
        #draws the lines of the sudoku grid and the 3x3 boxes
        for i in range(self.sudoku.size + 1):
            if i % (int(sqrt(self.sudoku.size))) == 0:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 3)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 3)
            else:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 1)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 1)
    

    def _draw_boxes(self):
        #draws the boxes in the grid that can be clicked on 
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] == 0:
                    usable = True
                    bold = False
                else:
                    usable = False
                    bold = True
                self.objects.append(Button(52 + j * 50, 52 + i * 50, 48, 48, "", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30, bold), self._select, usable))
    

    def _draw_numbers(self):
        #draws the numbers in the grid in the buttons
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] != 0:
                    self.objects[i * self.sudoku.size + j].text = str(self.sudoku.grid[i][j])
    

    def _select(self):
        mousepos = pygame.mouse.get_pos()
        index = ((mousepos[1] - 50) // 50 * self.sudoku.size) + ((mousepos[0] - 50) // 50)
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


    def draw(self, screen):
        screen.fill((255, 255, 255))
        self._draw_lines(screen)
        self._draw_boxes()
        self._draw_numbers()
        undo_button = Button(50, 550, 100, 50, "Undo", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self._undo, True)
        self.objects.append(undo_button)