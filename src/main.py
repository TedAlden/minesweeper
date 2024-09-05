import pygame
import sys

from grid import Grid
from sprites import Sprites
from settings import *

sys.setrecursionlimit(9999)


class Game:

    def __init__(self, columns: int = 20, rows: int = 20, cell_size: int = 16, num_mines: int = 0):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen_size = (columns * cell_size, rows * cell_size)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.grid = Grid(columns, rows, num_mines)
        self.running = True

    def new(self) -> None:
        """
        Start the game and initialize game variables.
        """
        self.grid.new()

    def quit(self) -> None:
        """
        Stop the game and exit the PyGame process.
        """
        self.running = False

    def update(self) -> None:
        """
        Called once per frame to update the games logical state.
        """
        self.dt = self.clock.tick(0) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                # Press 'R' to restart game
                elif event.key == pygame.K_r:
                    self.new()

            if event.type == pygame.MOUSEBUTTONUP:
                if self.grid.alive:
                    cell_x = event.pos[0] // CELL_SIZE
                    cell_y = event.pos[1] // CELL_SIZE
                    # Left click to dig cell
                    if event.button == 1:
                        self.grid.dig(cell_x, cell_y)
                    # Right click to flag cell
                    elif event.button == 3:
                        self.grid.flag(cell_x, cell_y)
       
    def render(self) -> None:
        """
        Handle the rendering portion of the games runtime.
        """
        self.screen.fill((0, 0, 0))

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(self.grid[y]):
                sprite = Sprites.GRID
                if cell.visible:
                    if cell.mine:
                        if cell.clicked:
                            sprite = Sprites.MINE_CLICKED
                        else:
                            sprite = Sprites.MINE
                    else:
                        mines = self.grid.count_neighbour_mines(x, y)
                        if mines == 0: sprite = Sprites.EMPTY
                        elif mines == 1: sprite = Sprites.GRID1
                        elif mines == 2: sprite = Sprites.GRID2
                        elif mines == 3: sprite = Sprites.GRID3
                        elif mines == 4: sprite = Sprites.GRID4
                        elif mines == 5: sprite = Sprites.GRID5
                        elif mines == 6: sprite = Sprites.GRID6
                        elif mines == 7: sprite = Sprites.GRID7
                        elif mines == 8: sprite = Sprites.GRID8
                else:
                    if cell.flagged:
                        sprite = Sprites.FLAG
                    else:
                        sprite = Sprites.GRID

                self.screen.blit(sprite, (x * CELL_SIZE, y * CELL_SIZE))

        pygame.display.flip()


if __name__ == "__main__":
    g = Game(CELL_COLUMNS, CELL_ROWS, CELL_SIZE, NUM_MINES)
    g.new()
    while g.running:
        g.update()
        g.render()
    sys.exit()
