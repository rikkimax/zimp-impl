from zimp.engine.gamestate import GameState
from zimp.engine import defs
import sys
import doctest


def rotational_output(dir1, dir2):
    """
    >>> rotational_output(defs.Direction.UP, defs.Direction.DOWN)\
        == defs.Direction.DOWN
    True
    >>> rotational_output(defs.Direction.LEFT, defs.Direction.DOWN)\
        == defs.Direction.RIGHT
    True
    """

    rotation = 0

    if dir1 == defs.Direction.RIGHT:
        rotation += 90
    elif dir1 == defs.Direction.DOWN:
        rotation += 180
    elif dir1 == defs.Direction.LEFT:
        rotation += 270
    else:
        # is top or unknown
        pass

    if dir2 == defs.Direction.RIGHT:
        rotation += 90
    elif dir2 == defs.Direction.DOWN:
        rotation += 180
    elif dir2 == defs.Direction.LEFT:
        rotation += 270
    else:
        # is top or unknown

        pass

    rotation %= 360

    if rotation == 0:
        return defs.Direction.UP
    elif rotation == 90:
        return defs.Direction.RIGHT
    elif rotation == 180:
        return defs.Direction.DOWN
    elif rotation == 270:
        return defs.Direction.LEFT
    else:
        return defs.Direction.Unknown


class CliGame(GameState):

    def on_new_turn(self):
        """
        Yay its a new turn. Make it happen in ui!
        """

        tile = self.current_tile.tile
        tile_state = self.current_tile

        #
        # tile state output
        #

        print("You are currently at " + tile.name + " tile.")

        sys.stdout.write("There are doors at")

        hit_door = False

        if tile.door_top:
            sys.stdout.write(" top")
            hit_door = True
        if tile.door_bottom:
            sys.stdout.write(" bottom")
            hit_door = True
        if tile.door_left:
            sys.stdout.write(" left")
            hit_door = True
        if tile.door_right:
            sys.stdout.write(" right")
            hit_door = True

        if hit_door:
            sys.stdout.write(".\n")
        else:
            sys.stdout.write(" none, its a dead end.\n")
            # zombie door time!

        if tile.type == defs.Tiles.DiningRoom:
            sys.stdout.write("The door to the outside is: ")

            door = rotational_output(tile_state.rotation, defs.Direction.UP)

            if door == defs.Direction.UP:
                sys.stdout.writeline("top.")
            elif door == defs.Direction.DOWN:
                sys.stdout.writeline("down.")
            elif door == defs.Direction.RIGHT:
                sys.stdout.writeline("right.")
            elif door == defs.Direction.LEFT:
                sys.stdout.writeline("left.")

        if tile.type == defs.Tiles.Kitchen:
            print("Snack time! Gain 1 health.")
            self.game_save.health += 1

        if tile.type == defs.Tiles.Garden:
            print("Helpful herbs! Gain 1 health")
            self.game_save.health += 1

        # choose door to get new tile for

        # get a new tile

        # handle rotation

        # handle move

        # get dev card
        # handle it

    def on_end_turn(self):
        """
        When a turn ends. Call this.
        """

        tile = self.current_tile.tile
        tile_state = self.current_tile

        #
        # tile state query / modify
        #

        if tile.type == defs.Tiles.EvilTemple:
            fine = False

            while not fine:
                sys.stdout.write("Spend time to find totem? [yes/no]: ")
                answer = sys.stdin.readline()
                if answer.lower() == "yes":
                    # todo dev card use
                    fine = True
                elif answer.lower() == "no":
                    #todo
                    fine = True
                else:
                    pass

        if tile.type == defs.Tiles.StorageRoom:
            fine = False

            while not fine:
                sys.stdout.write("Spend time looking for an item? [yes/no]: ")
                answer = sys.stdin.readline()
                if answer.lower() == "yes":
                    # todo found item
                    fine = True
                elif answer.lower() == "no":
                    #todo
                    fine = True
                else:
                    pass

        if tile.type == defs.Tiles.Graveyard:
            fine = False

            while not fine:
                sys.stdout.write("Spend time to bury totem? [yes/no]: ")
                answer = sys.stdin.readline()
                if answer.lower() == "yes":
                    # todo bury totem
                    fine = True
                elif answer.lower() == "no":
                    #todo
                    fine = True
                else:
                    pass

        #
        # End of turn actions
        #

        door_used_count = len([d for d in
                               [tile_state.up, tile_state.down, tile_state.left,
                                tile_state.right]
                               if not None])

        door_available_count = len([d for d in
                                    [tile.door_top, tile.door_bottom,
                                     tile.door_left, tile.door_right]
                                    if True])

        if door_used_count == door_available_count:
            # zombie door
            # because all doors possible that could be used have been used.

            # choose a direction

            sys.stdout.write("There are no doors at")

            hit_door = False

            if not tile.door_top:
                sys.stdout.write(" top")
                hit_door = True
            if not tile.door_bottom:
                sys.stdout.write(" bottom")
                hit_door = True
            if not tile.door_left:
                sys.stdout.write(" left")
                hit_door = True
            if not tile.door_right:
                sys.stdout.write(" right")
                hit_door = True

            if hit_door:
                sys.stdout.write(".\n")
            else:
                sys.stdout.write("none, ERROR.\n")
                raise Exception("WHAT IS GOING ON HERE NO ZOMBIE DOOR POSSIBLE")

            direction = defs.Direction.Unknown

            fine = False
            while not fine:
                sys.stdout.write("Choose a door please [left/right/up/down]: ")
                door = sys.stdin.readline().tolower()
                if door == "left":
                    if not tile.door_left:
                        direction = defs.Direction.LEFT
                        fine = True
                elif door == "right":
                    if not tile.door_right:
                        direction = defs.Direction.RIGHT
                        fine = True
                elif door == "up":
                    if not tile.door_top:
                        direction = defs.Direction.UP
                        fine = True
                elif door == "down":
                    if not tile.door_bottom:
                        direction = defs.Direction.DOWN
                        fine = True

            # make it a door (on tile)

            if direction == defs.Direction.UP:
                tile.door_top = True
            elif direction == defs.Direction.DOWN:
                tile.door_bottom = True
            elif direction == defs.Direction.LEFT:
                tile.door_left = True
            elif direction == defs.Direction.RIGHT:
                tile.door_right = True

            self.spawn_zombies(3, direction)

        if self.game_save.health <= 0 or \
                (self.game_save.dev_cards_used == 7 and
                 self.game_save.dev_cards_iteration == 3):
            print("You have died")
            self.game_save.on_death()
            return

        fine = False

        while not fine:
            sys.stdout.write("Wait and cower for 3 health? [yes/no]: ")
            answer = sys.stdin.readline()
            if answer.lower() == "yes":
                # todo gain health
                fine = True
            elif answer.lower() == "no":
                #todo
                fine = True
            else:
                pass

        print("End of turn")

    def spawn_zombies(self, count, direction=defs.Direction.Unknown):
        """
        Spawns {count} zombies in {direction}.
        Most likely this is used for the ui.
        """

        # get items that can be used for attack
        # ask which one the user wants to use
        # use it
        # calculate health loss
        # lose health
        pass

if __name__ == "__main__":
    doctest.testmod()