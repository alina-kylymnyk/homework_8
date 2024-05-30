import pickle


# Реалізуйте функціонал для збереження стану AddressBook
# у файл при закритті програми і відновлення стану при її запуску.
class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, address):
        self.contacts[name] = address

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

    def list_contacts(self):
        return self.contacts

    def __str__(self):
        return '\n'.join([f"{name}: {address}" for name, address in self.contacts.items()])


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


# Інтеграція збереження та завантаження в основний цикл

def main():
    book = load_data()  # Завантаження даних з файлу

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Remove Contact")
        print("4. List Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            book.add_contact(name, address)
            print("Contact added successfully.")
        elif choice == '2':
            name = input("Enter name: ")
            print(book.get_contact(name))
        elif choice == '3':
            name = input("Enter name: ")
            book.remove_contact(name)
            print("Contact removed successfully.")
        elif choice == '4':
            print(book)
        elif choice == '5':
            save_data(book)  # Збереження даних у файл перед виходом
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
