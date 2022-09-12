from .. import board, positions

def validatePawnMove(move, piece, player):
    pos = positions[piece]
    row, col = pos
    adjustment1 = 4 if player == 0 else 0
    adjustment2 = 2 if player == 1 else 0

    if move.upper() == 'L' and (col == (4 - adjustment1) or (board[row][col - 1 + adjustment2].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move.upper() == 'R' and (col == adjustment1 or (board[row][col + 1 - adjustment2].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move.upper() == 'F' and (row == (4 - adjustment1) or (board[row - 1 + adjustment2][col].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    elif move.upper() == 'B' and (row == adjustment1 or (board[row + 1 - adjustment2][col].split('-'))[0] == (piece.split('-'))[0]):
        print("Invalid move. Either out of bound or attacking a friendly character.")
        return False

    return True




def validateH1Move(move, piece, player):
    pos = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    match(move):
        case 'L' | 'l':
            if (player == 0 and col < 2) or (player == 1 and col > 2):
                print("Out of bound move.")
                return False
            prev1Type = board[row][col - 1 + adjustment].split('-')[0]
            prev2Type = board[row][col - 2 + (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'R' | 'r':
            if (player == 0 and col > 2) or (player == 1 and col < 2):
                print("Out of bound move.")
                return False
            prev1Type = board[row][col + 1 - adjustment].split('-')[0]
            prev2Type = board[row][col + 2 - (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

        case 'F' | 'f':
            if (player == 0 and row < 2) or (player == 1 and row > 2):
                print("Out of bound move")
                return False
            prev1Type = board[row - 1 + adjustment][col].split('-')[0]
            prev2Type = board[row - 2 + (2 * adjustment)][col].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'B' | 'b':
            if (player == 0 and row > 2) or (player == 1 and row < 2):
                print("Out of bound move")
                return False
            prev1Type = board[row + 1 - adjustment][col].split('-')[0]
            prev2Type = board[row + 2 - (2 * adjustment)][col].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

    return True




def validateH2Move(move, piece, player):
    pos = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    match(move.upper()):
        case 'LF' | 'FL':
            if (player == 0 and (col < 2 or row < 2)) or (player == 1 and (col > 2 or row > 2)):
                print("Out of bound move.")
                return False
            prev1Type = board[row - 1 + adjustment][col - 1 + adjustment].split('-')[0]
            prev2Type = board[row - 2 + (2 * adjustment)][col - 2 + (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'RF' | 'FR':
            if (player == 0 and (col > 2 or row < 2)) or (player == 1 and (col < 2 or row > 2)):
                print("Out of bound move.")
                return False
            prev1Type = board[row - 1 + adjustment][col + 1 - adjustment].split('-')[0]
            prev2Type = board[row - 2 + (2 * adjustment)][col + 2 - (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

        case 'LB' | 'BL':
            if (player == 0 and (col < 2 or row > 2)) or (player == 1 and (col > 2 or row < 2)):
                print("Out of bound move")
                return False
            prev1Type = board[row + 1 - adjustment][col - 1 + adjustment].split('-')[0]
            prev2Type = board[row + 2 - (2 * adjustment)][col - 2 + (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False
        
        case 'RB' | 'BR':
            if (player == 0 and (col > 2 or row > 2)) or (player == 1 and (col < 2 or row < 2)):
                print("Out of bound move")
                return False
            prev1Type = board[row + 1 - adjustment][col + 1 - adjustment].split('-')[0]
            prev2Type = board[row + 2 - (2 * adjustment)][col + 2 - (2 * adjustment)].split('-')[0]
            pieceTeam = piece.split('-')[0]
            if prev1Type == pieceTeam or prev2Type == pieceTeam:
                print("Can't attack friendly piece. Betrayal!! We don't do that here.")
                return False

    return True