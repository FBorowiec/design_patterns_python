import copy


class Address:
    def __init__(self, suite, city, street_address):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, {self.suite}, {self.city}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            proto=EmployeeFactory.main_office_employee, name=name, suite=suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            proto=EmployeeFactory.aux_office_employee, name=name, suite=suite
        )


import unittest


class PrototypePattern(unittest.TestCase):
    def test_prototype_pattern(self):
        john = EmployeeFactory.new_main_office_employee("John", 101)
        jane = EmployeeFactory.new_aux_office_employee("Jane", 505)
        print(john)
        print(jane)


if __name__ == "__main__":
    unittest.main()
