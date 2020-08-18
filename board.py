from configs import (EMPTY_CHAR, EMPTY_COLOR)
import random

class Empty:
    char = EMPTY_CHAR
    color = EMPTY_COLOR

    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()

class Board:
    def __init__(self, lines, columns):
        """
        Initializes the board filling 'data' with EMPTY_CHAR.
        'data' is a list of lists.
        """
        self.lines = lines
        self.columns = columns
        self.clear()

    def clear(self):
        """Clear the data of the board"""
        empty_line = [Empty() for j in range(self.columns)]
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

        if str(self.get_coord(free_line, free_column)) != Empty.char:
            # if the random coordinate above is not empty,
            # find the next coordinate available
            for _ in range(self.lines):
                for _ in range(self.columns):
                    free_column = (free_column + 1) % self.columns
                    if str(self.get_coord(free_line, free_column)) == Empty.char:
                        break
                free_line = (free_line + 1) % self.lines
            
        return free_line, free_column

    def as_list(self):
        """Return its data as a list of lists."""
        return self.data

    def __str__(self):
        """Return its data as a string."""
        text=''
        for i in range(self.lines):
            for j in range(self.columns):
                text += str(self.data[i][j]) + ' '
            text += '\n'
        return text
