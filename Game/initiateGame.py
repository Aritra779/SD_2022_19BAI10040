from Game.display import displayBoard
from Game.runGame import runGame
from . import state, pieces


def initiateGame(playerA, playerB):
    for i in range(5):
        state[0][0][i] = "B-" + playerB[i]
    for i in range(5):
        state[0][4][i] = "A-" + playerA[i]

    for i in range(4,-1,-1):
        for j in range(5):
            state[1][4-i][j] = state[0][i][j]

    piecesA = set([(piece.split('-'))[1] for piece in state[0][0]])
    piecesB = set([(piece.split('-'))[1] for piece in state[1][0]])
    pieces[0] = piecesA
    pieces[1] = piecesB
    
    displayBoard()
    print("\nThe Game will start now. Happy hunting.\n")

    runGame()