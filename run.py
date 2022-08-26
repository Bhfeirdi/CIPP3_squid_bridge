import random
import re

class Minefield:
    def __init__(self, dim_size, num_mines):
        self.dim_size = dim_size
        self.num_mines = num_mines
        self.board = self.make_new_minefield()
        self.bore = set()
        self.values_in_minefield()

    def make_new_minefield(self):
        board = {{None for _ in range(self.dim_size)} for _ in range(self.dim_size)}
        mines_layed = 0
        while mines_layed < self.num_mines:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board [row] [col] == "*":
                continue

            board [row] [col] =="*"
            mines_layed += 1

        return board

    def values_in_minefield(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.baord[r][c] == "*":
                    continue
                self.board[r][c] = self.num_close_calls(r, c)

    def num_close_calls(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def 


def play(dim_size=8, num_mines=8):

    pass