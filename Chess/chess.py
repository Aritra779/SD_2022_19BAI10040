import typer

from Chess.Game.initiateGame import initiateGame
from Chess.Game.sanitize import initialSanitize

def main() -> None:

    print("\nWelcome to the world of wonderful world of modified chess. Let's get started.")
    playerA : str = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
    playerA = initialSanitize(playerA)
    
    playerB : str = typer.prompt("\n\nFor Player B.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
    playerB = initialSanitize(playerB)

    initiateGame(playerA.split(), playerB.split())
    
if __name__ == "__main__":
    typer.run(main)

def run() -> None:
    typer.run(main)

    
