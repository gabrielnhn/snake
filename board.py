"""Board and Empty classes and methods implementation:"""

from configs import (EMPTY_CHAR, EMPTY_COLOR)
import random

class Board:
    """Board structure, a matrix implemented on a list of lists"""
    class Empty:
        """Empty item class"""
        char = EMPTY_CHAR
        color = EMPTY_COLOR
        def __init__(self):
            pass

        def __repr__(self):
            return self.char

        def __str__(self):
            return self.__repr__()

    def __init__(self, lines, columns):
        """
        Initializes the board filling 'data' with EMPTY_CHAR.
        'data' is a list of lists.
        """
        self.lines = lines
        self.columns = columns
        self.empty = self.Empty()
        self.clear()

    def clear(self):
        """Clear the data of the board"""
        empty_line = [self.empty for j in range(self.columns)]
        self.data = [list(empty_line) for i in range(self.lines)]
            
    def get_coord(self, line, column):
        """Return the value in (line, column)"""
        return self.data[line][column]
    
    def set_coord(self, line, column, new_value):
        """Set the value in (line, column)."""    
        self.data[line][column] = new_value

    def free_random_coord(self):
        """Get a random coordinate available in the board"""
        free_line = random.randrange(self.lines)
        free_column = random.randrange(self.columns)

        if str(self.get_coord(free_line, free_column)) != self.empty.char:
            # if the random coordinate above is not empty,
            # find the next available coordinate
            for _ in range(self.lines):
                available = False
                for _ in range(self.columns):
                    free_column = (free_column + 1) % self.columns
                    if str(self.get_coord(free_line, free_column)) == self.empty.char:
                        available = True
                        break
                if available:
                    break
                free_line = (free_line + 1) % self.lines
            
        return free_line, free_column

    def as_list(self):
        """Return its data as a list of lists."""
        return list(self.data)

    def __str__(self):
        """Return its data as a string."""
        text=''
        for i in range(self.lines):
            for j in range(self.columns):
                text += str(self.data[i][j]) + ' '
            text += '\n'
        return text
