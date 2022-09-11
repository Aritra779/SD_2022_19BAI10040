import typer
valid_type = {'P1','P2','P3','P4','P5','H1', 'H2', 'H3'}
valid_moves = {'L','R', 'F','B'}

def initialSanitize(player):
    positionList = player
    flagged = True
    while flagged:
        if len(positionList.split()) != 5:
            print("Invalid number of positions mentioned")
            positionList = typer.prompt("\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        pieceTypes = positionList.split()
        
        used_position = False
        entered_piece = set()
        invalid_piece = False

        for psTyp in pieceTypes:
            if psTyp in entered_piece:
                used_position = True
                break
            entered_piece.add(psTyp)
            if not invalid_piece and psTyp not in valid_type:
                invalid_piece = True
                break

        if used_position:
            print("You placed two same pieces. Try again.")
            positionList = typer.prompt("\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        if invalid_piece:
            print("Invalid type of piece. Allowed: P H1 H2 H3")
            positionList = typer.prompt("\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
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
        if turnLst[0] not in valid_type:
            print("Invalid type of piece. Allowed: P H1 H2 H3")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue
        
        if turnLst[1] not in valid_moves:
            print("Invalid move. Allowed : L R F B")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue

        flagged = False

    return turnList