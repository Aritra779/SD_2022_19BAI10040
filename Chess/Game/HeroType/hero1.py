from Chess.Game.validate import validateH1Move
from ... import positions,pieces,board

def hero1Moves(turn : str, player : int) -> bool:
    piece, move = turn.split()
    piece = ('A-' if player == 0 else 'B-') + piece
    pos : list[int] = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    if not validateH1Move(move, piece, player):
        return False

    match(move.upper()):
        case 'L':  
            board[row][col] = '-'
            prevPiece1 = board[row][col - 1 + adjustment]
            prevPiece2 = board[row][col - 2 + (2 * adjustment)]
            if prevPiece1 != '-':
                board[row][col - 1 + adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row][col - 2 + (2 * adjustment)] = piece
            positions[piece] = [row, col - 2 + (2 * adjustment)]

        case 'R':
            board[row][col] = '-'
            prevPiece1 = board[row][col + 1 - adjustment]
            prevPiece2 = board[row][col + 2 - (2 * adjustment)]
            if prevPiece1 != '-':
                board[row][col + 1 - adjustment] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row][col + 2 - (2 * adjustment)] = piece
            positions[piece] = [row, col + 2 - (2 * adjustment)]

        case 'F':
            board[row][col] = '-'
            prevPiece1 = board[row - 1 + adjustment][col]
            prevPiece2 = board[row - 2 + (2 * adjustment)][col]
            if prevPiece1 != '-':
                board[row - 1 + adjustment][col] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row - 2 + (2 * adjustment)][col] = piece
            positions[piece] = [row - 2 + (2 * adjustment), col]

        case'B':
            board[row][col] = '-'
            prevPiece1 = board[row + 1 - adjustment][col]
            prevPiece2 = board[row + 2 - (2 * adjustment)][col]
            if prevPiece1 != '-':
                board[row + 1 - adjustment][col] = '-'
                pieces[1 - player].remove((prevPiece1.split('-'))[1])
                print(prevPiece1, "is eliminated.")
                positions.pop(prevPiece1)
            if prevPiece2 != '-':
                pieces[1 - player].remove((prevPiece2.split('-'))[1])
                print(prevPiece2, "is eliminated.")
                positions.pop(prevPiece2)
            board[row + 2 - (2 * adjustment)][col] = piece
            positions[piece] = [row + 2 - (2 * adjustment), col]

    pos.clear()
    return True