import curses
from defines import (EMPTY_COLOUR, SNAKE_COLOUR, APPLE_COLOUR, TEXT_COLOUR)

EMPTY_COLOUR_ID = 1
SNAKE_COLOUR_ID = 2
APPLE_COLOUR_ID = 3
TEXT_COLOUR_ID = 4
def init_colours():
    """Sets up colours used by curses to print the board"""
    curses.start_color()
    curses.use_default_colors()
    # ID, Foreground, Background
    # Background = -1 -> Keeps the default terminal background
    curses.init_pair(EMPTY_COLOUR_ID, EMPTY_COLOUR, -1)
    curses.init_pair(SNAKE_COLOUR_ID, SNAKE_COLOUR, -1)
    curses.init_pair(APPLE_COLOUR_ID, APPLE_COLOUR, -1)
    curses.init_pair(TEXT_COLOUR_ID, TEXT_COLOUR, -1)

def init_curses():
    """
    Initializes functionalities from curses module
    Returns curses.initscr()
    """
    scr = curses.initscr()
    init_colours()
    curses.noecho()
    curses.cbreak()
    scr.nodelay(True)
    scr.keypad(True)
    curses.curs_set(0)
    return scr


def terminate_curses(scr):
    """Terminates curses functionalities"""
    scr.clear()
    scr.refresh()
    curses.curs_set(1)
    scr.keypad(False)
    scr.nodelay(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
