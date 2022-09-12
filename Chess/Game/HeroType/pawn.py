from Chess.Game.validate import validatePawnMove
from ... import board,pieces, positions

def pawnMoves(turn, player):
    piece, move = turn.split()
    piece = ('A-' if player == 0 else 'B-') + piece
    pos = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    if not validatePawnMove(move, piece, player):
        return False

    match(move.upper()):
        case 'L':  
            board[row][col] = '-'
            prevPiece = board[row][col - 1 + adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row][col - 1 + adjustment] = piece
            positions[piece] = [row, col - 1 + adjustment]

        case 'R':
            board[row][col] = '-'
            prevPiece = board[row][col + 1 - adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row][col + 1 - adjustment] = piece
            positions[piece] = [row, col + 1 - adjustment]

        case 'F':
            board[row][col] = '-'
            prevPiece = board[row - 1 + adjustment][col]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row - 1 + adjustment][col] = piece
            positions[piece] = [row - 1 + adjustment, col]

        case'B':
            board[row][col] = '-'
            prevPiece = board[row + 1 - adjustment][col]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row + 1 - adjustment][col] = piece
            positions[piece] = [row + 1 - adjustment, col]

    pos.clear()
    return True