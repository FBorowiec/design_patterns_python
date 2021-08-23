"""
You are given a class called `Person`.
The person has two attrivtues: `id`, and `name`.
Please implement a `PersonFactory` that has a non-static `creat_person()` method that takes a person's name
and return a person initialized with this name and an id.

The `id` of the person should be set as a 0-based index of the object created.
So the first person the factory makes should have id=0, second id=1 and so on.
"""


class Person:
    def __init__(self, id_: int, name: str):
        self.id_ = id_
        self.name = name


class PersonFactory:
    person_index = 0

    def create_person(self, name: str):
        """TODO: implement this function"""
        p = Person(self.person_index, name)
        self.person_index += 1
        return p


import unittest


class PersonFactoryTest(unittest.TestCase):
    def test_create_person(self):
        """"""


if __name__ == "__main__":
    unittest.main()
