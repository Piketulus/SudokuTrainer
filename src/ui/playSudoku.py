from math import sqrt
import pygame
from .button import Button

class PlaySudoku:

    def __init__(self, sudoku):
        self._sudoku = sudoku
        self._objects = []
        self._selected = None
        self._font = pygame.font.SysFont("comicsans", 30)


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
        

    def _play_sudoku(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        screen = pygame.display.set_mode((600, 720))
        screen.fill((255, 255, 255))
        self._draw_lines(screen)
        self._draw_boxes()
        self._draw_numbers()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYUP:
                    if self._selected != None:
                        row = (self._selected.y - 52) // 50
                        col = (self._selected.x - 52) // 50
                        if event.key == pygame.K_1:
                            self._selected.text = "1"
                            self._sudoku.update_grid(row, col, 1)
                        elif event.key == pygame.K_2:
                            self._selected.text = "2"
                            self._sudoku.update_grid(row, col, 2)
                        elif event.key == pygame.K_3:
                            self._selected.text = "3"
                            self._sudoku.update_grid(row, col, 3)
                        elif event.key == pygame.K_4:
                            self._selected.text = "4"
                            self._sudoku.update_grid(row, col, 4)
                        elif event.key == pygame.K_5:
                            self._selected.text = "5"
                            self._sudoku.update_grid(row, col, 5)
                        elif event.key == pygame.K_6:
                            self._selected.text = "6"
                            self._sudoku.update_grid(row, col, 6)
                        elif event.key == pygame.K_7:
                            self._selected.text = "7"
                            self._sudoku.update_grid(row, col, 7)
                        elif event.key == pygame.K_8:
                            self._selected.text = "8"
                            self._sudoku.update_grid(row, col, 8)
                        elif event.key == pygame.K_9:
                            self._selected.text = "9"
                            self._sudoku.update_grid(row, col, 9)
                        elif event.key == pygame.K_BACKSPACE:
                            self._selected.text = ""
                            self._sudoku.update_grid(row, col, 0)
            for obj in self._objects:
                obj.draw(screen)
                obj.process()
            if self._selected != None:
                self._selected.color = (200, 200, 200)
            if self._sudoku.is_solved():
                screen.blit(self.font.render("Solved!", 1, (0, 0, 0)), (250, 600))
            pygame.display.flip()


    def show_screen(self):
        self._play_sudoku()

    
    def quit_screen(self):
        pygame.quit()