"""
Made by Richard Andrew Cattermole
"""

import cmd
from zimp.engine import gamestate
from zimp.ui.cligame import CliGame
from zimp.ui.clihelpers import *
import os
import traceback


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

                try:
                    self.game_save = CliGame.deserialize(arg, more_info)
                    self.state = CmdUiState.Loaded
                    self.game_save_name = arg
                except gamestate.DeserializeException:
                    print("That was a bad choice. Could not load file.")

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
                except gamestate.SerializeException:
                    print("Could not save game. I'm so sorry.")
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

    try:
        ui.cmdloop()
    except Exception as err:
        print("I'm so sorry something has REALLY REALLY gone wrong. Please create a github issue at:")
        print("\thttps://github.com/rikkimax/zimp-impl/issues")
        print("And please tell them this information:")
        print("\t" + str(err.args))
        print("\t" + str(traceback.format_tb(sys.exc_info()[2])))
