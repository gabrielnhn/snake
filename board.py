from defines import (LINES, COLUMNS, EMPTY)
import curses

class Board:
    def __init__(self):
        """Initializes the board filling 'data' with EMPTY"""
        self.lines = LINES
        self.columns = COLUMNS
        
        line = [EMPTY for j in range(COLUMNS)]
        self.data = [list(line) for i in range(LINES)]

    def get_coord(self, line, column):
        """Returns the value in (line, column)"""
        return self.data[line][column]
    
    def set_coord(self, line, column, new_value):
        """Sets the value in (line, column)"""    
        self.data[line][column] = new_value

    def as_string(self):
        """Returns its data as a string"""
        text=''
        for i in range(LINES):
            for j in range(COLUMNS):
                text += str(self.data[i][j]) + ' '
            text += '\n'
        return text
    
    def as_list(self):
        """Returns its data as a list of str(lines)"""
        l = []
        for i in range(LINES):
            line = ''
            for j in range(COLUMNS):
                line += str(self.data[i][j]) + ' ' 
            l.append(line)
        return l


# Testing
if __name__ == '__main__':
    board = Board()
    print(board.as_string())