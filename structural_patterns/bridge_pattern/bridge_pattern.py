"""
A Bridge is a mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
"""

# circle square - shapes
# vector raster - forms
# How to draw them with a scalable approach?
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        """"""

    @abstractmethod
    def render_square(self, side):
        """"""


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")

    def render_square(self, side):
        print(f"Drawing a sqaure of side {side}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_square(self, side):
        print(f"Drawing pixels for a sqaure of side {side}")


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        """"""

    @abstractmethod
    def resize(self, factor):
        """"""


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestBridgePattern(unittest.TestCase):
    def test_bridge_pattern(self):
        raster = RasterRenderer()
        vector = VectorRenderer()

        circle_vector = Circle(vector, 5)
        circle_vector.draw()
        circle_vector.resize(2)
        circle_vector.draw()

        circle_raster = Circle(raster, 4)
        circle_raster.draw()
        circle_raster.resize(3)
        circle_raster.draw()


if __name__ == "__main__":
    unittest.main()
