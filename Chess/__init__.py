board = [['-' for _ in range(5)] for _ in range(5)]

#board is the game board (from playerA's perspective)
#vertical mirror of board is the board from playerB's perspective

pieces = list()
pieces.append(['-' for _ in range(5)])
pieces.append(['-' for _ in range(5)])

#pieces[0] -> all the pieces left on the board for player A
#pieces[1] -> all the pieces left on the board for player B

positions = dict()
#position will hold current position of each of 10 pieces.
