"""
The system should be open to extensions (for example with inheritance) but closed to modifications
"""
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    """
    Adding another filter function violates the Open-Close Principle!
    The modification should be added via extension and not via modification
    """

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    """
    Doesn't scale well!
    """

    def filter_by_size_color(self, products, size, color):
        for p in products:
            if p.size == size and p.size == size:
                yield p


"""
It's much better to have a separate Specification and Filter class
"""


class Specification:
    def if_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def if_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def if_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.if_satisfied(item):
                yield item


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestOpenClosePrinciple(unittest.TestCase):
    def setUp(self):
        super().setUp()

        apple = Product("Apple", Color.GREEN, Size.SMALL)
        tree = Product("Tree", Color.GREEN, Size.LARGE)
        house = Product("House", Color.BLUE, Size.LARGE)

        self.products = [apple, tree, house]

    def test_old_approach(self):
        # OLD APPROACH
        pf = ProductFilter()
        print("Green products (old):")
        for p in pf.filter_by_color(self.products, Color.GREEN):
            print(f"- {p.name} is green")

    def test_new_approach(self):
        # NEW APPROACH
        bf = BetterFilter()
        print("Green products (new):")
        green = ColorSpecification(Color.GREEN)
        for p in bf.filter(self.products, green):
            print(f"- {p.name} is green")

        print("Large products:")
        large = SizeSpecification(Size.LARGE)
        for p in bf.filter(self.products, large):
            print(f"- {p.name} is large")

        print("Large and Blue items:")
        large_blue = large & ColorSpecification(Color.BLUE)
        for p in bf.filter(self.products, large_blue):
            print(f"- {p.name} is large and blue")


if __name__ == "__main__":
    unittest.main()
