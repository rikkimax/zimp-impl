import cmd
import dbm
import os.path
from zimp.engine.gamestate import GameState
import sys
from zimp.ui.clihelpers import *


class CmdUiState:
    """
    The state that the cmd UI is currently in.
    Allows for cross command sequences
    """

    Startup = 0
    Loaded = 1


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
            if os.path.isfile(arg):
                try:
                    self.game_save = GameState.deserialize(arg)
                    self.state = CmdUiState.Loaded
                    self.game_save_name = arg
                except dbm.error:
                    print("Could not load file. Not a valid save game")
            else:
                print("Game save does not exist")

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
            self.game_save = GameState()
            self.state = CmdUiState.Loaded
            self.game_save_name = arg

            print_game_rules()

    def help_save(self):
        if self.state > CmdUiState.Loaded:
            print("Saves the current game state. Optional argument of save file name")
        else:
            print("")

    def do_save(self, arg):
        """
        Saves the current game state to file.
        Optionally takes an argument (save file)
        """

        if self.state > CmdUiState.Loaded:
            name = ""

            if arg == "":
                sys.stdout.write("Save file name: ")
                name = sys.stdin.readline()
            elif not self.game_save_name == "":
                name = self.game_save_name

            if not name == "":
                try:
                    self.game_save.serialize(self.game_save_name)
                except:
                    print("Could not save game")
            else:
                print("Must specify a name")

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