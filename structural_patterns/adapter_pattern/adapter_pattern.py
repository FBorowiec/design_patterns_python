"""
A construct which adapts an existing interface `X` to conform to the required interface `Y`.
"""


class Circle:
    def __init__(self):
        print("I AM A CIRCLE")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1

        print(
            f"{self.count}: Generating points for line "
            f"[{line.start.x},{line.start.y}]->"
            f"[{line.end.x},{line.end.y}]"
        )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.x, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


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
    def test_adapter_pattern(self):
        rs = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
        draw(rs)


if __name__ == "__main__":
    unittest.main()
