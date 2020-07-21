import curses
from defines import (SNAKE_COLOUR, EMPTY_COLOUR, APPLE_COLOUR, TEXT_COLOUR)

def init_colours():
    """Sets up the colours the program will use."""
    curses.start_color()
    curses.use_default_colors()
    # Number, Foreground, Background
    curses.init_pair(SNAKE_COLOUR, curses.COLOR_GREEN, -1)
    curses.init_pair(EMPTY_COLOUR, curses.COLOR_WHITE, -1)
    curses.init_pair(APPLE_COLOUR, curses.COLOR_RED, -1)
    curses.init_pair(TEXT_COLOUR, curses.COLOR_YELLOW, -1)

def init_curses():
    """Initializes the curses functionalities the program will use."""
    scr = curses.initscr()
    init_colours()
    curses.noecho()
    curses.cbreak()
    scr.nodelay(True)
    scr.keypad(True)
    curses.curs_set(0)
    return scr


def terminate_curses(scr):
    """Terminates the processes the program doesn't need to use anymore."""
    scr.clear()
    scr.refresh()
    curses.curs_set(1)
    scr.keypad(False)
    scr.nodelay(False)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
