"""
You are asked to implement the Builder design pattern for rendering simple chunks of code.
Sample use of the builder you are asked to create:
```
cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
```

The expected output of the above code is:

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

"""


class CodeBuilder:
    def __init__(self, root_name: str) -> None:
        """TODO: Implement this method"""
        self.root_name = root_name
        self.fields = []

    def add_field(self, field_type: str, field_value: str) -> None:
        """TODO: Implement this method"""
        self.fields.append((field_type, field_value))

    def __str__(self):
        attributes_string = ""
        for field in self.fields:
            attributes_string += f"\t\tself.{field[0]} = {field[1]}\n"
        """TODO: Implement this method"""
        return f"class {self.root_name}:\n\tdef __init__(self):\n{attributes_string}"


import unittest


class CodeBuilderTest(unittest.TestCase):
    def test_code_builder(self):
        cb = CodeBuilder(root_name="Person")
        cb.add_field("name", '""')
        cb.add_field("age", "0")

        print(cb)


if __name__ == "__main__":
    unittest.main()
