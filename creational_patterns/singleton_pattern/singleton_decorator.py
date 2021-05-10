"""
This is a better implementation that uses a decorator and prevents the initializer
from being called multiple times.
"""


def singleton(class_):
    _instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)
        return _instances[class_]

    return get_instance


@singleton
class Database:
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
