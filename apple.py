"""Apple class and methods implementation:"""

class Apple:
    """Apple to be eaten by the snake"""
    def __init__(self, line, column, char, color):
        """
        inputs:
            line, column: coordinates to spawn
            char: symbol representation
            color: `curses` color pair
        """ 
        self.line = line
        self.column = column
        self.char = char
        self.color = color
    
    def move(self, new_line, new_column):
        """Move itself to new coordinates"""
        self.line = new_line
        self.column = new_column
        
    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()