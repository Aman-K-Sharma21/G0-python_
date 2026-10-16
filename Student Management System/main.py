"""
STUDENT MANAGEMENT SYSTEM
--------------------------
Features:
    1. Add student
    2. View all students
    3. Search student
    4. Update student
    5. Delete student
    6. Exit

Data is stored in data.json.
Loaded once at startup, saved after every change.
"""

import json
import os

FILE_NAME = "data.json"


# =====================================================================
# STUDENT CLASS
# =====================================================================
class Student:
    """Represents one student and knows how to display, grade, and update itself."""

    MIN_MARKS = 0
    MAX_MARKS = 100
    MIN_PASS = 40

    def __init__(self, ID, Name, Age, Course, Marks):
        self.ID = ID
        self.Name = Name
        self.Age = Age
        self.Course = Course
        self.Marks = self._validate_marks(Marks)

    # ---------- 1. DISPLAY ----------
    def display(self):
        """Print this student's information in a neat format."""
        print(f"ID     : {self.ID}")
        print(f"Name   : {self.Name}")
        print(f"Age    : {self.Age}")
        print(f"Course : {self.Course}")
        print(f"Marks  : {self.Marks}")
        print(f"Grade  : {self.calculate_grade()}")

    # ---------- 2. GRADE / RESULT ----------
    def calculate_grade(self):
        """Return a letter grade based on marks."""
        m = self.Marks
        if m >= 90:
            return "A+"
        elif m >= 80:
            return "A"
        elif m >= 70:
            return "B"
        elif m >= 60:
            return "C"
        elif m >= 50:
            return "D"
        elif m >= 40:
            return "E"
        else:
            return "F (Fail)"

    def is_pass(self):
        """Return True if the student passed."""
        return self.Marks >= self.MIN_PASS

    # ---------- 3. UPDATE MARKS (with validation) ----------
    def update_marks(self, new_marks):
        """Change marks only if they are valid. Returns True on success."""
        self.Marks = self._validate_marks(new_marks)
        return True

    # ---------- helper ----------
    def _validate_marks(self, marks):
        """Check that marks are a number between MIN_MARKS and MAX_MARKS."""
        if not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")
        if not (self.MIN_MARKS <= marks <= self.MAX_MARKS):
            raise ValueError(
                f"Marks must be between {self.MIN_MARKS} and {self.MAX_MARKS}."
            )
        return marks

    # ---------- JSON helpers ----------
    def to_dict(self):
        """Convert this Student into a plain dict so json.dump can save it."""
        return {
            "ID": self.ID,
            "Name": self.Name,
            "Age": self.Age,
            "Course": self.Course,
            "Marks": self.Marks,
        }

    @classmethod
    def from_dict(cls, data):
        """Build a Student from a dict that came out of JSON."""
        return cls(data["ID"], data["Name"], data["Age"], data["Course"], data["Marks"])

    # ---------- pretty printing ----------
    def __str__(self):
        return f"Student({self.ID}, {self.Name}, {self.Course}, Marks={self.Marks})"

    def __repr__(self):
        return self.__str__()


# =====================================================================
# JSON HELPERS
# =====================================================================
def load_data():
    """Read data.json and return a list of Student objects. Empty list if no file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            raw = json.load(f)                      # list of dicts
        return [Student.from_dict(d) for d in raw]  # → list of Students
    except json.JSONDecodeError:
        return []


def save_data(students):
    """Save a list of Student objects to data.json."""
    with open(FILE_NAME, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)


# =====================================================================
# FEATURE FUNCTIONS
# =====================================================================
def add_student(students):
    """Add one or more students and save."""
    try:
        n = int(input("How many students do you want to enter: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(n):
        try:
            ID    = int(input(f"Enter ID of student {i + 1}: "))
            Age   = int(input("Enter age: "))
            Marks = int(input("Enter marks: "))
        except ValueError:
            print("ID, Age and Marks must be numbers. Skipping this one.")
            continue

        if any(s.ID == ID for s in students):
            print(f"ID {ID} already exists. Skipping.")
            continue

        Name   = input("Enter name: ")
        Course = input("Enter course: ")

        try:
            students.append(Student(ID, Name, Age, Course, Marks))
        except ValueError as e:
            print(f"Invalid student data: {e}")
            continue

    save_data(students)
    print("Student(s) saved successfully!")


def view_students(students):
    """Display every student."""
    if not students:
        print("No student records available!")
        return
    for i, s in enumerate(students, 1):
        print(f"--- Student {i} ---")
        s.display()
        print()


def search_student(students):
    """Find a student by ID."""
    if not students:
        print("No student records available!")
        return

    try:
        ID = int(input("Enter the ID of the student: "))
    except ValueError:
        print("ID must be a number.")
        return

    for s in students:
        if s.ID == ID:
            print("Student found:")
            s.display()
            return
    print("Student not found.")


def update_student(students):
    """Update Age, Course or Marks (ID and Name are locked)."""
    if not students:
        print("No student records available!")
        return

    try:
        ID = int(input("Enter the ID of the student to update: "))
    except ValueError:
        print("ID must be a number.")
        return

    # find the target student
    target = next((s for s in students if s.ID == ID), None)
    if target is None:
        print("Student not found.")
        return

    print("1. Age\n2. Course\n3. Marks")
    try:
        choice = int(input("Enter (1,2,3): "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        try:
            target.Age = int(input("Enter new age: "))
        except ValueError:
            print("Age must be a number.")
            return
    elif choice == 2:
        target.Course = input("Enter new course: ")
    elif choice == 3:
        try:
            new_marks = int(input("Enter new marks: "))
            target.update_marks(new_marks)
        except ValueError as e:
            print(f"Cannot update: {e}")
            return
    else:
        print("Invalid choice.")
        return

    save_data(students)
    print("Updated successfully!")


def delete_student(students):
    """Remove a student by ID."""
    if not students:
        print("No student records available!")
        return

    try:
        ID = int(input("Enter the ID to delete: "))
    except ValueError:
        print("ID must be a number.")
        return

    for s in students:
        if s.ID == ID:
            students.remove(s)
            save_data(students)
            print("Deleted successfully!")
            return

    print("Student not found.")


# =====================================================================
# MAIN MENU
# =====================================================================
def display_menu():
    print("\n1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")


def main():
    print("--------------- STUDENT MANAGEMENT SYSTEM ----------------------")
    students = load_data()      # ← load once at startup

    while True:
        display_menu()
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