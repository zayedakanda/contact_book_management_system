import csv
from contact_book_management_system import all_contact

def load_contact():
    try:
        with open("all_contact.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                contact = {
                    "name": row[0],
                    "phone": row[1],
                    "email": row[2],
                    "address": row[3]
                }
                all_contact.append(contact)
    except FileNotFoundError:
        print("No previous contact file found!!!")

    return all_contact