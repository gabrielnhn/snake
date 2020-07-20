from my_curses import (init_curses, terminate_curses)
from board import Board
from time import sleep

scr = init_curses()

board = Board()

board.set_coord(3, 3, '2')

for i, line in enumerate(board.as_list(), start=0):
    scr.addstr(i, 0, line)

scr.refresh()
sleep(5.0)

terminate_curses(scr)