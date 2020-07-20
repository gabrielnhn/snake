from defines import (LINES, COLUMNS, EMPTY)
import curses

class Board:
    def __init__(self):
        self.lines = LINES
        self.columns = COLUMNS
        
        line = [EMPTY for j in range(COLUMNS)]
        self.data = [line for i in range(LINES)]

    def as_string(self):
        text=''
        for i in range(LINES):
            for j in range(COLUMNS):
                text += str(self.data[i][j]) + ' '
            text += '\n'
        return text
    
    def as_list(self):
        l = []
        for i in range(LINES):
            line = ''
            for j in range(COLUMNS):
                line += str(self.data[i][j]) + ' ' 
            l.append(line)
        return l


# Testing
if __name__ == "__main__":
    board = Board()
    print(board.as_matrix())