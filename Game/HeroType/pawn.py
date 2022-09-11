from .. import state,pieces

def pawnMoves(turn, player):
    pos = list()
    piece, move = turn.split()
    piece = ('A-' if player == 0 else 'B-') + piece
    for j in range(4,-1,-1):
        for k in range(5):
            if state[player][j][k] == piece:
                pos.extend([j,k])
                break
    if move == 'L' and (pos[1] == 0 or (state[player][pos[0]][pos[1]-1].split('-'))[0] == (piece.split('-'))[0]):
        print("invalid move")
        return False

    elif move == 'R' and (pos[1] == 4 or (state[player][pos[0]][pos[1]+1].split('-'))[0] == (piece.split('-'))[0]):
        print("invalid move")
        return False

    elif move == 'F' and (pos[0] == 0 or (state[player][pos[0]-1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
        print("invalid move")
        return False

    elif move == 'B' and (pos[0] == 4 or (state[player][pos[0]+1][pos[1]].split('-'))[0] == (piece.split('-'))[0]):
        print("invalid move")
        return False

    elif move == 'L':
        state[player][pos[0]][pos[1]] = '-'
        state[1 - player][4 - pos[0]][pos[1]] = '-'
        if state[player][pos[0]][pos[1] - 1] != '-':
            pieces[1 - player].remove(((state[player][pos[0]][pos[1] - 1]).split('-'))[1])
        state[player][pos[0]][pos[1] - 1] = piece
        state[1 - player][4 - pos[0]][pos[1] - 1] = piece

    elif move == 'R':
        state[player][pos[0]][pos[1]] = '-'
        state[1 - player][4 - pos[0]][pos[1]] = '-'
        if state[player][pos[0]][pos[1] + 1] != '-':
            pieces[1 - player].remove(((state[player][pos[0]][pos[1] + 1]).split('-'))[1])
        state[player][pos[0]][pos[1] + 1] = piece
        state[1 - player][4 - pos[0]][pos[1] + 1] = piece

    elif move == 'F':
        state[player][pos[0]][pos[1]] = '-'
        state[1 - player][4 - pos[0]][pos[1]] = '-'
        if state[player][pos[0] - 1][pos[1]] != '-':
            pieces[1 - player].remove(((state[player][pos[0] - 1][pos[1]]).split('-'))[1])
        state[player][pos[0] - 1][pos[1]] = piece
        state[1 - player][5 - pos[0]][pos[1]] = piece

    elif move == 'B':
        state[player][pos[0]][pos[1]] = '-'
        state[1 - player][4 - pos[0]][pos[1]] = '-'
        if state[player][pos[0] + 1][pos[1]] != '-':
            pieces[1 - player].remove(((state[player][pos[0] + 1][pos[1]]).split('-'))[1])
        state[player][pos[0] + 1][pos[1]] = piece
        state[1 - player][3 - pos[0]][pos[1]] = piece

    pos.clear()
    return True