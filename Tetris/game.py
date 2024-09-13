from grid import Grid
from blocks import *

class Game:
    def __init__(self):
        self.score = 0
        self.grid = Grid()
        self.current_block = TBlock()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
    
    def moveDown(self):
        self.current_block.move(rows = 1, columns = 0)

    def get_score(self):
        return 0
    
    def moveLeft(self):
        self.current_block.move(rows = 0, columns = -1)
        if not self.grid.is_inside(self.current_block):
            self.moveRight

    def moveRight(self):
        self.current_block.move(rows = 0, columns = 1)
        if not self.grid.is_inside(self.current_block):
            self.moveLeft