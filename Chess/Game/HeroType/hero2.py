from Chess.Game.validate import validateH2Move
from ... import positions,pieces,board

def hero2Moves(turn, player):
    piece, move = turn.split()
    piece = ('A-' if player == 0 else 'B-') + piece
    pos = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    if not validateH2Move(move, piece, player):
        return False

    match(move.upper()):
        case 'LF' | 'FL' :
            board[row][col] = '-'
            prevPiece1 = board[row - 1 + adjustment][col - 1 + adjustment]
            prevPiece2 = board[row - 2 + (2 * adjustment)][col - 2 + (2 * adjustment)]
            if prevPiece1 != '-':
                board[row - 1 + adjustment][col - 1 + adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row - 2 + (2 * adjustment)][col - 2 + (2 * adjustment)] = piece
            positions[piece] = [row - 2 + (2 * adjustment), col - 2 + (2 * adjustment)]

        case 'RF' |'FR' :
            board[row][col] = '-'
            prevPiece1 = board[row - 1 + adjustment][col + 1 - adjustment]
            prevPiece2 = board[row - 2 + (2 * adjustment)][col + 2 - (2 * adjustment)]
            if prevPiece1 != '-':
                board[row - 1 + adjustment][col + 1 - adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row - 2 + (2 * adjustment)][col + 2 - (2 * adjustment)] = piece
            positions[piece] = [row - 2 + (2 * adjustment), col + 2 - (2 * adjustment)]

        case 'LB' | 'BL' :
            board[row][col] = '-'
            prevPiece1 = board[row + 1 - adjustment][col - 1 + adjustment]
            prevPiece2 = board[row + 2 - (2 * adjustment)][col - 2 + (2 * adjustment)]
            if prevPiece1 != '-':
                board[row + 1 - adjustment][col - 1 + adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row + 2 - (2 * adjustment)][col - 2 + (2 * adjustment)] = piece
            positions[piece] = [row + 2 - (2 * adjustment), col - 2 + (2 * adjustment)]

        case 'RB' | 'BR' :
            board[row][col] = '-'
            prevPiece1 = board[row + 1 - adjustment][col + 1 - adjustment]
            prevPiece2 = board[row + 2 - (2 * adjustment)][col + 2 - (2 * adjustment)]
            if prevPiece1 != '-':
                board[row + 1 - adjustment][col + 1 - adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row + 2 - (2 * adjustment)][col + 2 - (2 * adjustment)] = piece
            positions[piece] = [row + 2 - (2 * adjustment), col + 2 - (2 * adjustment)]

    pos.clear()
    return True