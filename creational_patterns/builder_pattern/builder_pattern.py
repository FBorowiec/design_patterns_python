"""
* Some objects are simple and can be created in a single initializer call
* Other objects require a lot of time to create
* Having an object with 10 initializer arguments is not productive
* Instead, opt for piecewise construction
* Builder provides and API for constructing an object step-by-step

Builder - When piecewise object construction is complicated,
          provide and API for doing it succinctly
"""

"""
# This is a bad way of creating html code in this case

words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f"  <li>{w}<li>")
parts.append("</ul>")
print('\n'.join(parts))

"""


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.text = text
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self):
        return str(self.__root)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


import unittest


class BuilderPattern(unittest.TestCase):
    def test_builder_pattern(self):
        builder = HtmlBuilder("ul")
        # builder.add_child("li", "hello")
        # builder.add_child("li", "world")
        builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
        print("Ordinary builder:\n", builder)


if __name__ == "__main__":
    unittest.main()
