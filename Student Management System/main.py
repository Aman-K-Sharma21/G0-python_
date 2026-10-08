"""

Required features
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
6. Exit

Each student should contain something like:

ID
Name
Age
Course
Marks

PROGRAM
│
├── display_menu()
│
├── add_student()
│
├── view_students()
│
├── search_student()
│
├── update_student()
│
├── delete_student()
│
└── main()
"""

def add_student():
    """This function is used to add student record in the list"""

    #Ask the user that how many student he want to record.
    No_of_student = int(input("How many student you want to enter : "))
    student_list = []
    for i in range(No_of_student):
        ID = int(input(f"Enter ID number of the student {i+1} : "))
        Name = input("Enter the name of the student : ")
        Age = int(input("Enter the age of the student : "))
        Course = input("Enter the name of the student's course : ")
        Marks = int(input("Enter the marks of the student : "))

        dict = {"ID" : ID , "Name" : Name, "Age" : Age , "Course" : Course , "Marks" : Marks}

        student_list.append(dict)
    return student_list


def view_all_student(list):
    if(len(list) == 0):
            print("No Student Record available!!!")
    else:
        for i,student in enumerate(list,1):
            print(f"{i} : {student}")


def search_student(list):
    if(len(list) == 0):
            print("No Student Record available!!!")
    else:
        ID_of_student = int(input("Enter the ID of the student : "))
        for i in list:
            stu_dict = i
            if ID_of_student == stu_dict["ID"]:
                print(stu_dict)

def Update_student(list):
    """
    This function is used to update the student details.
    Warning : You can only update Age,Course,Marks and ID and Name is not allowd to change .
    """

    if(len(list) == 0):
        print("No Student Record available!!!")
    else:

        ID_of_student = int(input("Enter the ID of the student which details you have to update : "))
        print("1.Age\n2.Course\n3.Marks\n ")
        update_query = int(input("Enter among(1,2,3) : "))

        if(update_query ==1):
            age = int(input("Enter the new age : "))
            for i in list:
                if ID_of_student == i["ID"]:
                    # i.update({"Age" : age})
                    i["Age"] = age
        if(update_query == 2):
            course = input("Enter the name of the course that you want to update with : ")
            for i in list:
                if ID_of_student == i["ID"]:
                    i["Course"] = course
        if(update_query == 3):
            marks = int(input("Enter the marks that you want to update with : "))
            if ID_of_student == i["ID"]:
                i["Marks"] = marks

def delete_student(list):
    ID_of_student = int(input("Enter the id of the student you want to delete from the database :"))

    for student in list:
        if student["ID"] == ID_of_student:
            list.remove(student)


def main():
    """STUDENT MANAGEMENT SYSTEM------"""
    print(f"--------------- STUDENT MANAGEMENT SYSTEM ----------------------")
    
    while(1):
        print("1. Add student\n2. View all students\n3. Search student\n4. Update student\n5. Delete student\n6. Exit")
        choice = int(input("Enter option among(1,2,3,4,5,6) : "))
        if choice == 6:
            print("Thank you for using it......")
            break
        else:
            if(choice == 1):
                list = add_student()
            elif(choice == 2):
                view_all_student(list)
            elif(choice == 3):
                search_student(list)
            elif(choice == 4):
                Update_student(list)
            elif(choice == 5):
                delete_student(list)
            else:
                print("Please Enter a valid input !!")


main()

        