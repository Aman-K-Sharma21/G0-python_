import Add_contact,SearchContact,DeleteContact,viewContact


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
        Add_contact.Add_contact()
    else:
        if (user_input == 2) :
            SearchContact.search_contact()
        elif (user_input == 3):
            DeleteContact.delete_contact()
        elif (user_input == 4):
            viewContact.view_contacts()