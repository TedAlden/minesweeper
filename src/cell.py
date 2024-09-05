from dataclasses import dataclass


@dataclass
class Cell:
    column: int
    row: int
    mine: bool = False
    flagged: bool = False
    visible: bool = False
    clicked: bool = False
