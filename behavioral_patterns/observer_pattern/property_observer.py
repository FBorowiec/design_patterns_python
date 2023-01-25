from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        for item in self:
            item(*args, **kwargs)


class PropertyOservable:
    def __init__(self) -> None:
        self.property_changed: Event = Event()


class Person(PropertyOservable):
    def __init__(self, age: int) -> None:
        super().__init__()
        self._age: int = age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)


class TrafficAuthority:
    def __init__(self, person: Person) -> None:
        self.person: Person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name: str, value: Any) -> None:
        if name == "age":
            if value < 18:
                print("No driving license for you!")
            else:
                print("Here's your driving license, enjoy!")
                self.person.property_changed.remove(self.person_changed)


import unittest


class ObserverPattern(unittest.TestCase):
    def test_observer_pattern(self) -> None:
        person: Person = Person(0)
        _: TrafficAuthority = TrafficAuthority(person)
        for age in range(16, 22):
            print(f"Setting age to {age}")
            person.age = age


if __name__ == "__main__":
    unittest.main()
