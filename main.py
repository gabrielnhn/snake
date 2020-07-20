from my_curses import (init_curses, terminate_curses)
from time import sleep
from board import Board

scr = init_curses()

board = Board()

for i, line in enumerate(board.as_list(), start=0):
    scr.addstr(i, 0, line)

scr.refresh()
sleep(5.0)

terminate_curses(scr)