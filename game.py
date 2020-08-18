"""
Snake game written in Python!
Uses 'curses' module to print the board in the terminal.

Written by Gabriel Nascarella Hishida.
Star the repository if you like it!
Feel free to send any feedback.
"""

from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT, wrapper)
from my_curses import (init_curses, terminate_curses, Color)
import configs
from board import Board
from snake import Snake
from apple import Apple
from main_functions import (new_key, set_board, print_board,
                            next_coord, game_over)

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
                apple.move(board)
                score += 1
            elif next_coord_char == snake.char:
                # bumped into itself:
                game_over(scr, board)
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
    # score will be used like
    # a return value of main()

    init_curses(screen)

    height, width = screen.getmaxyx()
    if (height < configs.LINES + 3) or (width < configs.COLUMNS + 1):
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
    
    terminate_curses(screen)
    

# calling the main function through wrapper, to avoid curses bugs
wrapper(main)
# wrapper calls the main function and gives it the argument curses.initscr()
# and if something happens during runtime, the terminal will be restored.
if score >= 0:
    print("Score: {}".format(score))
else:
    print("Screen too small to run the game")