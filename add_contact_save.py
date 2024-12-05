import csv

def save_contact(all_contact):
    file_name = 'all_contact.csv'

    with open(file_name, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(all_contact)

def add_contact(all_contact):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    for contact in all_contact:
        if contact['phone'] == phone:
            print(f"Error: The phone number {phone} already exists in the contact list.")
            return all_contact

    new_contact = {
        "name": name.upper(),
        "phone": phone,
        "email": email,
        "address": address.title()
    }

    all_contact.append(new_contact)
    save_contact(all_contact)
    print(f"Contact for {name} added successfully and saved to CSV File!")

    return all_contact
