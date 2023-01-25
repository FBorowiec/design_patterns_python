from typing import Any


class Event(list[Any]):
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
    def can_vote(self) -> bool:
        return self._age >= 18

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if self._age == value:
            return

        old_can_vote: bool = self.can_vote

        self._age = value
        self.property_changed("age", value)

        if old_can_vote != self.can_vote:
            self.property_changed("can_vote", self.can_vote)


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
        def person_changed(name: str, value: str) -> None:
            if name == "can_vote":
                print(f"Voting ability chnaged to {value}")

        p: Person = Person(0)
        p.property_changed.append(person_changed)

        for age in range(16, 22):
            print(f"Changing age to {age}")
            p.age = age


if __name__ == "__main__":
    unittest.main()
