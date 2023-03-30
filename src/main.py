#main
from entities.sudoku import Sudoku
from services.gameService import GameService
import time
import signal

def handler(signum, frame):
    raise Exception('Action took too much time')

if __name__ == "__main__":
    start = time.time()
    sudoku = Sudoku(9, 0)
    gameService = GameService()
    done = False
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)
    while not done:
        try:
            done = True
            gameService.createGame(sudoku)
        except:
            done = False
            signal.alarm(5)
    print(sudoku)
    count = 0
    for i in range(sudoku.size):
        for j in range(sudoku.size):
            if sudoku.grid[i][j] != 0:
                count += 1
    print("Number of numbers in the grid: " + str(count))
    #gameService.solve(sudoku)
    #print(sudoku)
    end = time.time()
    print("time:", end-start, "s")