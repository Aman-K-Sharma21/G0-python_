# Student Management System

class student :
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll = roll_no
        self.marks = marks

    def calgrade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >=75 :
            return "B"
        elif self.marks >=60 :
            return "C"
        elif self.marks >=45 :
            return "D"
        else :
            return "F"
        
    def display_info(self):
        print(f"\n ---Student Report Card---")
        print(f"Name : {self.name}")
        print(f"Roll number : {self.roll}")
        print(f"Marks : {self.marks}")


print("=== Student Management System ===")
s_name = input("Enter Student Name: ")
s_roll = input("Enter Roll Number: ")
s_marks = float(input("Enter Marks Obtained: "))

# Creating the object using your constructor
student_profile = student(s_name, s_roll, s_marks)

while True:
    print("\n1. Display Student Info\n2. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        # Call the display method here
        student_profile.display_info()
    elif choice == "2":
        print("Exiting System. Data cleared!")
        break
    else:
        print("Invalid Choice!")
        