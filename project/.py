# Phonebook dictionary
phonebook = {}

# take input if name is already in phonebook
def new_name(name,number):
     name = input("Enter contact name: ")
            if name in phonebook:
                print({name},"is already taken")

# Function to add a new contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact {name} has been added.")

# Function to search for a contact
def search_contact(name):
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} has been deleted.")
    else:
        print(f"Contact {name} not found.")

# Function to list all contacts
def list_contacts():
    if phonebook:
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

# Main program loop
def main():
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            if name in phonebook:
                print({name},"is already taken")

            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1