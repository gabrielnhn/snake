from time import sleep
from curses import (KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT)
from my_curses import (init_curses, terminate_curses)
from defines import (SNAKE_CHAR, APPLE_CHAR, DELAY_TIME, EXIT_KEY,
                     LINES, COLUMNS, GAME_OVER_TIME, GAME_OVER_STRING)
from board import Board
from snake import Snake
from apple import Apple
    
from main_functions import (new_key, column_center, set_board, print_board,
                            new_position, game_over)

# setup:
scr = init_curses()
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
    sleep(DELAY_TIME)

    # process new input
    key = new_key(scr, key)
    if key == EXIT_KEY:
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

terminate_curses(scr)

# print total score:
print("Score: {}".format(score))
