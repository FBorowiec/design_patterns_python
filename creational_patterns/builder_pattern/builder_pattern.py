"""
* Some objects are simple and can be created in a single initializer call
* Other objects require a lot of time to create
* Having an object with 10 initializer arguments is not productive
* Instead, opt for piecewise construction
* Builder provides and API for constructing an object step-by-step

Builder - When piecewise object construction is complicated,
          provide and API for doing it succinctly

# This is a bad way of creating html code in this case
words = ["hello", "world"]
parts = ["<ul>"]
for w in words:
    parts.append(f"  <li>{w}<li>")
parts.append("</ul>")
print('\n'.join(parts))

"""
import unittest


class HtmlElement:
    INDENT_SIZE: int = 2

    def __init__(self, name: str = "", text: str = ""):
        self.text: str = text
        self.name: str = name
        self.elements: list[HtmlElement] = []

    def to_string(self, indent: int) -> str:
        lines: list[str] = []
        i: str = " " * (indent * self.INDENT_SIZE)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.INDENT_SIZE)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.to_string(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.to_string(0)


class HtmlBuilder:
    def __init__(self, root_name: str):
        self.root_name: str = root_name
        self.__root: HtmlElement = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name: str, child_text: str) -> "HtmlBuilder":
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)

    @staticmethod
    def create(name: str) -> "HtmlBuilder":
        return HtmlBuilder(name)


class BuilderPattern(unittest.TestCase):
    def test_builder_pattern(self) -> None:
        builder: HtmlBuilder = HtmlBuilder("ul")
        # builder.add_child("li", "hello")
        # builder.add_child("li", "world")
        builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
        print("Ordinary builder:\n", builder)


if __name__ == "__main__":
    unittest.main()
