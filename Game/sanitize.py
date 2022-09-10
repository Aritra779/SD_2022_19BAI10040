import typer
valid_type = {'P','H1', 'H2', 'H3'}
valid_pos = {1,2,3,4,5}
valid_moves = {'L','R', 'F','B'}

def initialSanitize(player):
    positionList = player
    flagged = True
    while flagged:
        if len(positionList.split()) != 5:
            print("Invalid number of positions mentioned")
            positionList = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        positions = positionList.split()
        
        invalid_piece = False
        for pos in positions:
            if not invalid_piece and pos[0] not in valid_type:
                invalid_piece = True
                break
        if invalid_piece:
            print("Invalid type of piece. Allowed: P H1 H2 H3")
            positionList = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        invalid_piece = False
        used_position = False
        entered_pos = set()
        for pos in positions:
            if pos[1] in entered_pos:
                used_position = True
                break
            entered_pos.add(pos[1])
            if not invalid_piece and (int(pos[1]) not in valid_pos):
                invalid_piece = True
                break
        if used_position:
            print("Can't have two pieces in the same position.")
            positionList = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue
        if invalid_piece:
            print("Invalid position. Allowed: 1 2 3 4 5")
            positionList = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        invalid_piece = False
        flagged = False
    return positionList.split()

def sanitizeMove(turn):
    turnList = turn
    flagged = True
    while flagged:
        if len(turnList.split()) != 2:
            print("Please mention a piece followed by a direction separated by a space")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L.")
            continue

        turnLst = turnList.split()
        if turnLst[0][0] not in valid_type:
            print("Invalid type of piece. Allowed: P H1 H2 H3")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue

        if (int(turnLst[0][1]) not in valid_pos):
            print("Invalid position. Allowed: 1 2 3 4 5")
            positionList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue
        
        if turnLst[1] not in valid_moves:
            print("Invalid move. Allowed : L R F B")
            positionList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue

        flagged = False

    return turnList