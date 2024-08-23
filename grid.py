import random

from cell import Cell


class Grid:

    def __init__(self, width: int, height: int, num_mines: int):
        self.width = width
        self.height = height
        self.num_mines = min(num_mines, self.width * self.height)
        self.alive = False
        self.__grid = None

    def __getitem__(self, y: int) -> list[Cell]:
        return self.__grid[y]

    def __setitem__(self, y: int, value: list[Cell]):
        self.__grid[y] = value

    def __len__(self) -> int:
        return len(self.__grid)

    def new(self) -> None:
        """
        Create or reset the grid to a fresh state.
        """
        self.alive = True
        self.__grid = [
            [Cell(x, y) for x in range(self.width)] for y in range(self.height)
            ]
        # Randomly place mines on grid
        mine_counter = 0
        while mine_counter < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if not self.is_mine(x, y):
                self.set_mine(x, y)
                mine_counter += 1

    def count_neighbour_mines(self, x: int, y: int) -> int:
        """
        Counts the number of mines in the surrounding 3x3 square of the
        cell (x, y).
        """
        mine_count = 0
        top = max(y - 1, 0)
        bottom = min(y + 1, self.height - 1)
        left = max(x - 1, 0)
        right = min(x + 1, self.width - 1)
        for yy in range(top, bottom + 1):
            for xx in range(left, right + 1):
                if self.is_mine(xx, yy):
                    mine_count += 1

        return mine_count
    
    def count_unvisited_cells(self) -> int:
        """
        Counts the number of cells that have not been dug yet.
        """
        cell_count = 0
        for y, row in enumerate(self.__grid):
            for x, cell in enumerate(row):
                if not cell.mine and not cell.visible:
                    cell_count += 1

        return cell_count

    def dig(self, x: int, y: int) -> None:
        """
        Dig the cell (x, y). If it is safe, expand the visible area,
        otherwise end the game if a mine has been dug.
        """
        self.__grid[y][x].clicked = True
        # Prevent player from digging up a flagged cell
        if self.__grid[y][x].flagged:
            pass
        # Player dug up a mine
        elif self.__grid[y][x].mine:
            self.alive = False
            print("You lose")
            for yy, row in enumerate(self.__grid):
                for xx, cell in enumerate(self.__grid[yy]):
                    if cell.mine:
                        cell.visible = True
        # Player dug up a safe cell
        else:
            # Flood fill to attempt to dig up safe neighbouring cells
            self.flood_fill(x, y)
            self.__grid[y][x].visible = True

        # Player wins if alive and all safe cells have been dug up
        if self.alive and self.count_unvisited_cells() == 0:
            self.alive = False
            print("You win!")

    def flag(self, x: int, y: int) -> None:
        """
        Toggle the placement of a flag at the cell (x, y), as long as it
        is not already exposed.
        """
        if not self.__grid[y][x].visible:
            self.__grid[y][x].flagged = not self.__grid[y][x].flagged

    def flood_fill(self, x: int, y: int) -> None:
        """
        Recursively flood-fill the map to expose adjacent safe cells.
        """
        # base cases for recursion
        if self.__grid[y][x].mine or self.__grid[y][x].visible:
            return

        self.__grid[y][x].visible = True
        self.__grid[y][x].flagged = False
        # If there are nearby mines to this cell, don't continue further
        if self.count_neighbour_mines(x, y) != 0:
            return

        # Recursively continue to flood-fill the grid
        if x > 0:
            self.flood_fill(x - 1, y)
        if x < len(self.__grid[0]) - 1:
            self.flood_fill(x + 1, y)
        if y > 0:
            self.flood_fill(x, y - 1)
        if y < len(self.__grid) - 1:
            self.flood_fill(x, y + 1)

    def set_mine(self, x: int, y: int) -> None:
        """
        Places a mine at (x, y).
        """
        self.__grid[y][x].mine = True

    def is_mine(self, x: int, y: int) -> bool:
        """
        Checks whether there is a mine in the cell (x, y).
        """
        return self.__grid[y][x].mine

    def set_flag(self, x: int, y: int) -> None:
        """
        Places a flag in the cell (x, y).
        """
        self.__grid[y][x].flagged = True

    def remove_flag(self, x: int, y: int) -> None:
        """
        Removes the flag in the cell (x, y).
        """
        self.__grid[y][x].flagged = False

    def is_flag(self, x: int, y: int) -> bool:
        """
        Checks whether the cell (x, y) has been flagged by the player.
        """
        return self.__grid[y][x].flagged

    def set_visible(self, x: int, y: int) -> None:
        """
        Makes the cell (x, y) visible to the player.
        """
        self.__grid[y][x].visible = True

    def is_visible(self, x: int, y: int) -> bool:
        """
        Checks whether the cell at (x, y) is visible to the player.
        """
        return self.__grid[y][x].visible
    
    def set_clicked(self, x: int, y: int) -> None:
        """
        Marks the cell (x, y) as having been clicked by the player.
        """
        self.__grid[y][x].clicked = True

    def is_clicked(self, x: int, y: int) -> bool:
        """
        Checks whether the cell at (x, y) has been clicked on by the
        player.
        """
        return self.__grid[y][x].clicked
