# Definition of the program

## Purpose of the application

The application is intended to be a simple proof of concept for a multiplayer version of [Conway's Game Of Life](https://playgameoflife.com/). The idea was to make a competitive version of the traditional game. 
## Users

There is really just a singular user role, which is a generic _player_ role. Further iterations could consider adding a game _host_ role for the player that hosts the server, and sets the rules of the game. However at this point no special rules are needed. 

## UI

There are five UI-states:

![](https://github.com/MiikaMatias/ot-harjoitustyo/blob/main/documentation/images/outline.png)

1) menu: connects to settings and pregame
2) settings: connects to menu
3) pre_game: connects to menu and game
4) game: connects from pre-game to victory
5) victory: connects to menu

## Base version
Players play according to the rules defined in the [guide document](https://github.com/MiikaMatias/ot-harjoitustyo/blob/main/documentation/guide.md). The player is able to adjust the volume of the game in the settings menu. The best player wins!

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
