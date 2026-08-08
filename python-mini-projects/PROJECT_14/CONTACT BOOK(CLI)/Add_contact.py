def Add_contact():
    name = input("Enter the name of the person :").lower()
    phone_number = int(input("Enter the phone number :"))

    content = f"{name},{phone_number}\n"

    with open("contacts.txt","a") as f:
        f.write(content)
    print("----------------------Contact Added successfully-------------------")