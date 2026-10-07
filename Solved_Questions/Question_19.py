# Create a simple menu system:

# 1. Add student
# 2. Search student
# 3. Show all students
# 4. Exit

student_dict = {}

def Add_student(name,marks):
    student_dict[name] = marks

def Search_student(name):
    return f"The marks of {name} = {student_dict[name]}"
def show_all_student():
    for name in student_dict.keys():
        print(name)

while(True):
    print("1. Add student\n2. Search student\n3. Show all students\n4. Exit")
    choice = int(input("Enter what you want : "))

    if choice == 1:

        name = input("Enter the name of the student : ")
        marks = int(input("Enter the marks : "))
        Add_student(name,marks)
    elif choice ==2:
        name = input("Enter the name of the student : ")
        print(Search_student(name))
    elif choice == 3:
        show_all_student()
    elif choice == 4:
        break
    else:
        print("Please ! Enter a Valid input...")




