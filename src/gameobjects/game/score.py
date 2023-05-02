from gameobjects.menu.text import Text


class Scoreboard:

    """
    Encapsulates the pygame UI score texts and whose turn it is
    """

    def __init__(self,scoretext_1: Text, scoretext_2: Text, rounds: Text) -> None:
        self.__scoretext_1 = scoretext_1
        self.__scoretext_2 = scoretext_2
        self.__rounds = rounds

    def update(self, p1:int, p2:int, rounds:int):
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


