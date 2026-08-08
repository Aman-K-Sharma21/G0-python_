import viewContact
def delete_contact():
    viewContact.view_contacts()
    print("")
    name_to_delete = input("Enter the name of the person that you want to delete from the contact : ")
    
    with open("contacts.txt") as f:
        lines = f.readlines()

    with open("contacts.txt","w") as f:
        for line in lines:
            parts = line.strip().split(",")
            name = parts[0]

            if name != name_to_delete:
                f.write(line)