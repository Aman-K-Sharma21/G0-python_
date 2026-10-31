
from database import (
    init_db,add_student, add_course, enroll_student,
    view_enrollment, view_student_transcript, show_course_statistics,
)


def main():
    # Ensure tables exist and sample data is present
    try:
        init_db()
    except Exception as e:
        print(f"Could not initialise database: {e}")
        print("Check: is MySQL running? Did you run CREATE DATABASE student_course_db;?")
        return

    while True:
        print("\nSTUDENT COURSE REGISTRATION")
        print("-" * 32)
        print("1. Add student")
        print("2. Add course")
        print("3. Enroll student")
        print("4. View all enrolments")
        print("5. View student's transcript")
        print("6. Show course statistics")
        print("7. Exit")

        try:
            choice = int(input("Enter (1-7): "))
        except ValueError:
            print("Enter a number from 1 to 7.")
            continue

        # --- 1. Add student ---
        if choice == 1:
            try:
                student_id = int(input("Student ID: "))
                name       = input("Name: ")
                age        = int(input("Age: "))
            except ValueError:
                print("ID and age must be integers.")
                continue
            try:
                add_student(student_id, name, age)
            except ValueError as e:
                print(f"Error: {e}")

        # --- 2. Add course ---
        elif choice == 2:
            try:
                course_id = int(input("Course ID: "))
            except ValueError:
                print("Course ID must be an integer.")
                continue
            course_name = input("Course name: ")
            try:
                add_course(course_id, course_name)
            except ValueError as e:
                print(f"Error: {e}")

        # --- 3. Enroll student ---
        elif choice == 3:
            try:
                student_id = int(input("Student ID: "))
                course_id  = int(input("Course ID: "))
                marks      = float(input("Marks (0-100): "))
            except ValueError:
                print("ID, course ID and marks must be numbers.")
                continue
            try:
                enroll_student(student_id, course_id, marks)
            except ValueError as e:
                print(f"Error: {e}")

        # --- 4. View all enrollments ---
        elif choice == 4:
            view_enrollment()

        # --- 5. Student's transcript ---
        elif choice == 5:
            try:
                student_id = int(input("Student ID: "))
            except ValueError:
                print("ID must be an integer.")
                continue
            view_student_transcript(student_id)

        # --- 6. Course statistics ---
        elif choice == 6:
            show_course_statistics()

        # --- 7. Exit ---
        elif choice == 7:
            print("Goodbye!")
            break

        else:
            print("Please enter a valid choice (1-7).")


if __name__ == "__main__":
    main()