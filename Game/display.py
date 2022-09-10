def displayBoard(board):
    print('\nCurrent board configuration:\n')
    for row in board:
        print("|", end = " ")
        for col in row:
            print(col, end = " | ")
        print()