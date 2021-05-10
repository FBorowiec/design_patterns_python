"""
This implementation does not prevent the initializer from being called first.
Although it works it's not the preferred solution.
"""


class Database:
    _instace = None

    def __init__(self):
        print("Loading database...")

    def __new__(cls, *args, **kwargs):
        if not cls._instace:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instace


import unittest


class SingletonPattern(unittest.TestCase):
    def test_singleton_pattern(self):
        d1 = Database()
        d2 = Database()
        print("Initializer gets called twice!")

        self.assertTrue(d1 == d2)


if __name__ == "__main__":
    unittest.main()
