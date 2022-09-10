from cProfile import label
import typer

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
        piece = ('A-' if player == 0 else 'B-') + piece
        for j in range(4,-1,-1):
            for k in range(5):
                if state[player][j][k] == piece:
                    pos.extend([j,k])
                    break
        if move == 'L' and (pos[1] == 0 or (state[player][pos[0]][pos[1]-1].split('-'))[0] == (piece.split('-'))[0]):
            print("invalid move")
            continue
        elif move == 'R' and (pos[1] == 4 or (state[player][pos[0]][pos[1]+1].split('-'))[0] == (piece.split('-'))[0]):
            print("invalid move")
            continue
        elif move == 'F' and (pos[0] == 0 or (state[player][pos[0]-1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
            print("invalid move")
            continue
        elif move == 'B' and (pos[0] == 4 or (state[player][pos[0]+1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
            print("invalid move")
            continue
        elif move == 'L':
            state[player][pos[1]] = '-'
            if state[player][pos[0]][pos[1] - 1] != '-':
                pieces[1 - player].remove(((state[player][pos[0]][pos[1] - 1]).split('-'))[1])
            state[player][pos[0]][pos[1] - 1] = piece
        elif move == 'R':
            state[player][pos[0]][pos[1]] = '-'
            if state[player][pos[0]][pos[1] + 1] != '-':
                pieces[1 - player].remove(((state[player][pos[0]][pos[1] + 1]).split('-'))[1])
            state[player][pos[0]][pos[1] + 1] = piece
        elif move == 'F':
            state[player][pos[0]][pos[1]] = '-'
            if state[player][pos[0] - 1][pos[1]] != '-':
                pieces[1 - player].remove(((state[player][pos[0] - 1][pos[1]]).split('-'))[1])
            state[player][pos[0] - 1][pos[1]] = piece
        elif move == 'B':
            state[player][pos[0]][pos[1]] = '-'
            if state[player][pos[0] + 1][pos[1]] != '-':
                pieces[1 - player].remove(((state[player][pos[0] + 1][pos[1]]).split('-'))[1])
            state[player][pos[0] + 1][pos[1]] = piece
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