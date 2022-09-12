<!-- markdownlint-disable MD024 -->

# CHANGELOG

## v0.2.0

### Added

* Piece Type - `H2`
* Move Types - `LF`, `FL`, `FR`, `RF`, `LB`, `BL`, `RB`, `BR` for piece type `H2`

### Changed

* small changes in names of certain fucntions to make names uniform throughout the project
* Names and move types are now case insensitive i.e. `P1` and `p1` both will work.

### Removed

* Nothing :)

## v0.1.0

### Added

* Piece Type - `H1`
* Move Types - `L`, `R`, `F`, `B` for piece type `H1`
* [poetry](https://python-poetry.org/) for easier package management

### Changed

* Structure of the project folders
* Improved some core logic
* `Game` is now a directory. Not a package anymore.
* `HeroTypes` is now a directory. Not a package anymore.
* `Chess` is now the parent package.
* Fixed typos

### Removed

* Nothing. ;)

## Pre versioning

*All commits before the 8th commit aren't versioned.*

### Added

* First Version of the game
* README.md
* CHANGELOG.md
* Piece Type - `P`
* Move Types - `L`, `R`, `F`, `B`
* Move validation (and sanitization)
