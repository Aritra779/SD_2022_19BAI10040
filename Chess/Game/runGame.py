import typer
from Chess.Game.HeroType.hero1 import hero1Moves
from Chess.Game.HeroType.hero2 import hero2Moves
from Chess.Game.HeroType.hero3 import hero3Moves
from Chess.Game.HeroType.pawn import pawnMoves

from Chess.Game.display import displayBoard
from Chess.Game.sanitize import sanitizeMove
from .. import pieces

def runGame():

    player : int = 0
    # 0 -> A, 1 -> B

    while len(pieces[0]) > 0 and len(pieces[1]) > 0:
        print('Turn for player',('A' if player == 0 else 'B'))
        turn : str = typer.prompt("Enter a valid piece followed by a valid move like P1 L")
        turn = sanitizeMove(turn)
        piece : str = (turn.split())[0]
        if piece.upper() not in pieces[player]:
            print("Invalid move. Piece not present on the board.")
            continue
        
        if piece.upper().startswith('P'):
            if not pawnMoves(turn, player):
                continue

        elif piece.upper() == 'H1':
            if not hero1Moves(turn, player):
                continue

        elif piece.upper() == 'H2':
            if not hero2Moves(turn, player):
                continue

        elif piece.upper() == 'H3':
            if not hero3Moves(turn, player):
                continue

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