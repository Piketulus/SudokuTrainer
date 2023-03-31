import pygame
from .objects import Button

class Start:

    def start(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        startButton = Button(100, 100, 200, 50, "Start", (255, 255, 255), (0, 0, 0), pygame.font.SysFont("comicsans", 40))
        screen = pygame.display.set_mode((400, 600))
        screen.fill((255,192,203))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    startButton.click(pos)

            startButton.draw(screen)
            pygame.display.update()
                
    def showScreen(self):
        self.start()


    def quitScreen(self):
        pygame.quit()

    