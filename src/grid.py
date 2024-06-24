# grid.py

from settings import GRID_HEIGHT, GRID_WIDTH

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def check_lines(self):
        lines_cleared = 0
        for i in range(len(self.grid)):
            if all(self.grid[i]):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        return lines_cleared
