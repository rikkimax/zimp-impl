"""
Made by Richard Andrew Cattermole
"""

from zimp.engine.defs import Direction, Tiles
import shelve
import time
import random
from zimp.engine import devcard, tile, tilestate
import os


class SerializeException(Exception):
    """
    I'm not really concerned with _what_ happened.
    Just that something did go wrong.
    So now yell at the user.
    """

    def __str__(self):
        return "Could not serialize data to file system."


class DeserializeException(Exception):
    """
    I'm not really concerned with _what_ happened.
    Just that something did go wrong.
    So now yell at the user.
    """

    def __str__(self):
        return "Could not deserialize data from file system."


class GameState:
    """
        Holds the entire game state
        Also includes events to call for UI.

        >>> GameState().health == 0
        True
        >>> state = GameState()
        >>> state.setup_new_game()
        >>> state.health == 6
        True
    """

    current_tile = None
    foyer_tile = None
    dev_cards_used = []
    dev_cards_iteration = 0
    item1 = None
    item2 = None
    health = 0
    has_totem = False

    def setup_new_game(self):
        """
        Configures self for a new fresh game.
        """
        self.health = 6
        self.current_tile = tilestate.TileState(tile.Tile(Tiles.Foyer))
        self.foyer_tile = self.current_tile

    def spawn_zombies(self, count, direction=Direction.Unknown):
        """
        Spawns {count} zombies in {direction}.
        Most likely this is used for the ui.
        """
        pass

    def new_dev_card(self):
        """
        Draws a new dev card.
        """
        if len(self.dev_cards_used) == 7:
            self.dev_cards_used.clear()
            self.dev_cards_iteration += 1

        cards_left = [i for i in range(0, 7) if not i in self.dev_cards_used]
        card = cards_left[random.randint(0, len(cards_left))]
        self.dev_cards_used += card

        self.on_dev_card(devcard.Devcard(card))

    def on_start(self):
        """
        On start of new game.
        """
        pass

    def on_death(self):
        """
        When you die in a game.
        """
        pass

    def on_new_tile(self):
        """
        When you go to a new tile.
        """
        pass

    def on_dev_card(self, card):
        """
        When a development card is drawn, call this.
        """
        pass

    def on_place_tile(self, tile):
        """
        We are placing a new tile. Note this is where we rotate it.
        """
        pass

    def on_end_turn(self):
        """
        When a turn ends. Call this.
        """
        pass

    def on_new_turn(self):
        """
        Yay its a new turn. Make it happen in ui!
        """
        pass

    def serialize(self, file):
        """
        Saves the data structure into the given file.
        """

        try:
            file = shelve.open(os.path.abspath(file), writeback=True)
            file["game"] = self
            file["lastEdited"] = time.strftime("%c")
            file.close()
        except Exception as err:
            raise SerializeException()

    @classmethod
    def deserialize(cls, file, extra_info=None):
        """
        Loads a data structure from the given file.
        """

        try:
            file = shelve.open(os.path.abspath(file), writeback=True)
            ret = file["game"]
            if not extra_info is None:
                extra_info.last_edited = file["lastEdited"]
            file.close()
        except Exception as err:
            raise DeserializeException()

        return ret


class ExtraGameInfo:
    """
    A clever way to return data with deserialize method on GameState
    without tuples!
    """

    def __init__(self):
        self.last_edited = ""
