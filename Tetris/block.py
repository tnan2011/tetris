from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotate_state = 0
        self.row_offset = 0
        self.column_offset = 0
        self.colors = Colors.get_cell_colors()

    def get_tiles(self):
        tiles = self.cells[self.rotate_state]
        result = []
        for tile in tiles:
            row = tile.row
            column = tile.column
        
            result.append(Position(row + self.row_offset, column + self.column_offset))
        return result
    
    def draw(self, screen):
        tiles = self.get_tiles()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column + self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            tile_color = self.colors[self.id]
            pygame.draw.rect(screen, tile_color, tile_rect)

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns