"""
Most of this code was copied from online source.
http://www.darkcoding.net/software/
pretty-command-line-console-output-on-unix-in-python-and-go-lang/
"""
import sys


class Colors:
    Black = 0
    Red = 1
    Green = 2
    Yellow = 3
    Blue = 4
    Magenta = 5
    Cyan = 6
    White = 7


def bold(msg):
    return u'\033[1m%s\033[0m' % msg


def color(this_color, string, background_color=None):
    if not background_color is None:
        return str("\033[7;" + str(this_color + 30) + ";" + str(background_color + 40) + "m" + string + "\033[0m")
    else:
        return str("\033[" + str(this_color + 30) + "m" + string + "\033[0m")


def clear():
    """Clear screen, return cursor to top left"""
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()
