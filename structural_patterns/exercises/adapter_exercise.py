"""
You are given a class called `Square` and a function `calculate_area` which calculates
the are of a given rectangle.

In order to use `Square` in `calculate_area`, instead of augmenting it with widht/height members,
implement the `SquareToRectangleAdapter` class. This adapter takes a square and adapts it in such
a way that it can be used as an argument to `calculate_area`.
"""


class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square) -> None:
        # TODO
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestAdapterExercise(unittest.TestCase):
    def test_adapter_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))


if __name__ == "__main__":
    unittest.main()
