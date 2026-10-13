"""
STUDENT MANAGEMENT SYSTEM
- Data is stored in data.json
- Loaded once at startup
- Saved every time it changes
"""

import json
import os

FILE_NAME = "data.json"


# ---------- JSON helpers ----------
def load_data():
    """Read data.json and return list of students. Empty list if no file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(students):
    """Save the list of students to data.json."""
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)


# ---------- Feature functions ----------
def add_student(students):
    """Add one or more students and save."""
    try:
        n = int(input("How many students do you want to enter: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(n):
        try:
            ID = int(input(f"Enter ID of student {i + 1}: "))
        except ValueError:
            print("ID must be a number. Skipping this one.")
            continue

        # Prevent duplicate IDs
        if any(s["ID"] == ID for s in students):
            print(f"ID {ID} already exists. Skipping.")
            continue

        Name = input("Enter name: ")
        try:
            Age = int(input("Enter age: "))
            Marks = int(input("Enter marks: "))
        except ValueError:
            print("Age/Marks must be numbers. Skipping this one.")
            continue

        Course = input("Enter course: ")

        students.append({
            "ID": ID,
            "Name": Name,
            "Age": Age,
            "Course": Course,
            "Marks": Marks
        })

    save_data(students)         
    print("Student(s) saved successfully!")


def view_students(students):
    if len(students) == 0:
        print("No student records available!")
        return
    for i, student in enumerate(students, 1):
        print(f"{i} : {student}")


def search_student(students):
    if len(students) == 0:
        print("No student records available!")
        return
    try:
        ID = int(input("Enter the ID of the student: "))
    except ValueError:
        print("ID must be a number.")
        return

    for s in students:
        if s["ID"] == ID:
            print(s)
            return
    print("Student not found.")


def update_student(students):
    """Update Age, Course or Marks (ID and Name are locked)."""
    if len(students) == 0:
        print("No student records available!")
        return

    try:
        ID = int(input("Enter the ID of the student to update: "))
    except ValueError:
        print("ID must be a number.")
        return

    # 1) Find the target student first
    target = None
    for s in students:
        if s["ID"] == ID:
            target = s
            break

    if target is None:
        print("Student not found.")
        return

    # 2) Ask what to change
    print("1. Age\n2. Course\n3. Marks")
    try:
        choice = int(input("Enter (1,2,3): "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        target["Age"] = int(input("Enter new age: "))
    elif choice == 2:
        target["Course"] = input("Enter new course: ")
    elif choice == 3:
        target["Marks"] = int(input("Enter new marks: "))
    else:
        print("Invalid choice.")
        return

    # 3) Save the change
    save_data(students)
    print("Updated successfully!")


def delete_student(students):
    if len(students) == 0:
        print("No student records available!")
        return

    try:
        ID = int(input("Enter the ID to delete: "))
    except ValueError:
        print("ID must be a number.")
        return

    for s in students:
        if s["ID"] == ID:
            students.remove(s)
            save_data(students)     
            print("Deleted successfully!")
            return

    print("Student not found.")


# ---------- Main menu ----------
def main():
    print("--------------- STUDENT MANAGEMENT SYSTEM ----------------------")
    students = load_data()           

    while True:
        print("\n1. Add student\n2. View all students\n3. Search student"
              "\n4. Update student\n5. Delete student\n6. Exit")
        try:
            choice = int(input("Enter option (1-6): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 1:
            add_student(students)
        elif choice == 2:
            view_students(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            update_student(students)
        elif choice == 5:
            delete_student(students)
        elif choice == 6:
            print("Thank you for using it......")
            break
        else:
            print("Please enter a valid input!!")


main()