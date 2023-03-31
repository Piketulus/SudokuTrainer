import pygame
from .button import Button

class Start:

    def start(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        objects = []
        startButton = Button(100, 100, 200, 50, "Start", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self.quitScreen)
        objects.append(startButton)
        screen = pygame.display.set_mode((400, 600))
        screen.fill((255,192,203))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            for obj in objects:
                obj.process()
                obj.draw(screen)
            pygame.display.flip()
                
    def showScreen(self):
        self.start()


    def quitScreen(self):
        pygame.quit()

    