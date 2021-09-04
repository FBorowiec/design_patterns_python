"""
A construct which adapts an existing interface `X` to conform to the required interface `Y`.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(_):
    """You are given this API"""
    print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()

        print(
            f"Generatign points for line "
            f"[{line.start.x},{line.start.y}]->"
            f"[{line.end.x},{line.end.y}]"
        )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.x, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])


def draw(rcs):
    print("\n\n--Drawing--\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestAdapterPattern(unittest.TestCase):
    def test_dependency_injection(self):
        rs = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
        draw(rs)


if __name__ == "__main__":
    unittest.main()
