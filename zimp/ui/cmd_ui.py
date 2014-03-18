import cmd
import dbm
import os.path
from zimp.engine.gamestate import GameState
import sys


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

    def help_load(self):
        if self.state == CmdUiState.Startup:
            print("Loads a previous game given a file name")
        else:
            print("")

    def do_load(self, arg):
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
        self.game_save = GameState()
        self.state = CmdUiState.Loaded
        self.game_save_name = arg

    def help_save(self):
        if self.state > CmdUiState.Loaded:
            print("Saves the current game state. Optional argument of save file name")
        else:
            print("")

    def do_save(self, arg):
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


if __name__ == "__main__":
    ui = CmdUi()
    ui.startup()
    ui.cmdloop()