"""
* Complicated objects (e.g., cars) aren't designed from scrath
    * They reiterate existing designs
* An existing (partially or fully constructed) desing is a Prototype
* We make a copy (clone) the prototype and customize it
    * Requires 'deep copy' support
* We make the cloning convenient (e.g., via a Factory)
"""
import copy


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


import unittest


class PrototypePattern(unittest.TestCase):
    def test_prototype_pattern(self):
        john = Person("John", Address("123 London Road", "London", "UK"))
        jane = copy.deepcopy(john)  # copy.copy - shallow copy
        jane.name = "Jane"
        jane.address.street_address = "124 London Road"
        print(john, "\n", jane)


if __name__ == "__main__":
    unittest.main()
