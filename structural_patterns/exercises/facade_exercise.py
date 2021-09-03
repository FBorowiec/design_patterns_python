"""
A magic square is a square of numbers where the sum in each row, each column, and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square. The classes are:
- Generator: this class generates a 1-dimentional list of random digits in range 1 to 9.
- Splitter: this class takes a 2d list and splits it into all possible arrangements of 1d lists.
            it gives you the columns, the rows and the two diagonals
- Verifier: this class takes a 2d list and verifies that the sum of elements in every sublist is the same.

Implement a facade class called MagicSquareGenerator which simply generates the magic square of a given size.
"""
from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for _ in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def generate(self, size):
        # todo - return a magic square of the given size
        g = Generator()
        s = Splitter()
        v = Verifier()

        while True:
            square = []
            for _ in range(size):
                square.append(g.generate(size))

            if v.verify(s.split(square)):
                break

        return square


if __name__ == "__main__":
    msg = MagicSquareGenerator()
    print(msg.generate(3))
