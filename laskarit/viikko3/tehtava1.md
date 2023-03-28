```mermaid
 classDiagram
      Game "1" -- "2-8" Player
      Game "1" -- "1" GameBoard
      Player "1" -- "1" PlayerPiece
      GameBoard "1" -- "40" BoardTile
      PlayerPiece "1" -- "1" BoardTile
      
      
      class Game{
      }
      class Dice{
      }
      class Player{
      }
      class PlayerPiece{
      }
      class GameBoard{
      }
      class BoardTile{
      }
```
