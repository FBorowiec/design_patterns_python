class Person:
    def __init__(self) -> None:
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth}" + f"works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self, person=Person()) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


import unittest


class BuilderFacets(unittest.TestCase):
    def test_builder_facets(self):
        pb = PersonBirthDateBuilder()
        me = pb.called("John").works_as_a("Quant").born("1/1/1980").build()

        print(me)


if __name__ == "__main__":
    unittest.main()
