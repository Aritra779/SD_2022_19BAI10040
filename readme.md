# Alternate chess

This is a CLI based chess like game.

Description about the game will be here and the changelog with each version will be under [*CHANGELOG.md*](./changelog.md)

## pre-requisites

* [python (3.10)](https://www.python.org/)
* [poetry](https://python-poetry.org/)
* [typer](https://typer.tiangolo.com/)

## How to use

To get a local copy up and running follow these simple example steps.

1. Clone the repo

   ```sh
   git clone https://github.com/Aritra779/SD_19BAI10040.git
   ```

2. Install required packages/Libraries
    * with poetry

        ```sh
        poetry install
        ```

    * with pip

        ```sh
        pip install requirements.txt
        ```

3. run

    ```sh
    poetry run chess
    ```

inside of the folder where the project lies

## Rules of the game

* Each player (A and B) has to choose 5 pieces to begin their game with. So far available options are P1 P2 P3 P4 P5 and H1.
* Once this is done the game will start.
* It's a turn based game starting with player a
* Any `P` type pieces can move 1 cell `left`, `right`, `forward` or `backward` if there's no friendly piece in the destination cell
* `H1` can move 2 cells `left`, `right`, `forward` or `backward` if there's no friendly piece in the path
* `H2` can move 2 cells diagonally in any direction if there's no friendly piece in its path.
* `H3` can move in a `2-and-a-half` manner i.e., 2 cells in one direction and 1 cell in another orthogonal direction.
* If the destination cell is occupied by opponent piece then moving there will eliminate the opponent piece from the game.
* A `H1` or `H2` piece can take out all (maximum 2) pieces in its path unless there's a friendly piece in its path.
* A `H3` piece can take out only one opponent piece at a time.
* Game will be over once all the pieces of a player are eliminated from the board.
* *keep in mind you can't cross a friendly piece i.e. we don't betray our friends. :)*

## Currently supported Pieces

* P -> pawn
* H1 -> hero1
* H2 -> hero2
* H3 -> hero3

## Currently supported Moves

* For Pawn
  * L -> move 1 cell left
  * R -> move 1 cell right
  * F -> move 1 cell forward
  * B -> move 1 cell backward
* For Hero1
  * L -> move 2 cells left
  * R -> move 2 cells right
  * F -> move 2 cells forward
  * B -> move 2 cells backward
* For Hero2
  * LF or FL -> move 2 cells diagonally towards left front
  * RF or FR -> move 2 cells diagonally towards right front
  * LB or BL -> move 2 cells diagonally towards back left
  * RB or BR -> move 2 cells diagonally towards back right
* For Hero3
  * LF -> move 2 cells left and 1 cell forward
  * FL -> move 2 cells forward and 1 cell left
  * RF -> move 2 cells right and 1 cell forward
  * FR -> move 2 cells forward and 1 cell right
  * LB -> move 2 cells left and 1 cell backward
  * BL -> move 2 cells backward and 1 cell left
  * RB -> move 2 cells right and 1 cell backward
  * BR -> move 2 cells backward and 1 cell right

*invalid moves are checked (and sanitized) first before proceeding with the core task.*

## sneak peek

![initial Game][initialize_ss]
![during Game][rungame_ss]
![validity Check][validity_ss]

## Roadmap

* [x] More pieces type
* [x] Move moves type
* [ ] testing

## Changelog

### v0.3.0

* Piece Type - `H3`
* Move Types - `LF`, `FL`, `FR`, `RF`, `LB`, `BL`, `RB`, `BR` for piece type `H3`
* Type hinting added.

Entire changelog is available at [changelog.md](./changelog.md)

[initialize_ss]: images/initialScreen.png
[rungame_ss]: images/rungame.png
[validity_ss]: images/validityCheck.png
