"""Module used to manage the 'curses' module"""
import curses
from configs import (EMPTY_COLOR, SNAKE_COLOR, APPLE_COLOR, TEXT_COLOR)

class Color:
    """Enum for object colors"""
    EMPTY = 1
    SNAKE = 2
    APPLE = 3
    TEXT = 4

def init_colors():
    """Sets up colors used by curses to print the board"""
    curses.start_color()
    curses.use_default_colors()
    # ID, Foreground, Background
    # Background = -1 -> Keeps the default terminal background
    curses.init_pair(Color.EMPTY, EMPTY_COLOR, -1)
    curses.init_pair(Color.SNAKE, SNAKE_COLOR, -1)
    curses.init_pair(Color.APPLE, APPLE_COLOR, -1)
    curses.init_pair(Color.TEXT, TEXT_COLOR, -1)


def init_curses(scr):
    """
    Initializes functionalities from curses module.
    Takes curses.initscr() as input.
    """
    init_colors()
    curses.noecho()
    curses.cbreak()
    scr.nodelay(True)
    scr.keypad(True)
    curses.curs_set(0)


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
