# Contact Book CLI

# Features:

# Add Contact
# Search Contact
# Delete Contact
# View Contacts

def Add_contact():
    name = input("Enter the name of the person :").lower()
    phone_number = int(input("Enter the phone number :"))

    content = f"{name},{phone_number}\n"

    with open("contacts.txt","a") as f:
        f.write(content)


def search_contact():
    view_contacts()
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



def delete_contact():
    view_contacts()
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


def view_contacts():
    with open("contacts.txt") as f:
        lines = f.readlines()

        for line in lines:
            parts = line.strip().split(",")
            print(f"name = {parts[0]} : number = {parts[1]}")
        

while(True):
    print("-"*100)
    print(" "*30,"CONTACT BOOK CLI")
    print("-"*100)
    print("")
    print(" "*30,"1.ADD CONTACT")
    print(" "*30,"2.SEARCH CONTACT")
    print(" "*30,"3.DELETE CONTACT")
    print(" "*30,"4.VIEW CONTACT")

    print("")
    try:
        user_input = int(input("WHAT ARE YOU UPTO (1,2,3,4) : "))
    except Exception as e:
        print(e)

    if (user_input == 1):
        Add_contact()
    else:
        if (user_input == 2) :
            search_contact()
        elif (user_input == 3):
            delete_contact()
        elif (user_input == 4):
            view_contacts()