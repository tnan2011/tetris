import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cell_size = 30
        self.tile_size = 30
        self.colors = Colors.get_cell_colors()
        self.grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.colors = Colors().get_cell_colors()

    def draw(self, screen):
        for rows_index in range(self.rows):
            for cols_index in range(self.cols):
                tile_rect = pygame.Rect(cols_index * self.tile_size + 1, rows_index * self.tile_size + 1, self.tile_size + 1, self.tile_size - 1)
                tile_value = self.grid[rows_index][cols_index]
                pygame.draw.rect(screen, self.colors[tile_value], tile_rect)

    def is_inside(self, block):
        tiles = block.gettiles()
        for tile in tiles:
            if (tile.row < 0 or tile.row >= self.rows or tile.column < 0 or tile.column >= self.columns):
                return False
        return True