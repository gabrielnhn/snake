import random
from board import Board

class Apple:
    def __init__(self, line, column, char, color):
        self.line = line
        self.column = column
        self.char = char
        self.color = color
    
    def move(self, board):
        """If the apple is eaten, move itself to an available coordinate"""
        self.line, self.column = board.free_random_coord()
        
    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()