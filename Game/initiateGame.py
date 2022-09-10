from . import display as disp
from . import runGame

def initiateGame(playerA, playerB):
    board = [['-' for _ in range(5)] for _ in range(5)]
    for i in range(5):
        board[0][i] = "B-" + playerB[i]
    for i in range(5):
        board[4][i] = "A-" + playerA[i]
    disp.displayBoard(board)
    print("The Game will start now.")

    runGame.runGame(board)
