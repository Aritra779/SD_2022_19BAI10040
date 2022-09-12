import typer

valid_type : set[str] = {'P1','P2','P3','P4','P5','H1', 'H2', 'H3'}
valid_moves : dict[str,set[str]] = {
  **dict.fromkeys(['P', 'H1'], {'L','R', 'F','B'}), 
  **dict.fromkeys(['H2','H3'], {'LF','FL','RF','FR','LB','BL','RB','BR'})
}

def initialSanitize(player : str) -> str:
    positionList : str = player
    flagged : bool = True
    while flagged:
        if len(positionList.split()) != 5:
            print("Invalid number of positions mentioned")
            positionList = typer.prompt("\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
            continue

        pieceTypes : list[str] = positionList.split()
        
        used_position : bool = False
        entered_piece : set[str] = set()
        invalid_piece : bool = False

        for psTyp in pieceTypes:
            if psTyp in entered_piece:
                used_position = True
                break
            entered_piece.add(psTyp)
            if not invalid_piece and psTyp.upper() not in valid_type:
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
    
    return positionList.upper()




def sanitizeMove(turn : str) -> str:
    turnList : str = turn
    flagged : bool = True

    while flagged:
        if len(turnList.split()) != 2:
            print("Please mention a piece followed by a direction separated by a space")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L.")
            continue

        turnLst : list[str] = turnList.split()
        if turnLst[0].upper() not in valid_type:
            print("Invalid type of piece. Allowed: P H1 H2 H3")
            turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
            continue

        if (turnLst[0].upper()).startswith('P'):
            if turnLst[1].upper() not in valid_moves['P']:
                print("Invalid move for coresponding piece type. Allowed Moves: L R F B")
                turnList = typer.prompt("Enter a valid piece followd by a valid move like P1 L")
                continue

        elif turnLst[0].upper() == 'H1':
            if turnLst[1].upper() not in valid_moves['H1']:
                print("Invalid move for coresponding piece type. Allowed : L R F B")
                turnList = typer.prompt("Enter a valid piece followd by a valid move like H1 L")
                continue

        else:
            if turnLst[1].upper() not in valid_moves[turnLst[0].upper()]:
                print("Invalid move for coresponding piece type. Allowed : LF FL RF FR LB BL RB BR")
                turnList = typer.prompt("Enter a valid piece followd by a valid move like H2 LB")
                continue

        flagged = False

    return turnList.upper()