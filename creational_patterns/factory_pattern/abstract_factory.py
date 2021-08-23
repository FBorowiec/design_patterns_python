"""
If you have a hierarchy of types you can have a hierarchy of factories
"""
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Optional


class HotDrink(ABC):
    def consume(self) -> None:
        """Abstract consume method"""


class Tea(HotDrink):
    def consume(self) -> None:
        print("This tea is delicious")


class Coffee(HotDrink):
    def consume(self) -> None:
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount: float) -> HotDrink:
        """Abstract prepare method"""


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: float) -> Tea:
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: float) -> Coffee:
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


def make_drink(drink_type: str) -> Optional[HotDrink]:
    if drink_type == "tea":
        return TeaFactory().prepare(200)
    elif drink_type == "coffee":
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    factories = []
    initialized = False

    class AvailableDrink(Enum):  # violates Open-Close Principle
        COFFEE = auto()
        TEA = auto()

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self) -> HotDrink:
        print("Available drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}: ")
        idx = int(s)
        a = input("Specify amount: ")
        amount = int(a)
        return self.factories[idx][1].prepare(amount)


import unittest
from unittest.mock import patch


class AbstractFactoryPattern(unittest.TestCase):
    def test_abstract_factory_pattern(self):
        entry = "tea"
        drink = make_drink(entry)
        if drink is not None:
            drink.consume()

    @patch("builtins.input")
    def test_hot_drink_machine_test(self, input_mock):
        input_mock.side_effect = ["0", "80"]

        hdm = HotDrinkMachine()
        hdm.make_drink()


if __name__ == "__main__":
    unittest.main()
