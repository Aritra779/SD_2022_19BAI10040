import typer
from Game.initiateGame import initiateGame
import Game

def main():
    print("Welcome to the world of wonderful world of modified chess. Let's get started.")
    playerA = "P1 P2 P3 P4 P5"
    #playerA = typer.prompt("\n\nFor Player A.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")
    playerB = "P1 P2 P3 P4 P5"
    #playerB = typer.prompt("\n\nFor Player B.\nEnter the pieces positioned from left to right(separated by a space)\nSample:P1 P3 P4 P2 P5\nEnter your pieces position")


    initiateGame(playerA.split(), playerB.split())
    
    

if __name__ == "__main__":
    typer.run(main)
