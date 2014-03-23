"""
Coded by Claire.
"""

import csv
# -- Richard edit --
from zimp.engine import item
import sys
# -- Richard edit --


class DevCard:
    """
    Assigns text and values to the actions on the dev cards.

    >>> DevCard(0, 0).text
    'You try hard not to wet yourself.'
    >>> DevCard(8, 2).text
    '4 Zombies'
    >>> DevCard(0, 0).is_item
    False
    >>> DevCard(8, 2).is_item
    False
    >>> DevCard(0, 0).is_attack
    False
    >>> DevCard(8, 2).is_attack
    True
    >>> DevCard(0, 0).health_adjust
    0
    >>> DevCard(8, 2).health_adjust
    -4
    >>> DevCard("str", 0)
    Traceback (most recent call last):
    ...
    Exception: id invalid for text
    >>> DevCard(0, "str")
    Traceback (most recent call last):
    ...
    Exception: iteration invalid for text
    >>> DevCard(9, 0)
    Traceback (most recent call last):
    ...
    Exception: id invalid for text
    >>> DevCard(0, 3)
    Traceback (most recent call last):
    ...
    Exception: iteration invalid for text
    >>> DevCard(-1, 0)
    Traceback (most recent call last):
    ...
    Exception: id invalid for text
    >>> DevCard(0, -1)
    Traceback (most recent call last):
    ...
    Exception: iteration invalid for text
    >>> DevCard(1.1, 0)
    Traceback (most recent call last):
    ...
    Exception: id invalid for text
    >>> DevCard(0, 1.1)
    Traceback (most recent call last):
    ...
    Exception: iteration invalid for text
    """

    item = None

    def __init__(self, id, iteration):
        if not isinstance(id, int):
            raise Exception("id invalid for text")

        if id < 0 or id > 8:
            raise Exception("id invalid for text")

        if not isinstance(iteration, int):
            raise Exception("iteration invalid for text")

        if iteration < 0 or iteration > 2:
            raise Exception("iteration invalid for text")

        i = 0
        # -- Richard edit --
        sep = "\\"
        if sys.path[0].__contains__("/"):
            sep = "/"
        file = "../" * len(sys.path[0].split("zimp" + sep)[1].split(sep))
        file += "../data/devcard.csv"
        with open(file, newline='\n') as csvfile:
            # -- Richard edit --
            for line in csv.reader(csvfile, delimiter=',', quotechar='|'):
                if i == id:
                    if len(line) == 3:
                        self.text = line[iteration]
                i += 1

        self.item = item.Item(id)

        self.is_item = [[False, True, False],
                        [False, False, True],
                        [True, False, False],
                        [False, False, False],
                        [True, False, False],
                        [False, False, False],
                        [False, False, False],
                        [False, True, False],
                        [False, False, False]][id][iteration]

        self.is_attack = [[False, False, True],
                          [True, False, False],
                          [False, True, False],
                          [True, False, True],
                          [False, True, False],
                          [False, True, False],
                          [True, False, True],
                          [False, False, True],
                          [False, False, True]][id][iteration]

        self.health_adjust = [[0, 0, -6],
                              [-4, -1, 0],
                              [0, -4, -1],
                              [-4, -1, -6],
                              [0, -5, -1],
                              [-1, -4, 0],
                              [-3, 0, -5],
                              [1, 0, -4],
                              [0, 1, -4]][id][iteration]

    def on_time_action(self, game_state):
        """
        When an action is to occur for this dev card, do this.
        This allows for custom handling of the events of any card.
        """
        # go to game_state and get id and iteration
        # for id and iteration
        #   print text
        #   if is_attack
        #       attack or run
        #       A LOT OF THIS NEEDS TO BE IN CliGame
        #       if attack
        #           get item.attack_value
        #           health_lost = item.attack_value + health_adjust
        #           health = health + health_lost
        #       if run
        #           health = health -1
        #       if run_with_oil
        #           pass
        #   if is_item
        #       print("Spend time looking for item?")
        #           if y
        #               get new_dev_card to get item
        #               increment dev_cards_used
        #           if n
        #               pass
        #   elif
        #       health = health_adjust
        # increment dev_cards_used
        return ("This is on_time_action")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
