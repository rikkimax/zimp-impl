from zimp.engine.defs import Direction


class TileState:

    tile = None
    rotation = Direction.Unknown
    left = None
    right = None
    up = None
    down = None
    has_item_been_found = False