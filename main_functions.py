"""All major functions used by the main program are defined here:"""

import configs
def parse_configs():
    """Check whether the settings are valid"""
    try:
        if (configs.LINES < 1) or (configs.COLUMNS < 1):
            raise ValueError('Invalid size')

        elif (configs.APPLE_CHAR == configs.SNAKE_CHAR) or (
            configs.EMPTY_CHAR == configs.SNAKE_CHAR) or (
            configs.APPLE_CHAR == configs.EMPTY_CHAR):
            raise ValueError('Invalid chars')        
        
        elif configs.REFRESH_TIME <= 0:
            raise ValueError('Invalid time')

        available_colors = (COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN,
        COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW)

        if (configs.APPLE_COLOR not in available_colors) or (
            configs.SNAKE_COLOR not in available_colors) or (
            configs.EMPTY_COLOR not in available_colors) or (
            configs.TEXT_COLOR not in available_colors):
            raise ValueError('Invalid color')

    except AttributeError:
        raise Exception('Missing configs') from None


from time import sleep
import curses
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT,
                    COLOR_BLACK, COLOR_BLUE, COLOR_CYAN, COLOR_GREEN,
                    COLOR_MAGENTA, COLOR_RED, COLOR_WHITE, COLOR_YELLOW)
from my_curses import Color
from board import Board
from snake import Snake, SnakePart
from apple import Apple


# structures used by function new_key:
opposite = {KEY_DOWN: KEY_UP, KEY_UP: KEY_DOWN,
            KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT}
arrow_keys = opposite.keys()

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

def set_board(board, snake, apple):
    """
    Set up the new board to match the coordinates
    of the apple and the snake.
    """
    board.set_coord(apple.line, apple.column, apple)
    for i, j, direction in snake.coords[:-1]:
        # board.set_coord(i, j, snake)
        board.set_coord(i, j, SnakePart(direction))
    i,j,_ = snake.coords[-1]
    board.set_coord(i, j, snake.head)

def print_board_centralized(scr, board, score, terminal_lines, terminal_columns):
    """
    Same as print_board,
    but prints it in the center of the terminal.
    """
    scr.erase()
    
    for line_index, board_line in enumerate(board.as_list(),
        start=(terminal_lines//2 - (board.lines//2))):

        column_index = terminal_columns//2 - (board.columns)
        for item in board_line:
            scr.addstr(line_index, column_index, str(item),
                curses.color_pair(item.color))
            column_index += 2
    
    text = "SCORE: {}".format(score)
    scr.addstr(terminal_lines//2 - (board.lines//2) - 2,
        terminal_columns//2 - (len(text)//2), text, Color.TEXT)
    scr.refresh()


def next_coord(board, snake, key):
    """
    Return the next coordinates the snake will be
    when following the direction pointed by 'key'
    """
    i, j, _ = snake.get_head()

    if key == KEY_RIGHT:
        j += 1
        d = ">"
    elif key == KEY_LEFT:
        j += -1
        d = "<"
    elif key == KEY_UP:
        i += -1
        d = "^"
    elif key == KEY_DOWN:
        i += 1
        d = "v"
    
    return (i % board.lines, j % board.columns, d)

def game_over(scr, board, terminal_lines, terminal_columns):
    """
    The game is finished. Print GAME_OVER_MESSAGE
    for GAME_OVER_TIME seconds in the center of the screen
    """
    GAME_OVER_TIME = 3 # seconds
    GAME_OVER_MESSAGE = "GAME OVER!"

    scr.addstr(terminal_lines//2 - (board.lines//2) - 2,
        terminal_columns//2 - (len(GAME_OVER_MESSAGE)//2), 
        GAME_OVER_MESSAGE, Color.TEXT)
    scr.refresh()
    sleep(GAME_OVER_TIME)
