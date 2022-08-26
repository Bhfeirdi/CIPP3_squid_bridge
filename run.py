import random

class Minefield:
    def __init__(self, dim_size, num_mines):
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = self.make_new_minefield()
        self.bore = set()


    def make_new_minefield(self):
        board = {{None for _ in range(self.dim_size)} for _ in range(self.dim_size)}
        mines_layed = 0
        while mines_layed < self.num_mines:
            loc = random.


def play(dim_size=8, num_mines=8):

    pass