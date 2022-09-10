from cProfile import label
import typer
from Game.HeroType.hero1 import hero1Moves
from Game.HeroType.hero2 import hero2Moves
from Game.HeroType.hero3 import hero3Moves
from Game.HeroType.pawn import pawnMoves

from Game.display import displayBoard
from Game.sanitize import sanitizeMove


def runGame(board):
    boardA = board
    boardB = list()
    for i in range(4,-1,-1):
        boardB.append(boardA[i])

    state = dict()
    state[0] = boardA
    state[1] = boardB

    piecesA = set([(piece.split('-'))[1] for piece in board[4]])
    piecesB = set([(piece.split('-'))[1] for piece in board[0]])
    pieces = [piecesA, piecesB]
    pos = []
    player = 0 # 0 -> A, 1 -> B
    while len(pieces[0]) > 0 or len(pieces[1]) > 0:
        pos.clear()
        print('turn for player',('A' if player == 0 else 'B'))
        turn = typer.prompt("Enter a valid piece followd by a valid move like P1 L.")
        turn = sanitizeMove(turn)
        piece, move = turn.split()
        if piece not in pieces[player]:
            print("invalid move. Piece not present.")
            continue
        
        if piece.startswith('P'):
            if not pawnMoves(state, pieces, turn, player):
                continue

        elif piece == 'H1':
            hero1Moves()
        elif piece == 'H2':
            hero2Moves()
        elif piece == 'H3':
            hero3Moves()
        else:
            print("Something went wrong. Try again")
            continue

        print("Board from current players view")
        displayBoard(state[player])
        print("Board from next players view")
        displayBoard(state[1 - player])
        player = 1 - player
    print("Well Now we have a winner")
    if len(pieces[1]) == 0:
        print("A won the match")
    else:
        print("B won the match")