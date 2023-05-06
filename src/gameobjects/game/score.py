from math import sqrt
from gameobjects.menu.text import Text


class Scoreboard:

    """
    Encapsulates the pygame UI score texts and whose turn it is
    """

    def __init__(self, scoretext_1: Text, scoretext_2: Text,
                 rounds: Text, titlerounds: Text, hops: Text, victory: Text) -> None:
        self.__scoretext_1 = scoretext_1
        self.__scoretext_2 = scoretext_2
        self.__rounds = rounds
        self.__title_rounds = titlerounds
        self.__hops = hops
        self.__victory = victory

    def update(self, points_1: int, points_2: int, rounds: int, moves_left):
        """
        Updates score of players

            Args:
                points_1: integer, score of player 1
                points_2: integer, score of player 2
                rounds: integers, rounds left in game
        """
        self.__scoretext_1.text = str(points_1)
        self.__scoretext_2.text = str(points_2)
        self.__rounds.text = f"{str(rounds)}/10"
        self.__hops.text = str(int(sqrt(rounds)))
        if moves_left != 1:
            self.__title_rounds.text = str(moves_left - 1)
        else:
            self.__title_rounds.text = str(3)
            if self.__title_rounds.rgb == (176, 62, 80):
                self.__title_rounds.rgb = (64, 164, 244)
            else:
                self.__title_rounds.rgb = (176, 62, 80)

    def game_state(self):
        """
        Sets boardstate to standard
        """
        self.__scoretext_1.row, self.__scoretext_2.row = 0.9, 0.9
        self.__scoretext_1.col, self.__scoretext_2.col = 0.1, 0.9
        self.__scoretext_1.scale, self.__scoretext_2.scale = 0.4, 0.4

    def victory_state(self, player_1_score, player_2_score):
        """
        Sets boardstate to victory

            Args:
                player_1_score: int, score of player 1
                player_2_score: int, score of player 2
        """
        self.__scoretext_1.row, self.__scoretext_2.row = 0.45, 0.45
        self.__scoretext_1.col, self.__scoretext_2.col = 0.25, 0.75
        self.__scoretext_1.scale, self.__scoretext_2.scale = 0.7, 0.7
        if player_1_score > player_2_score:
            self.__victory.text = "Blue Won!"
        elif player_1_score < player_2_score == 2:
            self.__victory.text = "Red Won!"
        else:
            self.__victory.text = "Tie!"
