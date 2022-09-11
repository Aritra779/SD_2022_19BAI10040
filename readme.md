This is the very first version of the CLI based chess like games.

Description about the game will be here and the changelog with each version will be under changelog.md

# pre-requisites
- python 
- typer
# How to use
run
```
python chess.py
```
inside of the folder where the project lies
# Currently supported Pieces:
* P -> pawn

# Currently supported Moves:
* L -> move 1 cell left
* R -> move 1 cell right
* F -> move 1 cell forward
* B -> move 1 cell backward

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