from zimp.engine.defs import Direction
import shelve
import time


class GameState:

    current_tile = None
    foyer_tile = None
    dev_cards_used = []
    dev_cards_iteration = 0
    item1 = None
    item2 = None
    health = 0
    has_totem = False

    def spawn_zombies(self, count, direction = Direction.Unknown):
        """
        Spawns {count} zombies in {direction}.
        Most likely this is used for the ui.
        """
        pass

    def new_dev_card(self):
        """
        Draws a new dev card.
        """
        pass

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
        pass

    @classmethod
    def deserialize(cls, file, extra_info = None):
        """
        Loads a data structure from the given file.
        """
        pass


class ExtraGameInfo:

    def __init__(self, last_edited):
        self.last_edited = last_edited