# ui.py

import pygame
from pygame.locals import *
from settings import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT
from high_score import get_high_score, save_high_score
from themes import ThemeManager

class UI:
    def __init__(self, theme_manager, grid_height=GRID_HEIGHT, cell_size=CELL_SIZE):
        self.cell_size = cell_size
        self.colors = theme_manager.get_colors()  # Use get_colors() to get the theme colors
        self.background = self.colors['background']  # Access background color directly from colors
        self.grid_color = self.colors['grid']  # Access grid color directly from colors
        self.grid_height = grid_height
        self.score = 0
        self.high_score = get_high_score()

        pygame.init()
        self.screen = pygame.display.set_mode((GRID_WIDTH * cell_size, grid_height * cell_size))
        pygame.display.set_caption('Tetris')

        self.font = pygame.font.Font(None, 36)  # Define a font for text rendering

        self.clock = pygame.time.Clock()

    def _convert_color(self, color):
        return color  # Assuming colors are already in RGB format

    def draw_grid(self, grid):
        self.screen.fill(self._convert_color(self.background))
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell_type = grid[row][col]
                rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                if cell_type == 0:
                    color = self.colors['empty_cell']
                else:
                    color = self.colors['cell'][cell_type]
                pygame.draw.rect(self.screen, self._convert_color(color), rect)

    def update_score(self, lines_cleared):
        self.score += lines_cleared * 10
        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)  # Save high score to file or database

    def update_score_display(self):
        text = f"Score: {self.score}  High Score: {self.high_score}"
        text_surface = self.font.render(text, True, self._convert_color(self.colors['text']))
        self.screen.blit(text_surface, (10, 10))  # Adjust position as needed

    def draw_next_block(self, block):
        color_index = block.color
        if isinstance(color_index, int) and color_index < len(self.colors['cell']):
            color = self.colors['cell'][color_index]
        else:
            color = (255, 255, 255)  # Default to white if color index is out of range or not an integer

        for i in range(len(block.shape)):
            for j in range(len(block.shape[0])):
                if block.shape[i][j] == 1:
                    rect = pygame.Rect((j + block.j) * self.cell_size, (i + block.i) * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, self._convert_color(color), rect)

    def update(self):
        pygame.display.flip()
        self.clock.tick(30)  # Cap FPS to 30

    def display_message(self, message, color):
        text_surface = self.font.render(message, True, self._convert_color(color))
        self.screen.blit(text_surface, ((GRID_WIDTH * self.cell_size - text_surface.get_width()) // 2, (GRID_HEIGHT * self.cell_size - text_surface.get_height()) // 2))

    def clear_screen(self):
        self.screen.fill(self._convert_color(self.background))

    def quit(self):
        pygame.quit()
