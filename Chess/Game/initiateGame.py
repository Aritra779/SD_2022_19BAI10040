from Chess.Game.display import displayBoard
from Chess.Game.runGame import runGame
from .. import board, pieces, positions


def initiateGame(playerA : list, playerB : list) -> None:
    for i in range(5):
        board[0][4 - i] = "B-" + playerB[i]
        positions[board[0][4 - i]] = [0,4 - i]
    for i in range(5):
        board[4][i] = "A-" + playerA[i]
        positions[board[4][i]] = [4,i]


    piecesA : set[str] = set([(piece.split('-'))[1] for piece in board[4]])
    piecesB : set[str] = set([(piece.split('-'))[1] for piece in board[0]])
    pieces[0] = piecesA
    pieces[1] = piecesB
    
    displayBoard()
    print("\nThe Game will start now. Happy hunting.\n")

    runGame()