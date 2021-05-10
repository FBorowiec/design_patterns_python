"""
Singleton pattern using a metaclass.
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print("Loading database...")


import unittest


class SingletonPattern(unittest.TestCase):
    def test_singleton_pattern(self):
        d1 = Database()
        d2 = Database()
        print("Initializer called once")

        self.assertTrue(d1 == d2)


if __name__ == "__main__":
    unittest.main()
