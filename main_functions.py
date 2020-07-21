from time import sleep
import curses
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT)
from my_curses import (init_curses, terminate_curses)
from defines import (SNAKE_CHAR, APPLE_CHAR, SNAKE_COLOUR, APPLE_COLOUR,
                     EMPTY_COLOUR, TEXT_COLOUR,
                     DELAY_TIME, EXIT_KEY, LINES, COLUMNS,
                     GAME_OVER_TIME, GAME_OVER_STRING)
from board import Board
from snake import Snake
from apple import Apple

opposite = {KEY_DOWN: KEY_UP, KEY_UP: KEY_DOWN,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT}
    # dictionary used by function new_key

def new_key(scr, old_key):
    """
    Returns the key the loop will process,
    according to the current input or the old key.
    """
    new_value = scr.getch()
    if (new_value == -1) or (new_value == opposite[old_key]):
        return old_key
    else:
        return new_value

def set_board(board, snake, apple):
    """
    Sets up the new board to match the coordinates
    of the apple and the snake
    """
    board.set_coord(apple.line, apple.column, APPLE_CHAR)
    for i, j in snake.coords:
        board.set_coord(i, j, SNAKE_CHAR)

def column_center(text):
    """
    When printing 'text', use this function to center it
    relatively to the board.
    """
    return (COLUMNS // 2) + (len(text) // 2) - 1


def print_board(scr, board, score):
    """
    Prints every value in the board,
    matching each of them with its colour.
    Also prints the current score.
    """
    scr.erase()
    for line_number, board_line in enumerate(board.as_list(), start=0):
        column = 0
        for char in board_line.split():
            if char == SNAKE_CHAR:
                scr.addstr(line_number, column, char, curses.color_pair(SNAKE_COLOUR))
            elif char == APPLE_CHAR:
                scr.addstr(line_number, column, char, curses.color_pair(APPLE_COLOUR))
            else:
                scr.addstr(line_number, column, char, curses.color_pair(EMPTY_COLOUR))
            column += 2
    


    text = "SCORE: {}".format(score)
    scr.addstr(LINES + 1, column_center(text) + 1, text, TEXT_COLOUR)
    scr.refresh()


def new_position(snake, key):
    """
    Returns the next coordinates the snake will be
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
    
    return (i % LINES, j % COLUMNS)

def game_over(scr):
    """
    The game is finished. Prints GAME_OVER_STRING
    for GAME_OVER_TIME at the center of the screen
    """
    scr.addstr(LINES + 2, column_center(GAME_OVER_STRING),
    GAME_OVER_STRING, TEXT_COLOUR)
    scr.refresh()
    sleep(GAME_OVER_TIME)
