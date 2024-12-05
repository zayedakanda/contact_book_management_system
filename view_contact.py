def view_contact(all_contact):
    if all_contact:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(all_contact, start=1):
            name = contact.get('name')
            phone = contact.get('phone')
            email = contact.get('email')
            address = contact.get('address')
            print(f"{idx}. Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print(f"Address: {address}")
            print("*" * 20)
    else:
        print("\nNo contacts available.")