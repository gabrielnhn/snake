"""
Snake game written in Python,
using 'curses' module to print the board in the terminal.

Execute this file to run the game.

Written by Gabriel Hishida.

Star the repository if you like it!
Feel free to send any feedback.
"""

from main_functions import (new_key, set_board, print_board_centralized,
                            next_coord, game_over, parse_configs)

import configs
parse_configs()

from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT, wrapper)
from my_curses import (init_curses, terminate_curses, Color)
from board import Board
from snake import Snake
from apple import Apple

def game(scr, board, snake, apple):
    """
    Main function used to run the game
    Take curses.initscr() as input
    Return total game score
    """

    # setup:
    score = 0
    key = KEY_RIGHT

    # game loop:
    while True:    
        try:
            # adjust to any screen changes in real time
            height, width = scr.getmaxyx()
            
            if (height < configs.LINES + 4) or (width < configs.COLUMNS*2 + 3):
                # The game won't fit in anymore
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
            i, j = next_coord(board, snake, key)

            next_coord_char = str(board.get_coord(i, j))

            # check the new position
            if next_coord_char == apple.char:
                # eat apple:
                snake.grow_to(i, j)
                apple.move(*board.free_random_coord())
                score += 1
            elif next_coord_char == snake.char:
                # bumped into itself:
                game_over(scr, board, height, width)
                break
            else:
                # empty space:
                snake.move_to(i, j)

        except KeyboardInterrupt:
            # stop the game
            break
    
    # return total score:
    return score
    

def main(screen):
    """
    Main program called by wrapper
    Decide whether to run the game or not, according to terminal size
    Take curses.initscr() as input
    """
    global score
    # score will be used as if it was
    # the return value of main()

    init_curses(screen)

    height, width = screen.getmaxyx()
    if (height < configs.LINES + 4) or (width < configs.COLUMNS*2 + 3):
        # The game won't fit in the standard screen
            score = -1

    else:
        # set up structures
        board = Board(configs.LINES, configs.COLUMNS)
        snake =  Snake(configs.INITIAL_SIZE, board.lines, board.columns,
                       configs.SNAKE_CHAR, Color.SNAKE)
        apple = Apple(*board.free_random_coord(), configs.APPLE_CHAR, Color.APPLE)
        
        # run the game
        score = game(screen, board, snake, apple)
    

# calling the main function through wrapper, to avoid curses bugs
wrapper(main)
# wrapper calls the main function and gives it the argument curses.initscr()
# and if something happens during runtime, the terminal will be restored.
if score < 0:
    print("Screen too small to run the game")
else:
    print("Score: {}".format(score))