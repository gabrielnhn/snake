from time import sleep
import curses
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT)
from my_curses import (init_curses, terminate_curses, 
                       EMPTY_COLOR_ID, TEXT_COLOR_ID)
from configs import (REFRESH_TIME, GAME_OVER_TIME, GAME_OVER_MESSAGE)
from board import Board, Empty
from snake import Snake
from apple import Apple

# structures used by function new_key:
opposite = {KEY_DOWN: KEY_UP, KEY_UP: KEY_DOWN,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT}
    # stores the opposite key for each arrow key
arrow_keys = opposite.keys()
    # stores arrow keys

def new_key(scr, old_key):
    """
    Return the keyboard key the loop will process,
    according to the current 'getch()' input or old key.
    Also flush input stream if get the same key twice
    """
    new_value = scr.getch()
    
    if (new_value == -1) or (
        new_value == old_key) or (
        new_value == opposite[old_key]) or (
        new_value not in arrow_keys):
        # if there's no new input (-1)
        # or it's the same value of the old key
        # or it's the opposite direction to where the snake was going
        # or it's not an arrow key

        curses.flushinp()
        return old_key
    else:
        return new_value


def column_center(columns, text):
    """
    When printing 'text', use this function to center it
    relatively to the board.
    """
    return (columns // 2) + (len(text) // 2) - 1

def set_board(board, snake, apple):
    """
    Set up the new board to match the coordinates
    of the apple and the snake.
    """
    board.set_coord(apple.line, apple.column, apple)
    for i, j in snake.coords:
        board.set_coord(i, j, snake)

def print_board(scr, board, score):
    """
    Print every value in the board,
    matching each of them with its color.
    Also print the current score
    """
    scr.erase()
    for line_index, board_line in enumerate(board.as_list(), start=0):
        column = 0
        for item in board_line:
            scr.addstr(line_index, column, str(item), curses.color_pair(item.color))
            column += 2
    
    text = "SCORE: {}".format(score)
    scr.addstr(board.lines + 1, column_center(board.columns, text) + 1, text, TEXT_COLOR_ID)
    scr.refresh()


def new_position(board, snake, key):
    """
    Return the next coordinates the snake will be
    when following the direction pointed by 'key'
    """
    i, j = snake.get_head()

    if key == KEY_RIGHT:
        j += 1
    elif key == KEY_LEFT:
        j += -1
    elif key == KEY_UP:
        i += -1
    elif key == KEY_DOWN:
        i += 1
    
    return (i % board.lines, j % board.columns)

def game_over(scr, board):
    """
    The game is finished. Print GAME_OVER_MESSAGE
    for GAME_OVER_TIME at the center of the screen
    """
    scr.addstr(board.lines + 2, column_center(board.columns, GAME_OVER_MESSAGE),
    GAME_OVER_MESSAGE, TEXT_COLOR_ID)
    scr.refresh()
    sleep(GAME_OVER_TIME)
