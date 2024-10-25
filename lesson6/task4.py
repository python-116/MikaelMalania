# Address Book with inner classes

class AddressBook:
    def __init__(self) -> None:
        self.entries = []

    def add_entry(self, name: str, email: str):
        entry = self.Entry(name, email)
        self.entries.append(entry)

    class Entry:
        def __init__(self, name: str, email: str) -> None:
            self.name = name
            self.email = email


my_address_book = AddressBook()

my_address_book.add_entry("John", "john.johnson@gmail.com")
my_address_book.add_entry("Mary", "mary.smith@gmail.com")

for entry in my_address_book.entries:
    print(f"Name: {entry.name}, Email: {entry.email}")
