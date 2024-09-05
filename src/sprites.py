import pygame
import os

from settings import *


def load_image(name: str, size: tuple[int, int]) -> pygame.Surface:
    """
    Load an image from the assets folder and resize it.
    """
    path = os.path.join(os.path.dirname(__file__), "assets", name)
    picture = pygame.image.load(path)
    return pygame.transform.scale(picture, size)


class Sprites:

    GRID = load_image("grid.png", (CELL_SIZE, CELL_SIZE))
    GRID1 = load_image("grid1.png", (CELL_SIZE, CELL_SIZE))
    GRID2 = load_image("grid2.png", (CELL_SIZE, CELL_SIZE))
    GRID3 = load_image("grid3.png", (CELL_SIZE, CELL_SIZE))
    GRID4 = load_image("grid4.png", (CELL_SIZE, CELL_SIZE))
    GRID5 = load_image("grid5.png", (CELL_SIZE, CELL_SIZE))
    GRID6 = load_image("grid6.png", (CELL_SIZE, CELL_SIZE))
    GRID7 = load_image("grid7.png", (CELL_SIZE, CELL_SIZE))
    GRID8 = load_image("grid8.png", (CELL_SIZE, CELL_SIZE))
    EMPTY = load_image("empty.png", (CELL_SIZE, CELL_SIZE))
    FLAG = load_image("flag.png", (CELL_SIZE, CELL_SIZE))
    MINE = load_image("mine.png", (CELL_SIZE, CELL_SIZE))
    MINE_CLICKED = load_image("mine_clicked.png", (CELL_SIZE, CELL_SIZE))
