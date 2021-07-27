import pygame
import math
import sys

from grid import Cell, Grid, CELLSIZE
from sprites import Sprites


sys.setrecursionlimit(9999)
TILESIZE = 16


class Game:

    def __init__(self, screen_size):
        self.screen_size = self.screen_width, self.screen_height = screen_size
        self.running = False

    def start(self) -> None:
        """
        Start the game and initialize game variables.
        """
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.running = True

        self.tiles_group = pygame.sprite.Group()
        self.grid = Grid(60)


    def quit(self) -> None:
        """
        Stop the game and exit the PyGame process.
        """
        self.running = False
        pygame.quit()

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

            if event.type == pygame.MOUSEBUTTONUP:
                # mouse clicked on grid...
                pos = pygame.mouse.get_pos()
                cell_x, cell_y = pos[0] // CELLSIZE, pos[1] // CELLSIZE
                self.grid.dig(cell_x, cell_y)
       
    def render(self) -> None:
        """
        Handle the rendering portion of the games runtime.
        """
        self.screen.fill((0, 0, 0))  # fill background

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                cell = self.grid[y][x]
                sprite = Sprites.GRID
                
                if cell.mine:
                    sprite = Sprites.GRID

                if cell.visible and not cell.mine:
                    mines = self.grid.count_nearby_mines(x, y)

                    if mines == 0: sprite = Sprites.EMPTY
                    elif mines == 1: sprite = Sprites.GRID1
                    elif mines == 2: sprite = Sprites.GRID2
                    elif mines == 3: sprite = Sprites.GRID3
                    elif mines == 4: sprite = Sprites.GRID4
                    elif mines == 5: sprite = Sprites.GRID5
                    elif mines == 6: sprite = Sprites.GRID6
                    elif mines == 7: sprite = Sprites.GRID7
                    elif mines == 8: sprite = Sprites.GRID8

                elif cell.flagged:
                    sprite = Sprites.FLAG

                else:
                    sprite = Sprites.GRID

                self.screen.blit(sprite, (x * CELLSIZE, y * CELLSIZE))

        pygame.display.flip()  # update changes to PyGame window
