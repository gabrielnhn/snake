from configs import (LINES, COLUMNS, INITIAL_SIZE)

class Snake:
    def __init__(self):
        """
        Initializes the snake in the center of the board,
        with size INITIAL_SIZE.
        """
        self.coords = [(LINES//2 - 1, COLUMNS//2 + x - 1) for x in range(-INITIAL_SIZE + 1, 1) ]

    def move_to(self, line, column):
        """Moves the snake to (line, column)."""
        self.coords.pop(0)
        self.coords.append((line, column))

    def increase_to(self, line, column):
        """Moves the snake to (line, column) increasing its size by 1."""
        self.coords.append((line, column))

    def get_head(self):
        """Returns last coordinate."""
        return self.coords[-1]

# Testing
if __name__ == "__main__":
    snake = Snake()
    print(snake.coords)