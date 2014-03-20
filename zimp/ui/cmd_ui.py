import cmd
import dbm
import os.path
import builtins
from zimp.engine import gamestate, defs
from zimp.ui.cligame import CliGame
import sys
from zimp.ui.clihelpers import *
import os


class CmdUiState:
    """
    The state that the cmd UI is currently in.
    Allows for cross command sequences
    """

    Startup = 0
    Loaded = 1
    Turn = 2


class CmdUi(cmd.Cmd):

    def startup(self):
        self.state = CmdUiState.Startup
        self.game_save = None
        self.game_save_name = None
        self.prompt = "$ zimp >>> "

    def help_load(self):
        if self.state == CmdUiState.Startup:
            print("Loads a previous game given a file name")
        else:
            print("")

    def do_load(self, arg):
        """
        Loads a new game from save file.
        """

        if self.state == CmdUiState.Startup:
            try:
                more_info = gamestate.ExtraGameInfo()

                self.game_save = CliGame.deserialize(arg, more_info)
                self.state = CmdUiState.Loaded
                self.game_save_name = arg

                print("Last saved: " + more_info.last_edited)
            except:
                print("Could not load file. Not a valid save game")

    def help_new(self):
        if self.state == CmdUiState.Startup:
            print("Creates a new game. Optional argument of save file name")
        else:
            print("")

    def do_new(self, arg):
        """
        Creates a new game.
        Optional argument being the save file name
        """

        if self.state == CmdUiState.Startup:
            self.game_save = CliGame()
            self.state = CmdUiState.Loaded
            self.game_save_name = arg

            print_game_rules()
            self.game_save.setup_new_game()

    def help_delete(self):
        if self.state == CmdUiState.Loaded:
            print("Deletes a saved game")
        else:
            print("")

    def do_delete(self, arg):
        """
        Deletes a saved game.
        Takes an optional argument of the game save.
        If is the current game, resets the program.
        """

        if self.state == CmdUiState.Loaded:
            if arg == "":
                name = self.game_save_name
            else:
                name = arg

            if not name == "":
                os.remove(name + '.dat')
                os.remove(name + '.bak')
                os.remove(name + '.dir')

            if name == self.game_save_name:
                print("Resetting game state")
                self.state = CmdUiState.Startup

    def help_save(self):
        if self.state == CmdUiState.Loaded:
            print("Saves the current game state. Optional argument of save file name")
        else:
            print("")

    def do_save(self, arg):
        """
        Saves the current game state to file.
        Optionally takes an argument (save file)
        """

        if self.state == CmdUiState.Loaded:
            name = ""
            if not self.game_save_name == "":
                name = self.game_save_name
            elif not arg == "":
                name = arg
            else:
                sys.stdout.write("Please enter the save file name: ")
                sys.stdout.flush()
                name = sys.stdin.readline()

            if not name == "":
                try:
                    self.game_save.serialize(name)
                    self.game_save_name = name
                except:
                    print("Could not save game")
            else:
                print("Must specify a name")

    def help_turn(self):
        if self.state == CmdUiState.Turn:
            print("Play a turn of the game")

    def do_turn(self, arg):
        if self.state == CmdUiState.Turn:
            tile_state = self.game_save.current_tile
            tile = tile_state.tile

            self.game_save.on_new_turn()

            #
            # tile state output
            #

            print("You are currently at " + tile.name + " tile.")

            sys.stdout.write("There are doors at ")

            hit_door = False

            if tile.door_top:
                sys.stdout.write("top ")
                hit_door = True
            if tile.door_bottom:
                sys.stdout.write("bottom ")
                hit_door = True
            if tile.door_left:
                sys.stdout.write("left ")
                hit_door = True
            if tile.door_right:
                sys.stdout.write("right")
                hit_door = True

            if hit_door:
                sys.stdout.write(".\n")
            else:
                sys.stdout.write("none, its a dead end.\m")
                # zombie door time!

            if tile.type == defs.Tiles.DiningRoom:
                # todo print that the door to outside is at top (allow for rotations)
                pass

            if tile.type == defs.Tiles.Kitchen:
                print("Snack time! Gain 1 health.")
                self.game_save.health += 1

            if tile.type == defs.Tiles.Garden:
                print("Helpful herbs! Gain 1 health")
                self.game_save.health += 1

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

            door_used_count = len([d for d in
                                  [tile_state.up, tile_state.down, tile_state.left, tile_state.right]
                                  if not None])
            door_available_count = len([d for d in
                                       [tile.door_top, tile.door_bottom, tile.door_left, tile.door_right]
                                       if True])

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

            if door_used_count == door_available_count:
                # zombie door
                # because all doors possible that could be used have been used.
                pass

            if self.game_save.health <= 0 or\
                    (self.game_save.dev_cards_used == 7 and self.game_save.dev_cards_iteration == 3):
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
            self.game_save.on_end_turn()

    def do_quit(self, arg):
        """
        Quit the application
        """
        return True

    def do_clear(self, arg):
        """
        Clears the screen
        """
        clear()

def print_game_rules():
    print("==----------==")
    print("| " + bold("Game rules") + " |")
    print("==----------==")
    print()
    print('The aim of the game is to not ' + color(Colors.Red, bold('die')) +\
          '. Oh and you can only do this by burying the totem in the grave yard.')

if __name__ == "__main__":
    ui = CmdUi()
    ui.startup()
    ui.cmdloop()