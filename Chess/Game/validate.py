from .. import board, positions

def validatePawnMove(move, piece, player):
    pos = positions[piece]
    row, col = pos
    adjustment1 = 4 if player == 0 else 0
    adjustment2 = 2 if player == 1 else 0

    if move == 'L' and (col == (4 - adjustment1) or (board[row][col - 1 + adjustment2].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move == 'R' and (col == adjustment1 or (board[row][col + 1 - adjustment2].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move == 'F' and (row == (4 - adjustment1) or (board[row - 1 + adjustment2][col].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move == 'B' and (row == adjustment1 or (board[row + 1 - adjustment2][col].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    return True




def validateH1Moves(move, piece, player):
    pos = positions[piece]
    row, col = pos
    adjustment2 = 2 if player == 1 else 0

    match(move):
        case 'L':
            if (player == 0 and col < 2) or (player == 1 and col > 2):
                print("Out of bound move.")
                return False
            prev1Type = board[row][col - 1 + adjustment2].split('-')[0]
            prev2Type = board[row][col - 2 + (2 * adjustment2)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'R':
            if (player == 0 and col > 2) or (player == 1 and col < 2):
                print("Out of bound move.")
                return False
            prev1Type = board[row][col + 1 - adjustment2].split('-')[0]
            prev2Type = board[row][col + 2 - (2 * adjustment2)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

        case 'F':
            if (player == 0 and row < 2) or (player == 1 and row > 2):
                print("Out of bound move")
                return False
            prev1Type = board[row - 1 + adjustment2][col].split('-')[0]
            prev2Type = board[row - 2 + (2 * adjustment2)][col].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'B':
            if (player == 0 and row > 2) or (player == 1 and row < 2):
                print("Out of bound move")
                return False
            prev1Type = board[row + 1 - adjustment2][col].split('-')[0]
            prev2Type = board[row + 2 - (2 * adjustment2)][col].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

    return True