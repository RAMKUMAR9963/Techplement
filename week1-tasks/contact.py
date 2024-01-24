import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

def display_contacts(contacts):
    print("\nContacts List:")
    for name, details in contacts.items():
        print(f"Name: {name}, \nPhone: {details['phone']}, \nEmail: {details['email']}")

def add_contact(contacts):
    print("\nAdd Contact:")
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    if len(name) == 0 or len(phone) == 0 or len(email) == 0:
        print("Error: Name, Phone, and Email are mandatory fields.")
        return

    if not phone.isdigit() or len(phone) != 10:
        print("Error: Invalid phone number.")
        return

    if "@" not in email or "." not in email:
        print("Error: Invalid email address.")
        return

    if name in contacts:
        print("Error: Contact already exists.")
        return

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully.")

def search_contact(contacts):
    print("\nSearch Contact:")
    name = input("Enter Name to search: ")

    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    print("\nUpdate Contact:")
    name = input("Enter Name to update: ")

    if name in contacts:
        phone = input("Enter New Phone: ")
        email = input("Enter New Email: ")

        if not phone.isdigit() or len(phone) != 10:
            print("Error: Invalid phone number.")
            return

        if "@" not in email or "." not in email:
            print("Error: Invalid email address.")
            return

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System Menu:")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
