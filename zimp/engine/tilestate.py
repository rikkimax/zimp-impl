#------------------------------------------------------------------------------
# Name:        tilestate
# Purpose:
#
# Author:      framework = Richard Cattermole
#              content code = Loki Kristianson
#
# Created:     19/03/2014
# Copyright:   (c)
#
#------------------------------------------------------------------------------


# -- Richard edit --
from zimp.engine.defs import Direction
from zimp.engine.tile import current_area
# -- Richard edit --

class TileState:
    # -- Richard edit --
    def __init__(self, tile, rotation = Direction.Unknown, left = None, right = None, top = None, bottom = None,
                 has_item_been_found = False):
        # -- Richard edit --
        self.tile = tile
        self.rotation = rotation
        if rotation == 1:
            self.left = left
            self.right = right
            self.top = top
            self.bottom = bottom
        elif rotation == 2:
            self.left = bottom
            self.right = top
            self.top = left
            self.bottom = right
        elif rotation == 3:
            self.left = right
            self.right = left
            self.top = bottom
            self.bottom = top
        else:
            self.left = top
            self.right = bottom
            self.top = right
            self.bottom = left
        self.has_item_been_found = has_item_been_found
        return


#place_tile = TileState(current_area[1], 1, current_area[2],
#                       current_area[3], current_area[4],
#                       current_area[5], False)