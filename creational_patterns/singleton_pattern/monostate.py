"""
A variation of the singleton pattern is the monostate.
It happens when you put all the state in a static variable but allowing multiple instantiations.
"""


class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55,
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} year old"


import unittest


class MonostatePattern(unittest.TestCase):
    def test_monostate_pattern(self):
        ceo1 = CEO()
        print(ceo1)

        ceo2 = CEO()
        ceo2.age = 77
        print(ceo1)
        print(ceo2)


if __name__ == "__main__":
    unittest.main()
