def main():
    contacts = []
    continue_ = True
    while continue_:
        choice = int(input("\nContacts\
        \n========\
        \n1. View Contacts\
        \n2. Add new contact\
        \n3. Search\
        \n4. Update contact\
        \n5. Delete Contact\
        \n6. Quit\
        \nEnter choice number\
        \n>>"))
        if choice == 1:
            view(contacts)
            continue_ = get_menu_choice()
        elif choice == 2:
            add(contacts)
            continue_ = get_menu_choice()
        elif choice == 3:
            search(contacts)
            continue_ = get_menu_choice()
        elif choice == 4:
            update(contacts)
            continue_ = get_menu_choice()
        elif choice == 5:
            delete(contacts)
            continue_ = get_menu_choice()
        elif choice == 6:
            break

def add(contacts):
    contact = {}
    contact["name"] = input("\nEnter a name\
    \n>>")
    contact["number"] = input("\nEnter a number\
    \n>>")
    contacts.append(contact)


def  get_menu_choice():
    choice2 = int(input("\n1. Return to menu\
    \n2. Quit\
    \n>>"))
    return choice2 == 1

def delete(contacts):
    choice = input("enter a name\n>>")
    if len(contacts) == 0:
        print("name not found")
        return
    for contact in contacts:
        if choice == contact['name']:
            contacts.remove(contact)
            break

def search(contacts):
    name = input("Enter a name\n>>")
    if len(contacts) == 0:
        print("name not found")
        return
    for contact in contacts:
        if name == contact['name']:
            print(f"{contact['name']} {contact['number']}\n")
        elif name != contact['name']:
            print("no names")
            return

def update(contacts):
    name = input("Enter a name\n>>")
    if len(contacts) == 0:
        print("name not found")
        return
    for contact in contacts:
        if name == contact['name']:
            number = input("Enter a new number\n>>")
            contact['number'] = number
            break
        elif name != contact['name']:
            print("name is not found")
            continue

    #add contact, update bob which doesnt exist, add bob, update bob again, something wrong

def view(contacts):
    if len(contacts) == 0:
        print("There are no contacts")
        return
    for contact in contacts:
        print(f"\n{contact['name']} {contact['number']}\n")

main()