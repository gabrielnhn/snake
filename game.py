"""
Snake game written in Python!
Uses 'curses' module to print the board in the terminal.

Written by Gabriel Nascarella Hishida.
Star the repository if you enjoy it!
Feel free to send any feedback.
"""

from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT, wrapper)
from my_curses import (init_curses, terminate_curses)
from configs import (SNAKE_CHAR, APPLE_CHAR, REFRESH_TIME, EXIT_KEY,
                     LINES, COLUMNS, GAME_OVER_TIME, GAME_OVER_MESSAGE)
from board import Board
from snake import Snake
from apple import Apple
from main_functions import (new_key, column_center, set_board, print_board,
                            new_position, game_over)


def game(scr):
    """
    Main function used to run the game
    Takes curses.initscr() as input
    Returns total game score
    """

    # setup:
    score = 0
    snake = Snake()
    apple = Apple()
    key = KEY_RIGHT

    # game loop:
    while True:    
        # print screen
        board = Board()
        set_board(board, snake, apple)
        print_board(scr, board, score)
        sleep(REFRESH_TIME)

        # process new input
        key = new_key(scr, key)
        if chr(key) == EXIT_KEY:
            break

        # process new game state:
        # get next position
        i, j = new_position(snake, key)

        new_position_char = board.get_coord(i, j)

        # check new position
        if new_position_char == APPLE_CHAR:
            # eat apple:
            snake.increase_to(i, j)
            score += 1
        elif new_position_char == SNAKE_CHAR:
            # bumped into itself:
            game_over(scr)
            break
        else:
            # empty space:
            snake.move_to(i, j)

        # check if apple was eaten:
        apple.check(board)

    
    # return total score:
    return score
    

def main(screen):
    """
    Main program called by wrapper
    Decides whether to run the game or not, according to terminal size
    Takes curses.initscr() as input
    """
    global score

    init_curses(screen)
    height, width = screen.getmaxyx()

    if (height < LINES + 3) or (width < COLUMNS + 1):
        terminate_curses(screen)
        print("Terminal too small in order to play the game")

    else:
        score = game(screen)
        terminate_curses(screen)

# calling the main function through wrapper, to avoid curses bugs
wrapper(main)
# wrapper calls the main function and gives it the argument curses.initscr()
# and if something happens during runtime, the terminal will be restored.
print("Score: {}".format(score))
