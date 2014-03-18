class Tile:

    type = 0
    name = ''
    door_top = False
    door_right = False
    door_bottom = False
    door_left = False
    add_1_health = False
    may_resolve_card = False

    def on_resolve_card(self, card):
        """
        When a dev card has been solved call this.
        Allows for events on this instance.
        """
        pass

    def find_next(self, direction):
        """
        Resolves a new Tile card.
        For special cards this won't be randomly chosen.

        Returns:
            A new Tile instance
        """
        pass