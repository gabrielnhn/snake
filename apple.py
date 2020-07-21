import random
from board import Board
from defines import (LINES, COLUMNS, APPLE_CHAR, SNAKE_CHAR)

class Apple:
    def __init__(self):
        """Initializes new random apple."""
        self.line = random.randrange(LINES)
        self.column = random.randrange(COLUMNS)
    
    def check(self, board):
        """If the apple is eaten, changes its position to somewhere free."""
        while board.get_coord(self.line, self.column) == SNAKE_CHAR:
            self.line = random.randrange(LINES)
            self.column = random.randrange(COLUMNS)
