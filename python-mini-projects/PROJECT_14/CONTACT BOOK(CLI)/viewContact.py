def view_contacts():
    with open("contacts.txt") as f:
        lines = f.readlines()

        for line in lines:
            parts = line.strip().split(",")
            print(f"name = {parts[0]} : number = {parts[1]}")