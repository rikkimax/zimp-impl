"""
Coded by Claire.
"""

import csv


class Item:
    """
    Assigns names and values to the items on the dev cards.

    >>> Item(0).name
    'Oil'
    >>> Item(8).name
    'Candle'
    >>> Item(0).is_weapon
    False
    >>> Item(4).is_weapon
    True
    >>> Item(8).is_weapon
    False
    >>> Item(0).is_consumable
    True
    >>> Item(4).is_consumable
    False
    >>> Item(8).is_consumable
    True
    >>> Item(0).attack_value
    0
    >>> Item(4).attack_value
    2
    >>> Item(8).attack_value
    0
    >>> Item("str")
    Traceback (most recent call last):
    ...
    Exception: id invalid for item
    >>> Item(9)
    Traceback (most recent call last):
    ...
    Exception: id invalid for item
    >>> Item(-1)
    Traceback (most recent call last):
    ...
    Exception: id invalid for item
    >>> Item(2.7)
    Traceback (most recent call last):
    ...
    Exception: id invalid for item
    """

    name = ''
    is_weapon = False
    is_consumable = False
    attack = 0

    def __init__(self, id):
        if not isinstance(id, int):
            raise Exception("id invalid for item")

        if id < 0 or id > 8:
            raise Exception("id invalid for item")

        self.name = ["Oil", "Gasoline", "Board with Nails",
                     "Machete", "Grisly Femur", "Golf Club",
                     "Chainsaw", "Can of Soda", "Candle"][id]

        self.is_weapon = [False, False, True,
                          True, True, True,
                          True, False, False][id]

        self.is_consumable = [True, True, False,
                              False, False, False,
                              False, True, True][id]

        self.attack_value = [0, 0, 2, 3, 2, 2, 4, 0, 0][id]

    def on_attack(self):
        """
        When the item is used to attack zombies, call this.
        """
        return ("This is on_attack")

    def on_usage(self):
        """
        When the item is used. Note this is for consumable.
        """
        return ("This is on_usage")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
