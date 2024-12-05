
def search_contact(all_contact):
    if not all_contact:  # Check if the list is empty
        print("\nNo contacts to search.")
        return

    search_query = input("\nEnter a name, phone, or email to search: ").lower()  # Get the search query

    results = []
    for contact in all_contact:
        name = contact.get('name', '').lower()
        phone = contact.get('phone', '').lower()
        email = contact.get('email', '').lower()

        # Check if the search query matches name, phone, or email
        if search_query in name or search_query in phone or search_query in email:
            results.append(contact)

    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact.get('address')}")
            print("-" * 30)
    else:
        print("\nNo contacts found matching your search.")