import random
from enum import Enum


WIDTH = 20
HEIGHT = 20
CELLSIZE = 16


class Cell:

    def __init__(self, mine: bool = False,
                 flagged: bool = False,
                 visible: bool = False):
                 
        self.mine = mine
        self.flagged = flagged
        self.visible = visible


class Grid:

    def __init__(self, num_mines: int):
        self.grid = [[Cell() for x in range(WIDTH)] for y in range(HEIGHT)]

        assert num_mines < WIDTH * HEIGHT, \
                "Cannot place more mines than there are cells"

        # randomly place mines
        for _ in range(num_mines):
            while True:
                x = random.randint(0, WIDTH - 1)
                y = random.randint(0, HEIGHT - 1)

                if not self.is_mine(x, y):
                    self.place_mine(x, y)
                    break

    def __getitem__(self, y: int) -> list[Cell]:
        return self.grid[y]

    def __setitem__(self, y: int, value: list[int]):
        self.grid[y] = value

    def __len__(self) -> int:
        return len(self.grid)

    def count_nearby_mines(self, x: int, y: int) -> int:
        """
        Counts the number of mines in the surrounding 3x3 square of the
        cell (x, y).
        """
        top = max(y - 1, 0)
        bottom = min(y + 1, HEIGHT - 1)
        left = max(x - 1, 0)
        right = min(x + 1, WIDTH - 1)
        count = 0

        for _y in range(top, bottom + 1):
            for _x in range(left, right + 1):
                if self.is_mine(_x, _y):
                    count += 1

        return count

    def dig(self, x, y):
        """
        Dig the cell (x, y). If it is safe, expand the visible area,
        otherwise end the game if a mine has been dug.
        """
        self.flood_fill(x, y) # attempt to fill in any nearby safe cells
        self.grid[y][x].visible = True

    def flood_fill(self, x: int, y: int) -> None:
        """
        Recursively flood-fill the map to expose adjacent safe cells in
        the Minesweeper fashion.
        """
        # base cases for recursion
        if self.grid[y][x].mine or self.grid[y][x].visible:
            return

        self.grid[y][x].visible = True
        # if there are nearby mines to this cell, don't continue further
        if self.count_nearby_mines(x, y) != 0:
            return

        # recursively continue to flood-fill the grid
        if x > 0:
            self.flood_fill(x - 1, y)
        if x < len(self.grid[0]) - 1:
            self.flood_fill(x + 1, y)
        if y > 0:
            self.flood_fill(x, y - 1)
        if y < len(self.grid) - 1:
            self.flood_fill(x, y + 1)

    def place_mine(self, x: int, y: int) -> None:
        """
        Places a mine at (x, y).
        """
        self.grid[y][x].mine = True

    def is_mine(self, x: int, y: int) -> bool:
        """
        Checks whether there is a mine in the cell (x, y).
        """
        return self.grid[y][x].mine

    def place_flag(self, x: int, y: int) -> None:
        """
        Places a flag in the cell (x, y).
        """
        self.grid[y][x].flagged = True

    def remove_flag(self, x: int, y: int) -> None:
        """
        Removes the flag in the cell (x, y).
        """
        self.grid[y][x].flagged = False

    def is_flagged(self, x: int, y: int) -> bool:
        """
        Checks whether the cell (x, y) has been flagged by the player.
        """
        return self.grid[y][x].flagged

    def set_visible(self, x: int, y: int) -> None:
        """
        Makes the cell (x, y) visible to the player.
        """
        self.grid[y][x].visible = True

    def is_visible(self, x: int, y: int) -> bool:
        """
        Checks whether the cell at (x, y) is visible to the player.
        """
        return self.grid[y][x].visible
