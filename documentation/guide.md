# Guide
This is an user guide for the project.

## Installation

1. Install the dependencies:
`poetry install`
2. Build the project
`poetry run invoke build`
3. Run the project
`poetry run invoke start`

## Command line functionality
Run tests by running `poetry run invoke coverage`

Generate a report by running `poetry run invoke coverage-report`

Check pylint by running `poetry run invoke lint`

## How to play

The gameplay loop is simple:

- Each player places three cells on the board
- State shifts, so we apply normal game of life rules as well as interaction rules
    - if live cell is surrounded by less than two friendlies, it dies
    - if live cell is surrounded by two or three friendlies, it lives
    - if live cell is surrounded by four friendlies or more, it dies
    - if live cell is surrounded by more enemies than friendlies, it dies
    - if dead cell is surrounded by three friendlies and less than three enemies, it becomes alive
- Points are gained from eating enemy cells (+2) and making new cells (+1)
- The number at the side of score is the number of stateshifts, which increases gradually as the game goes on
- Most points win!
