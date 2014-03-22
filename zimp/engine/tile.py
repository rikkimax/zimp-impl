#------------------------------------------------------------------------------
# Name:        tile
# Purpose:     choosing tiles
#
# Author:      framework = Richard Cattermole
#              content code = Loki Kristianson
#
# Created:     19/03/2014
#
# -- Richard edit --
# commit file is based upon
# https://github.com/lokikristianson/zimp-impl/commit/064a046e5a3a1b93e951ebaeebfac68f4391753f#diff-207dd9adbc17f263cbd9c106f70bd130
# -- Richard edit --
#
#------------------------------------------------------------------------------


import random

current_area = []
area_data = []
area = []
# -- Richard edit --
for line in open("../../data/zimp_tiles.txt"):
# -- Richard edit --
    line = line.split(",")
    for num in range(0, 16):
        area_data = line[0:7]
        area_data[0] = int(area_data[0])
        for i in range(2, 7):
            area_data[i] = bool(area_data[i])
        area.append(area_data)
        del (line[0:7])


class Tile:
    def __init__(self, id):
        self.type = id
        self.name = area[id][1]
        current_area = area[0]

    def on_resolve_card(self, card):
        """
        Rikki & Claire, I'll have this function done Saturday

        When a dev card has been solved call this.
        Allows for events on this instance.
        """
        pass

    def find_next(self):
        """
        Randomly chooses a new Tile card.
        This does not apply to the Foyer and Patio.
        Returns:
            A new Tile instance
        """
        global area
        global current_area
        x = 0
        for num in range(1, len(area)):  # loop to be removed when game runs
            del area[x]  # Takes foyer out of equasion, and after that
            #  each room as it is chosen
            x = random.randrange(0, len(area), 1)
            if area[x][1] == "Patio":
                return
            else:
                current_area = area[x]
            return

# These functions below will be called from the game engine
which_tile = Tile(0)  # Chooses initial Foyer
which_tile.find_next()  # Randomly chooses next tile
