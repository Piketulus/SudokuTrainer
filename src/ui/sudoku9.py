import pygame
from .button import Button

class Sudoku9:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.objects = []
        self.selected = None
        self.screen = pygame.display.set_mode((500, 600))
        self.screen.fill((255, 255, 255))
        self.font = pygame.font.SysFont("comicsans", 30)


    def drawLines(self):
        #draws the lines of the sudoku grid and the 3x3 boxes
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 3)
                pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 3)
            else:
                pygame.draw.line(self.screen, (0, 0, 0), (50 + i * 50, 50), (50 + i * 50, 500), 1)
                pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + i * 50), (500, 50 + i * 50), 1)
    

    def drawBoxes(self):
        #draws the boxes in the grid that can be clicked on 
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                self.objects.append(Button(50 + j * 50, 50 + i * 50, 50, 50, "", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self.select()))
        
    
    def drawNumbers(self):
        #draws the numbers in the grid in the buttons
        for i in range(self.sudoku.size):
            for j in range(self.sudoku.size):
                if self.sudoku.grid[i][j] != 0:
                    self.objects[i * self.sudoku.size + j].text = str(self.sudoku.grid[i][j])
                    self.objects[i * self.sudoku.size + j].draw(self.screen)


    def select(self):
        mousepos = pygame.mouse.get_pos()
        self.selected = self.objects[mousepos[0] // 50 * self.sudoku.size + mousepos[0] // 50]


    def sudoku9(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        self.drawLines()
        self.drawBoxes()
        self.drawNumbers()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            for obj in self.objects:
                obj.process()
                obj.draw(self.screen)
            pygame.display.flip()


    def showScreen(self):
        self.sudoku9()

    
    def quitScreen(self):
        pygame.quit()