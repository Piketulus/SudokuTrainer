#main
from entities.sudoku import Sudoku
from services.gameService import GameService

if __name__ == "__main__":
    sudoku = Sudoku(9, 0)
    gameService = GameService()
    gameService.createGame(sudoku)
    print(sudoku)
    gameService.solve(sudoku)
    print(sudoku)