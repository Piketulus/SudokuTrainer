import pygame
from services.gameService import GameService
from .button import Button
from .playSudoku import PlaySudoku

class Start:

    def _start(self):
        pygame.init()
        pygame.display.set_caption("Sudoku")
        objects = []
        start_button = Button(100, 100, 200, 50, "Start", (255, 255, 255), (200, 200, 200), (0, 0, 0), pygame.font.SysFont("comicsans", 30), self._start_sudoku)
        objects.append(start_button)
        screen = pygame.display.set_mode((400, 600))
        screen.fill((255,192,203))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            for obj in objects:
                obj.draw(screen)
                obj.process()
            pygame.display.flip()


    def show_screen(self):
        self._start()


    def quit_screen(self):
        pygame.quit()
    

    def _start_sudoku(self):
        gameService = GameService()
        sudoku = gameService.generate_sudoku(9, 0)
        play = PlaySudoku(sudoku)
        play.show_screen()
        self.quit_screen()

    