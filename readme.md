This is a CLI based chess like game.

Description about the game will be here and the changelog with each version will be under [*CHANGELOG.md*](./CHANGELOG.md)

# pre-requisites
* [python (3.10)](https://www.python.org/)
* [poetry](https://python-poetry.org/)
* [typer](https://typer.tiangolo.com/)
# How to use

To get a local copy up and running follow these simple example steps.

1. Clone the repo
   ```sh
   git clone https://github.com/Aritra779/SD_19BAI10040.git
   ```
2. Install required packages/Libraries
    - with poetry
        ```sh
        poetry install
        ```
    - with pip
        ```sh
        pip install requirements.txt
        ```
3. run
    ```
    poetry run chess
    ```
inside of the folder where the project lies

# Rules of the game
* Each player (A and B) has to choose 5 pieces to begin their game with. So far available options are P1 P2 P3 P4 P5 and H1.
* Once this is done the game will start.
* It's a turn based game starting with player a
* Any `P` type pieces can move 1 cell `left`, `right`, `forward` or `backward` if there's no friendly piece in the destination cell
* `H1` can move 2 cells `left`, `right`, `forward` or `backward` if there's no friendly piece in the destination cell
* If the destination cell is occupied by opponent piece then moving there will eliminate the opponent piece from the game.
* A `H1` piece can take out 2 pieces at once if they are in its path. (only 2 cell movement).
* Game will be over once all the pieces of a player are eliminated from the board.
* *keep in mind you can't cross a friendly piece i.e. we don't betray our friends. :)* 
# Currently supported Pieces:
* P -> pawn
* H1 -> hero1

# Currently supported Moves:
* L -> move 1 cell left for pawn or 2 cells left for hero1
* R -> move 1 cell right for pawn or 2 cells right for hero1
* F -> move 1 cell forward for pawn or 2 cells forward for hero1
* B -> move 1 cell backward for pawn or 2 cells forward for hero1

*invalid moves are checked (and sanitized) first before proceeding with the core task.*

# sneak peek

![initial Game][initialize_ss]
![during Game][rungame_ss]
![validity Check][validity_ss]
# Roadmap

- [ ] More pieces type
- [ ] Move moves type
- [ ] testing 


[initialize_ss]: images/initialScreen.png
[rungame_ss]: images/rungame.png
[validity_ss]: images/validityCheck.png