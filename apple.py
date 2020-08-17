import random
from board import Board

class Apple:
    def __init__(self, line, column, char, color):
        self.line = line
        self.column = column
        self.char = char
        self.color = color
    
    def check(self, board):
        """If the apple is eaten, change its position to an available coord"""
        if board.get_coord(self.line, self.column) != self:
            self.line, self.column = board.free_random_coord()
        
    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()