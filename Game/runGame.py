import typer
from Game.HeroType.hero1 import hero1Moves
from Game.HeroType.hero2 import hero2Moves
from Game.HeroType.hero3 import hero3Moves
from Game.HeroType.pawn import pawnMoves

from Game.display import displayBoard
from Game.sanitize import sanitizeMove
from . import state, pieces

def runGame():

    player = 0
    # 0 -> A, 1 -> B

    while len(pieces[0]) > 0 or len(pieces[1]) > 0:
        print('turn for player',('A' if player == 0 else 'B'))
        turn = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
        turn = sanitizeMove(turn)
        piece, move = turn.split()
        if piece not in pieces[player]:
            print("invalid move. Piece not present on the board.")
            continue
        
        if piece.startswith('P'):
            if not pawnMoves(turn, player):
                continue

        elif piece == 'H1':
            hero1Moves(turn, player)
        elif piece == 'H2':
            hero2Moves(turn, player)
        elif piece == 'H3':
            hero3Moves(turn, player)
        else:
            print("Something went wrong. Try again")
            continue

        displayBoard()
        player = 1 - player
    print("Well Now we have a winner")
    if len(pieces[1]) == 0:
        print("A won the match")
    else:
        print("B won the match")