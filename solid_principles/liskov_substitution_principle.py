"""
Subtypes should be immediately substitutable for their base types.
"If it looks like a duck and quacks like a duck but needs batteries,
you probably have a wrong abstraction"
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # BAD! We've just violated the Liskov Substitution Principle.
    # Any derived class should be substitutable into the "use_it(rc)" function.
    # For the square the center mechanic is broken. Setting Height also sets width and vice versa.
    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _height = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # side effects!

    area = int(w * 10)
    return area


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestLiskovSubstitution(unittest.TestCase):
    def test_rectangle_class(self):
        rc = Rectangle(2, 3)
        area = use_it(rc)
        expected_area = int(rc.width * rc.height)

        print(f"Expected an area of {expected_area}, got {area}")
        self.assertEqual(area, expected_area)

    def test_square_class(self):
        sq = Square(5)
        area = use_it(sq)
        expected_area = int(sq.width * sq.width)

        print(f"Expected an area of {expected_area}, got {area}")
        self.assertEqual(area, expected_area)


if __name__ == "__main__":
    unittest.main()