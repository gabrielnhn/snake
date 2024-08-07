#!/usr/bin/env python3
"""
Snake game written in Python,
using 'curses' module to print the board in the terminal.

Run this file to play the game!
"""

__author__ = "Gabriel Nascarella Hishida"


from main_functions import (new_key, set_board, print_board_centralized,
                            next_coord, game_over, parse_configs)

import configs
parse_configs()

from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT, wrapper)
from my_curses import (init_curses, terminate_curses, Color)
from board import Board
from snake import Snake, SnakePart
from apple import Apple

def game(scr, board, snake, apple):
    """
    Main function used to run the game
    Take curses.initscr() as input
    Return total game score
    """

    # setup:
    terminal_too_small = False
    score = 0
    key = KEY_RIGHT

    # game loop:
    while True:    
        try:
            # adjust to any screen changes in real time
            height, width = scr.getmaxyx()
            
            if (height < configs.LINES + 4) or (width < configs.COLUMNS*2 + 3):
                # The game won't fit in anymore
                terminal_too_small = True
                break

            # print screen
            board.clear()
            set_board(board, snake, apple)
            print_board_centralized(scr, board, score, height, width)
            sleep(configs.REFRESH_TIME)

            # process new input
            key = new_key(scr, key)

            # process new game state:
            # get the next position of the snake
            i, j, d = next_coord(board, snake, key)

            next_coord_char = str(board.get_coord(i, j))

            # check thscore = -1e new position
            if next_coord_char == apple.char:
                # eat apple:
                snake.grow_to(i, j, d)
                apple.move(*board.free_random_coord())
                score += 1
            elif next_coord_char != board.Empty.char:
            # elif isinstance(next_coord_char, SnakePart):
                # bumped into itself:
                game_over(scr, board, height, width)
                break
            else:
                # empty space:
                snake.move_to(i, j, d)

        except KeyboardInterrupt:
            # stop the game
            break
    
    # return total score:
    return score, terminal_too_small
    

def main(screen):
    """
    Main program called by wrapper
    Decide whether to run the game or not, according to terminal size
    Take curses.initscr() as input
    """
    # global variables are necessary 
    # because curses.wrapper() can't forward main()'s return value
    global score
    global terminal_too_small
    # terminal_too_small will be used as
    # the 'error' value of main()

    init_curses(screen)

    # set up structures
    board = Board(configs.LINES, configs.COLUMNS)
    snake =  Snake(configs.INITIAL_SIZE, board.lines, board.columns,
                    configs.SNAKE_CHAR, Color.SNAKE)
    apple = Apple(*board.free_random_coord(), configs.APPLE_CHAR, Color.APPLE)
    
    # run the game
    score, terminal_too_small = game(screen, board, snake, apple)
    

score = 0
terminal_too_small = False

# calling the main function through wrapper, to avoid curses bugs
wrapper(main)
# wrapper calls the main function and gives it the argument curses.initscr()
# and if something happens during runtime, the terminal will be restored.

if terminal_too_small:
    print("Screen too small to run the game")

print("Score: {}".format(score))