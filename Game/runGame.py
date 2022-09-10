import typer

from Game.display import displayBoard
#from . import sanitize

def runGame(board):
    boardA = board
    boardB = list()
    for i in range(4,-1,-1):
        boardB.append(boardA[i])

    state = dict()
    state[0] = boardA
    state[1] = boardB

    pieceCount = [5,5]
    pos = []
    while pieceCount[0] > 0 or pieceCount[1] > 0:
        pos.clear()
        for i in [0,1]:
            pos.clear()
            print('turn for player',('A' if i == 0 else 'B'))
            turn = typer.prompt("Enter a valid piece followd by a valid move like P1 L.")
            #turn = sanitize.sanitizeMove(turn)
            piece, move = turn.split()
            piece = ('A-' if i == 0 else 'B-') + piece
            for j in range(4,-1,-1):
                for k in range(5):
                    if state[i][j][k] == piece:
                        pos.extend([j,k])
                        break
            print(state[i][pos[0]-1][pos[1]])
            if move == 'L' and (pos[1] == 0 or (state[i][pos[0]][pos[1]-1].split('-'))[0] == (piece.split('-'))[0]):
                    print("invalid move")
                    continue
            elif move == 'R' and (pos[1] == 4 or (state[i][pos[0]][pos[1]+1].split('-'))[0] == (piece.split('-'))[0]):
                print("invalid move")
                continue
            elif move == 'F' and (pos[0] == 0 or (state[i][pos[0]-1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
                print("invalid move")
                continue
            elif move == 'B' and (pos[0] == 4 or (state[i][pos[0]+1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
                print("invalid move")
                continue
            elif move == 'L':
                state[i][pos[1]] = '-'
                if state[i][pos[0]][pos[1] - 1] != '-':
                    pieceCount[1 - i] -= 1
                state[i][pos[0]][pos[1] - 1] = piece
            elif move == 'R':
                state[i][pos[0]][pos[1]] = '-'
                if state[i][pos[0]][pos[1] + 1] != '-':
                    pieceCount[1 - i] -= 1
                state[i][pos[0]][pos[1] + 1] = piece
            elif move == 'F':
                state[i][pos[0]][pos[1]] = '-'
                if state[i][pos[0] - 1][pos[1]] != '-':
                    pieceCount[1 - i] -= 1
                state[i][pos[0] - 1][pos[1]] = piece
            elif move == 'B':
                state[i][pos[0]][pos[1]] = '-'
                if state[i][pos[0] + 1][pos[1]] != '-':
                    pieceCount[1 - i] -= 1
                state[i][pos[0] + 1][pos[1]] = piece
            print("Board from current players view")
            displayBoard(state[i])
            print("Board from next players view")
            displayBoard(state[i])
    print("Well Now we have a winner")
    if pieceCount[1] == 0:
        print("A won the match")
    else:
        print("B won the match")