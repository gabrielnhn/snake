from time import sleep
import curses
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT)
from my_curses import (init_curses, terminate_curses)
from defines import (SNAKE_CHAR, APPLE_CHAR, DELAY_TIME, EXIT_KEY,
                     LINES, COLUMNS, GAME_OVER_TIME, GAME_OVER_STRING)
from board import Board
from snake import Snake
from apple import Apple

opposite = {KEY_DOWN: KEY_UP, KEY_UP: KEY_DOWN,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT}

def new_key(scr, old_key):
    new_value = scr.getch()
    if (new_value == -1) or (new_value == opposite[old_key]):
        return old_key
    else:
        return new_value

def set_board(board, snake, apple):
    board.set_coord(apple.line, apple.column, APPLE_CHAR)
    for i, j in snake.coords:
        board.set_coord(i, j, SNAKE_CHAR)

def column_center(text):
    return (COLUMNS // 2) + (len(text) // 2) - 1

def print_board(scr, board, score):
    scr.erase()
    for index, board_line in enumerate(board.as_list(), start=0):
        scr.addstr(index, 0, board_line)
    

    text = "SCORE: {}".format(score)
    scr.addstr(LINES + 1, column_center(text) + 1, text)
    scr.refresh()


def new_position(snake, key):
    i, j = snake.get_head()

    if key == KEY_RIGHT:
        j += 1
    elif key == KEY_LEFT:
        j += -1
    elif key == KEY_UP:
        i += -1
    elif key == KEY_DOWN:
        i += 1
    
    return (i % LINES, j % COLUMNS)

def game_over(scr):
    scr.addstr(LINES + 2, column_center(GAME_OVER_STRING), GAME_OVER_STRING)
    scr.refresh()
    sleep(GAME_OVER_TIME)
