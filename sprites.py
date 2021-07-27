import pygame
from grid import CELLSIZE


def load_image(path: str, size: tuple[int, int]) -> pygame.Surface:
    """
    Load a picture from a location on the computer and resize it.
    """
    picture = pygame.image.load(path)
    return pygame.transform.scale(picture, size)


class Sprites:

    EMPTY = load_image("assets\\empty.png", (CELLSIZE, CELLSIZE))
    GRID = load_image("assets\\grid.png", (CELLSIZE, CELLSIZE))
    MINE = load_image("assets\\mine.png", (CELLSIZE, CELLSIZE))
    FLAG = load_image("assets\\flag.png", (CELLSIZE, CELLSIZE))

    GRID1 = load_image("assets\\grid1.png", (CELLSIZE, CELLSIZE))
    GRID2 = load_image("assets\\grid2.png", (CELLSIZE, CELLSIZE))
    GRID3 = load_image("assets\\grid3.png", (CELLSIZE, CELLSIZE))
    GRID4 = load_image("assets\\grid4.png", (CELLSIZE, CELLSIZE))
    GRID5 = load_image("assets\\grid5.png", (CELLSIZE, CELLSIZE))
    GRID6 = load_image("assets\\grid6.png", (CELLSIZE, CELLSIZE))
    GRID7 = load_image("assets\\grid7.png", (CELLSIZE, CELLSIZE))
    GRID8 = load_image("assets\\grid8.png", (CELLSIZE, CELLSIZE))
