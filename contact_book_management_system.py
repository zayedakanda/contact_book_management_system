import add_contact_save
import view_contact
import remove_contact
import search_contact

all_contact = []

while True:
    print("\nWelcome to Your Contacts Book Management System!")
    print("\nMenu ID: 1. Add a New Contact.")
    print("Menu ID: 2. View Contacts.")
    print("Menu ID: 3. Remove a Contact.")
    print("Menu ID: 4. Search a Contact.")
    print("Menu ID: 5. Exit.")

    menu = input("\nSelect a Number: ")

    if menu == "1":
        all_contact = add_contact_save.add_contact(all_contact)
    elif menu == "2":
        view_contact.view_contact(all_contact)
    elif menu == "3":
        all_contact = remove_contact.remove_contact(all_contact)
    elif menu == "4":
        search_contact.search_contact(all_contact)
    elif menu == "5":
        print("\nThanks for using our Contact Book Management System!")
        break
    else:
        print("Please select a valid number.")

