# Definition of the program

## Purpose of the application

The application is intended to be a multiplayer version of [Conway's Game Of Life](https://playgameoflife.com/), wherein two players will blindly put their 'cells' down on the board, and then gather points based on how many of their cells will survive. The general idea is to have this game be playable on multiple clients – online so that each player plays on their own device – if time constraints allow, but an initial draft will only concern a single client.

## Users

There is really just a singular user role, which is a generic _player_ role. Further iterations could consider adding a game _host_ role for the player that hosts the server, and sets the rules of the game. 

## UI draft

There are three of four initially planned UI-states:

![](./documentation/images/outline.png)

1) Menu; connects to main game through game rule configuration screen; connects to options
2) Game screen | rule configuration screen; game rules can be modified in rule config. Different configurations can be saved into a database; rule config connects to the main game and maybe settings; game connects to settings and the menu through a game-over event.
3) Settings; includes sound sliders and some other options; maybe credits.

## Base version
The player is able to start the game, and configure it's rules. Afterwards, the players will play against each other. Settings may be modified during any point. Game may be quit during any point. Rule presets can be saved. The game mechanics will be nice and the implementation will be slick. 

## Further ideas

Within the confines of time constaints it may be that...

- The game is playable online
- The game settings will become more diverse, including:
    1) modifiable amount of turns
    2) game speed
    3) amount of 'cells' available at the start for each player
    4) rules between interactions of rival 'cells'
    5) different methods of getting points; modifiable amounts for points 
    6) variable map sizes
    7) special cell types
    8) special map types; wall tiles e.g.
    9) 'special abilities' such as limiting the possible moves for an enemy
- A leaderboard may be implemented
- A bot enemy/enemies or a campaign mode could be implemented
- Progression mechanics could be implemented, e.g. unlockables
- Music selection and sfx may be refined, changed
- More
