

from . import state

def displayBoard():
    print('\nCurrent board configuration:\n')
    print("Player-A".center(36), end = "\t\t\t")
    print("Player-B".center(36))
    print("(viewpoint)".center(36), end = "\t\t\t")
    print("(viewpoint)".center(36))
    print()

    for i in range(5):
        print("|", end = " ")
        for j in range(5):
            print(state[0][i][j].center(4), end = " | ")
        print("\t\t\t|", end = " ")
        for j in range(5):
            print(state[1][i][j].center(4), end = " | ")
        print()