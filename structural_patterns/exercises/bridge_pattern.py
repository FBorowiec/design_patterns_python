"""
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Refactor this hierarchy, giving the base class `Shape` a constructor that takes an interface `Renderer` defined as:

```bash
class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
```
As well as `VectorRenderer` and `RasterRenderer` classes. Each inheritor of the `Shape` abstract class should have
a constructor that takes a `Renderer` such that, subsequently, each constructed object's `__str__()` operates
correctly, for example:
`str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
"""
from abc import ABC

# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


class Shape(ABC):
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return "Drawing %s as %s" % (self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, "Triangle")


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, "Square")


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


import unittest


class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), "Drawing Square as lines")

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), "Drawing Triangle as pixels")
