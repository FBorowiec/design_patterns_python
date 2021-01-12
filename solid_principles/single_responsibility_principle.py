"""
A given class should be responsible only for doing one thing and one thing only.
Or in other words a class should only have one reason to change.
Separation of concerns - different classes handling different, independent tasks/problems.
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    """
    Breaking the Single Responsibility Principle by adding more functionalities
    """

    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        # Some implementation...
        pass

    def load_from_web(self, url):
        # Some implementation...
        pass


"""
A better idea is to use another class for handling that type of operations
"""


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


# TEST--------------------------------------------------------------------------------------------|

import unittest


class TestJournalPersistenceManager(unittest.TestCase):
    def test_journal_persistence_manager(self):
        j = Journal()
        j.add_entry("I cried today.")
        j.add_entry("I ate a bug")
        print(f"Journal entries:\n{j}")


if __name__ == "__main__":
    unittest.main()
