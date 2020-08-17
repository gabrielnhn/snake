"""
Snake game written in Python!
Uses 'curses' module to print the board in the terminal.

Written by Gabriel Nascarella Hishida.
Star the repository if you enjoy it!
Feel free to send any feedback.
"""

from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT, wrapper)
from my_curses import (init_curses, terminate_curses, SNAKE_COLOR_ID, APPLE_COLOR_ID)
from configs import (INITIAL_SIZE, SNAKE_CHAR, APPLE_CHAR, REFRESH_TIME,
                     LINES, COLUMNS, GAME_OVER_TIME, GAME_OVER_MESSAGE)
from board import Board
from snake import Snake
from apple import Apple
from main_functions import (new_key, column_center, set_board, print_board,
                            new_position, game_over)


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
            # print screen
            board.clear()
            set_board(board, snake, apple)
            print_board(scr, board, score)
            sleep(REFRESH_TIME)

            # process new input
            key = new_key(scr, key)

            # process new game state:
            # get next position
            i, j = new_position(board, snake, key)

            new_position_char = str(board.get_coord(i, j))

            # check new position
            if new_position_char == apple.char:
                # eat apple:
                snake.grow_to(i, j)
                score += 1
            elif new_position_char == snake.char:
                # bumped into itself:
                game_over(scr, board)
                break
            else:
                # empty space:
                snake.move_to(i, j)

            # check if apple was eaten:
            apple.check(board)

        except KeyboardInterrupt:
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

    init_curses(screen)

    height, width = screen.getmaxyx()
    if (height < LINES + 3) or (width < COLUMNS + 1):
    # The game won't fit in the standard screen
        score = -1

    else:
        board = Board(LINES, COLUMNS)
        snake =  Snake(INITIAL_SIZE, board.lines, board.columns, SNAKE_CHAR, SNAKE_COLOR_ID)
        apple = Apple(*board.free_random_coord(), APPLE_CHAR, APPLE_COLOR_ID)

        score = game(screen, board, snake, apple)
    
    terminate_curses(screen)
    

# calling the main function through wrapper, to avoid curses bugs
wrapper(main)
# wrapper calls the main function and gives it the argument curses.initscr()
# and if something happens during runtime, the terminal will be restored.
if score >= 0:
    print("Score: {}".format(score))
else:
    print("Screen too small to run the game")