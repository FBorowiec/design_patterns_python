"""
We need to be informed when certain things happen:
    - object's property changes
    - object's does something
    - some external event happens

We want to listen to events and be notified when they occur:
    - Notifications should include useful data

Want to unsubscribe from events if we don't need them anymore

OBSERVER:
    An observer is an object that wishes to be informed about events happening in the system.
    The entity generating the events is an observable.

    - It is an intrusive approach: an observable must provide an event to subscribe to.
    - Subscription and unsubscritption handled with addtiohn/removal of items in a list.
    - Property notifications are easy; dependent property notifications are tricky.
"""
from typing import Any


class Event(list[Any]):
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str):
        self.name: str = name
        self.address: str = address
        self.falls_ill: Event = Event()

    def catch_a_cold(self) -> None:
        self.falls_ill(name=self.name, address=self.address)


def call_doctor(name: str, address: str) -> None:
    print(f"{name} is ill and lives at {address}. Call a doctor!")


import unittest


class ObserverPattern(unittest.TestCase):
    def test_observer_pattern(self) -> None:
        person = Person("John", "123 London Road")
        person.falls_ill.append(call_doctor)
        person.catch_a_cold()


if __name__ == "__main__":
    unittest.main()
