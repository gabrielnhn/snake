"""Snake class and methods implementation:"""


class SnakePart:
    def __init__(self, char):
    
        self.char = char
        self.color = 2

    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()

class Head(SnakePart):
    def __init__(self):
        super().__init__(char="@")

class Snake:
    def __init__(self, size, lines, columns, char, color):
        """
        Initializes the snake in the center of the board,
        With an initial 'size'
        """
        if size > columns:
            raise ValueError("Snake's size is too large")
        
        self.coords = [(lines//2 - 1, columns//2 + x - 1, ">") for x in range(-size + 1, 1) ]
        self.char = char
        self.color = color
        self.head = Head()

    def move_to(self, line, column, direction=None):
        """Move the snake to (line, column)."""
        self.coords.pop(0)
        if direction:
            self.coords.append((line, column, direction))
        else:
            self.coords.append((line, column))

    def grow_to(self, line, column, direction=None):
        """Move the snake to (line, column) increasing its size by 1."""
        if direction:
            self.coords.append((line, column, direction))
        else:
            self.coords.append((line, column))

    def get_head(self):
        """Return the last coordinate."""
        return self.coords[-1]

    def __repr__(self):
        return self.char

    def __str__(self):
        return self.__repr__()