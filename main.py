from game import Game
from sys import exit


if __name__ == "__main__":

    g = Game((320, 320))
    g.start()

    while g.running:
        g.update()
        g.render()

    exit()
