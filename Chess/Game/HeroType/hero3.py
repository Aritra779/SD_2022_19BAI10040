from typing import List
from Chess.Game.validate import validateH3Move
from ... import positions,pieces,board

def hero3Moves(turn : List, player : int) -> bool:
    piece, move = turn.split()
    piece = ('A-' if player == 0 else 'B-') + piece
    pos : list[int] = positions[piece]
    row, col = pos
    adjustment = 2 if player == 1 else 0

    if not validateH3Move(move, piece, player):
        return False

    match(move.upper()):
        case 'LF' :
            board[row][col] = '-'
            prevPiece = board[row - 1 + adjustment][col - 2 + (2 * adjustment)]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row - 1 + adjustment][col - 2 + (2 * adjustment)] = piece
            positions[piece] = [row - 1 + adjustment, col - 2 + (2 * adjustment)]

        case 'FL' :
            board[row][col] = '-'
            prevPiece = board[row - 2 + (2 * adjustment)][col - 1 + adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row - 2 + (2 * adjustment)][col - 1 + adjustment] = piece
            positions[piece] = [row - 2 + (2 * adjustment), col - 1 + adjustment]

        case 'RF' :
            board[row][col] = '-'
            prevPiece = board[row - 1 + adjustment][col + 2 - (2 * adjustment)]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row - 1 + adjustment][col + 2 - (2 * adjustment)] = piece
            positions[piece] = [row - 1 + adjustment, col + 2 - (2 * adjustment)]

        case 'FR' :
            board[row][col] = '-'
            prevPiece = board[row - 2 + (2 * adjustment)][col + 1 - adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row - 2 + (2 * adjustment)][col + 1 - adjustment] = piece
            positions[piece] = [row - 2 + (2 * adjustment), col + 1 - adjustment]

        case 'LB' :
            board[row][col] = '-'
            prevPiece = board[row + 1 - adjustment][col - 2 + (2 * adjustment)]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row + 1 - adjustment][col - 2 + (2 * adjustment)] = piece
            positions[piece] = [row + 1 - adjustment, col - 2 + (2 * adjustment)]

        case 'BL' :
            board[row][col] = '-'
            prevPiece = board[row + 2 - (2 * adjustment)][col - 1 + adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row + 2 - (2 * adjustment)][col - 1 + adjustment] = piece
            positions[piece] = [row + 2 - (2 * adjustment), col - 1 + adjustment]

        case 'RB' :
            board[row][col] = '-'
            prevPiece = board[row + 1 - adjustment][col + 2 - (2 * adjustment)]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row + 1 - adjustment][col + 2 - (2 * adjustment)] = piece
            positions[piece] = [row + 1 - adjustment, col + 2 - (2 * adjustment)]

        case 'BR' :
            board[row][col] = '-'
            prevPiece = board[row + 2 - (2 * adjustment)][col + 1 - adjustment]
            if prevPiece != '-':
                pieces[1 - player].remove((prevPiece.split('-'))[1])
                print(prevPiece, "is eliminated.")
                positions.pop(prevPiece)
            board[row + 2 - (2 * adjustment)][col + 1 - adjustment] = piece
            positions[piece] = [row + 2 - (2 * adjustment), col + 1 - adjustment]

    pos.clear()
    return True