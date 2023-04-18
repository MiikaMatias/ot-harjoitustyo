## Week 3

- Main script created, runs a gameplay loop that renders an useless button
- The foundational logic for the game of life system has been made in logic/gameboard.py
- Tests for logic/gameboard.py made
- Foundational GUI class created at gui/image
- Display made at gui/display
- Downloaded some menu assets to assets/menu_items/menu
- Some other miscallaneus additions + documentation

## Week 4

- Created the basic menu structure with all requisite transitions par from game -> settings and game -> menu
- Fleshed out the button class, and made it inherit off of the Image class
- Cleaned up the functionality of GameOfLife by a lot
- Downloaded some assets that will probably be used in the actual implemenation of the game
- Wrote credits for assets
- Made buttons, text, game objects completely dynamically sizeable; text has different properties than f.e. tiles
- Made a preliminary tile class that will work as the communication point between game logic and the UI through the gameboard
