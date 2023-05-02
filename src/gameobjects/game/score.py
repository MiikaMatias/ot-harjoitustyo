from gameobjects.menu.text import Text


class Scoreboard:

    """
    Encapsulates the pygame UI score texts and whose turn it is
    """

    def __init__(self,scoretext_1: Text, scoretext_2: Text, rounds: Text, titlerounds: Text) -> None:
        self.__scoretext_1 = scoretext_1
        self.__scoretext_2 = scoretext_2
        self.__rounds = rounds
        self.__title_rounds = titlerounds

    def update(self, p1:int, p2:int, rounds:int, moves_left:int):
        """
        Updates score of players

            Args: 
                p1: integer, score of player 1
                p2: integer, score of player 2
                rounds: integers, rounds left in game
        """
        self.__scoretext_1.text = str(p1)
        self.__scoretext_2.text = str(p2)
        self.__rounds.text = str(rounds)
        if moves_left != 1:
            self.__title_rounds.text = str(moves_left-1)
        else:
            self.__title_rounds.text = str(3)
            if self.__title_rounds.rgb == (176,62,80):
                self.__title_rounds.rgb = (64,164,244)
            else:
                self.__title_rounds.rgb = (176,62,80)




