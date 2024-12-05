from view_contact import view_contact

def remove_contact(all_contact):
    if not all_contact:
        print("\nContact list is Empty!!")
        return

    view_contact(all_contact)
    try:
        contact_index = int(input("\nPlease enter your remove contact in the list!! ")) - 1

        if 0 <= contact_index < len(all_contact):
            removed_contact = all_contact.pop(contact_index)
            print(f"\nContact '{removed_contact['name']}' has been removed successfully.")
        else:
            print("\nError: Invalid contact number.")
    except ValueError:
        print("\nError: Please enter a valid number.")
