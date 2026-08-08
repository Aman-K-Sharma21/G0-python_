import viewContact
def search_contact():
    viewContact.view_contacts()
    print("")
    search_number = input("Enter the name of the person :").lower()
    with open("contacts.txt") as f:
        # lines = f.readlines()
        # print(lines[0])
        
        # print(f.readline())
        # print(f.readline())

        # lines = f.readlines()
        for line in f:
            # Remove the hidden newline character from the line
            clean_line = line.strip() 
        
        # Split the line into name and number
            parts = clean_line.split(",")
            name = parts[0]
            number = parts[1]

            if(name == search_number):
                print(f"Name : {name}\nPhone number : {number}")
                break
        else:
            print(f"{search_number} is not in the contact list.")