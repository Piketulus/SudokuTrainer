from math import sqrt
import pygame
from .button import Button

class PlaySudoku:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.objects = []
        self.selected = None
        self.font = pygame.font.SysFont("comicsans", 30)


    def drawLines(self, screen):
        #draws the lines of the sudoku grid and the 3x3 boxes
        for i in range(self.sudoku.size + 1):
            if i % (int(sqrt(self.sudoku.size))) == 0:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 3)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 3)
            else:
                pygame.draw.line(screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 1)
                pygame.draw.line(screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 1)
    

    def drawBoxes(self):
        #draws the boxes in the grid that can be clicked on 
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] == 0:
                    usable = True
                    bold = False
                else:
                    usable = False
                    bold = True
                self.objects.append(Button(52 + j * 50, 52 + i * 50, 48, 48, "", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30, bold), self.select, usable))
    

    def drawNumbers(self, screen):
        #draws the numbers in the grid in the buttons
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] != 0:
                    self.objects[i * self.sudoku.size + j].text = str(self.sudoku.grid[i][j])
    

    def select(self):
        mousepos = pygame.mouse.get_pos()
        self.selected = self.objects[((mousepos[1] - 50) // 50 * self.sudoku.size) + ((mousepos[0] - 50) // 50)]
        

    def playSudoku(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        screen = pygame.display.set_mode((600, 720))
        screen.fill((255, 255, 255))
        self.drawLines(screen)
        self.drawBoxes()
        self.drawNumbers(screen)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYUP:
                    if self.selected != None:
                        row = (self.selected.y - 52) // 50
                        col = (self.selected.x - 52) // 50
                        if event.key == pygame.K_1:
                            self.selected.text = "1"
                            self.sudoku.updateGrid(row, col, 1)
                        elif event.key == pygame.K_2:
                            self.selected.text = "2"
                            self.sudoku.updateGrid(row, col, 2)
                        elif event.key == pygame.K_3:
                            self.selected.text = "3"
                            self.sudoku.updateGrid(row, col, 3)
                        elif event.key == pygame.K_4:
                            self.selected.text = "4"
                            self.sudoku.updateGrid(row, col, 4)
                        elif event.key == pygame.K_5:
                            self.selected.text = "5"
                            self.sudoku.updateGrid(row, col, 5)
                        elif event.key == pygame.K_6:
                            self.selected.text = "6"
                            self.sudoku.updateGrid(row, col, 6)
                        elif event.key == pygame.K_7:
                            self.selected.text = "7"
                            self.sudoku.updateGrid(row, col, 7)
                        elif event.key == pygame.K_8:
                            self.selected.text = "8"
                            self.sudoku.updateGrid(row, col, 8)
                        elif event.key == pygame.K_9:
                            self.selected.text = "9"
                            self.sudoku.updateGrid(row, col, 9)
                        elif event.key == pygame.K_BACKSPACE:
                            self.selected.text = ""
                            self.sudoku.updateGrid(row, col, 0)
            for obj in self.objects:
                obj.draw(screen)
                obj.process()
            if self.selected != None:
                self.selected.color = (200, 200, 200)
            if self.sudoku.isSolved():
                screen.blit(self.font.render("Solved!", 1, (0, 0, 0)), (250, 600))
            pygame.display.flip()


    def showScreen(self):
        self.playSudoku()

    
    def quitScreen(self):
        pygame.quit()