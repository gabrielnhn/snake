import curses

EMPTY_COLOUR = 1
SNAKE_COLOUR = 2
APPLE_COLOUR = 3
TEXT_COLOUR = 4
def init_colours():
    """Sets up colours used by curses to print the board"""
    curses.start_color()
    curses.use_default_colors()
    # ID, Foreground, Background
    # Background = -1 -> Keeps the default terminal background
    curses.init_pair(SNAKE_COLOUR, curses.COLOR_GREEN, -1)
    curses.init_pair(EMPTY_COLOUR, curses.COLOR_WHITE, -1)
    curses.init_pair(APPLE_COLOUR, curses.COLOR_RED, -1)
    curses.init_pair(TEXT_COLOUR, curses.COLOR_YELLOW, -1)

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
