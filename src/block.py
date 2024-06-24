# block.py

from random import randint, choice

SHAPES = [
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

class Block:
    COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 165, 0)]

    def __init__(self, grid):
        self.grid = grid
        self.shape = choice(SHAPES)
        self.color_index = randint(1, len(self.COLORS) - 1)
        self.color = self.COLORS[self.color_index]
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.i = 0
        self.j = len(self.grid[0]) // 2 - self.width // 2
        self.fill()

    def fill(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.shape[i][j]:
                    self.grid[self.i + i][self.j + j] = self.color_index

    def erase(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.shape[i][j]:
                    self.grid[self.i + i][self.j + j] = 0

    def move_left(self):
        if self.j > 0 and all(self.grid[self.i + i][self.j + j - 1] == 0 for i in range(self.height) for j in range(self.width) if self.shape[i][j]):
            self.erase()
            self.j -= 1
            self.fill()

    def move_right(self):
        if self.j + self.width < len(self.grid[0]) and all(self.grid[self.i + i][self.j + j + 1] == 0 for i in range(self.height) for j in range(self.width) if self.shape[i][j]):
            self.erase()
            self.j += 1
            self.fill()

    def move_down(self):
        if self.i + self.height < len(self.grid) and all(self.grid[self.i + i + 1][self.j + j] == 0 for i in range(self.height) for j in range(self.width) if self.shape[i][j]):
            self.erase()
            self.i += 1
            self.fill()

    def can_fall(self):
        return self.i + self.height < len(self.grid) and all(self.grid[self.i + i + 1][self.j + j] == 0 for i in range(self.height) for j in range(self.width) if self.shape[i][j])

    def rotate(self):
        new_shape = [[self.shape[y][x] for y in range(self.width - 1, -1, -1)] for x in range(self.height)]
        if self.j + len(new_shape[0]) > len(self.grid[0]) or self.i + len(new_shape) > len(self.grid):
            return  # Rotation would place block out of grid bounds, so skip
        self.erase()
        self.shape = new_shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.fill()


