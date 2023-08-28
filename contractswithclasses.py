import json
import os


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.directory = os.path.dirname(os.path.abspath(__file__))
        self.python_file_path = os.path.join(
            self.directory, 'contractswithclasses.py')
        self.json_file_path = os.path.join(self.directory, 'contacts.json')
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.json_file_path, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.json_file_path, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self):
        name = input("Enter the name: ")
        number = input("Enter the number: ")
        email = input("Enter the email: ")

        for contact in self.contacts:
            if contact['number'] == number:
                print("The number already exists.")
                return

        contact = {'name': name, 'number': number, 'email': email}
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact successfully saved.")

    def delete_contact(self):
        name = input("Enter the name of the contact you want to delete: ")
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact successfully deleted.")
                return
        print("The contact was not found.")

    def edit_contact(self):
        name = input("Enter the name of the contact you want to edit: ")
        for contact in self.contacts:
            if contact['name'] == name:
                print("Contact details:")
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                print("Leave empty if you don't want to edit a field.")

                new_name = input("Enter the new name: ")
                new_number = input("Enter the new number: ")
                new_email = input("Enter the new email: ")

                if new_name:
                    contact['name'] = new_name
                if new_number:
                    contact['number'] = new_number
                if new_email:
                    contact['email'] = new_email

                self.save_contacts()
                print("Contact successfully edited.")
                return
        print("The contact was not found.")

    def search_contact(self):
        name = input("Enter the name of the contact you want to search for: ")
        for contact in self.contacts:
            if contact['name'] == name:
                print("Contact details:")
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                return
        print("The contact was not found.")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                print("------------------------")

    def run(self):
        while True:
            print("########### Choose one of the following options: ##############")
            print("1 - Add a contact")
            print("2 - Edit a contact")
            print("3 - Delete a contact")
            print("4 - Search for a contact")
            print("5 - Show all contacts")
            print("6 - Quit")

            choice = input("Enter your choice here: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.edit_contact()
            elif choice == '3':
                self.delete_contact()
            elif choice == '4':
                self.search_contact()
            elif choice == '5':
                self.show_contacts()
            elif choice == '6':
                break
            else:
                print("Invalid choice.")

        print("Program terminated.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
