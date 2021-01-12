"""
Do not create interface that are too large.
YAGNI - You Ain't Going to Need It!
"""
from abc import abstractmethod


# Bad - wrong application approach
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        pass  # noop

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")


# Good - small implementations of each applications
class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    @abstractmethod
    def print(self, document):
        self.printer.print(document)

    @abstractmethod
    def scan(self, document):
        self.scanner.scan(document)


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestInterfaceSegregation(unittest.TestCase):
    def test_interface_segregation(self):
        old_machine = OldFashionedPrinter()
        with self.assertRaises(NotImplementedError):
            old_machine.scan("my_document")

        photocopier = Photocopier()
        photocopier.scan("my_document")


if __name__ == "__main__":
    unittest.main()
