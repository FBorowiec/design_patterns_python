"""
A. High-level modules should not depend on low-level modules.
   Both should depend on abstractions.
B. Abstractions should not depend on details.
   Details should depend on abstractions.
*Abstractions - Interfaces or Base classes
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []  # bad if the relations change type! (ex. to a dictionary)

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, child))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module
    # BAD
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f"John has a child called {r[2].name}.")

    # GOOD
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}.")


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestDependencyInjection(unittest.TestCase):
    def test_dependency_injection(self):
        parent = Person("John")
        child1 = Person("Chris")
        child2 = Person("Matt")

        relationships = Relationships()
        relationships.add_parent_and_child(parent, child1)
        relationships.add_parent_and_child(parent, child2)


if __name__ == "__main__":
    unittest.main()
