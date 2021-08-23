"""
* Use when object creation logic becomes too convoluted
* Initializer is not descriptive
    * Name is always `__init__`
    * Cannot overload with same sets of arguments wieh different names
    * Can turn into 'optional parameter hell'
* Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to
    * A separate method (Factory Method)
    * That may exist in a separate class (Factory)
    * Can create hierarchy of factories with Abstract Factory

Factory - It is a component responsible solely for the wholesale (non-piecewise creation of objects).
"""

import math
from enum import Enum


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class PointBad:
    """
    This kind of breaks the open-close principle and is increasingly difficult to expand with new coordnate systems
    """

    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * math.sin(b)
            self.y = a * math.cos(b)


class PointGood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    @staticmethod
    def new_cartesian_point(x, y):
        return PointGood(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return PointGood(rho * math.cos(theta), rho * math.sin(theta))


import unittest


class FactoryPattern(unittest.TestCase):
    def test_factory_pattern(self):
        p = PointGood(2, 3)
        p2 = PointGood.new_polar_point(1, 2)
        print(p, p2)


if __name__ == "__main__":
    unittest.main()
