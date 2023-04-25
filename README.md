# Game of life: Multiplayer
This game will be a multiplayer version of the titular game! As of this moment it is unfinished.

## How to play
Navigate to the game from the menu. Click to create a cell of either color (every second click is blue, every second is red). Press space to go to the next state.

## Python version 
Use python 3.8.

## Documentation
[Definition document](./documentation/definition.md) 


[Changelog](./documentation/changelog.md)


[Architecture](./documentation/architecture.md)


[Time spent on the project](./documentation/hours-spent.md)


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
