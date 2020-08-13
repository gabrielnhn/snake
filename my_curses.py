import curses
from defines import (EMPTY_COLOR, SNAKE_COLOR, APPLE_COLOR, TEXT_COLOR)

EMPTY_COLOR_ID = 1
SNAKE_COLOR_ID = 2
APPLE_COLOR_ID = 3
TEXT_COLOR_ID = 4
def init_colors():
    """Sets up colors used by curses to print the board"""
    curses.start_color()
    curses.use_default_colors()
    # ID, Foreground, Background
    # Background = -1 -> Keeps the default terminal background
    curses.init_pair(EMPTY_COLOR_ID, EMPTY_COLOR, -1)
    curses.init_pair(SNAKE_COLOR_ID, SNAKE_COLOR, -1)
    curses.init_pair(APPLE_COLOR_ID, APPLE_COLOR, -1)
    curses.init_pair(TEXT_COLOR_ID, TEXT_COLOR, -1)

def init_curses():
    """
    Initializes functionalities from curses module
    Returns curses.initscr()
    """
    scr = curses.initscr()
    init_colors()
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
