state = list()
pieces = list()

state.append([['-' for _ in range(5)] for _ in range(5)])
state.append([['-' for _ in range(5)] for _ in range(5)])

#state[0] -> current state of the board from playerA perspective
#state[1] -> current state of the board from playerB perspective
#state[0] and state[1] are just vertical mirror images of each other

pieces.append(['-' for _ in range(5)])
pieces.append(['-' for _ in range(5)])

#pieces[0] -> all the pieces left on the board for player A
#pieces[1] -> all the pieces left on the board for player B