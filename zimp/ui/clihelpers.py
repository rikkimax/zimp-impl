"""
Most of this code was copied from online source.
http://www.darkcoding.net/software/pretty-command-line-console-output-on-unix-in-python-and-go-lang/
"""
import sys


class Colors:
    Black = 30
    Red = 31
    Green = 32
    Yellow = 33
    Blue = 34
    Magenta = 35
    Cyan = 36
    White = 37


def bold(msg):
    return u'\033[1m%s\033[0m' % msg


def color(this_color, string):
    return str("\033[" + str(this_color) + "m" + string + "\033[0m")


def clear():
    """Clear screen, return cursor to top left"""
    sys.stdout.write('\033[2J')
    sys.stdout.write('\033[H')
    sys.stdout.flush()