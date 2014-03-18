class Item:

    name = ''
    is_weapon = False
    is_consumable = False
    attack = 0

    def on_attack(self):
        """
        When the item is used to attack zombies, call this.
        """
        pass

    def on_usage(self):
        """
        When the item is used. Note this is for consumable.
        """
        pass