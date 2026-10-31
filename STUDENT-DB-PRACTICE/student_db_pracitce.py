import mysql.connector


DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "aman2029",
    "database" : "student_db"
}

with mysql.connector.connect(**DB_CONFIG) as connection:
    with connection.cursor() as cur:
        cur.execute("""
            create table if not exists students (
                student_id integer primary key,
                name varchar(20) not null, 
                age int not null, 
                course varchar(50) not null, 
                marks float not null check(marks >=0 and marks <=100)
            )
        """)

    connection.commit()


def Add_student(Id,Name,Age,Course,Marks):

    if not(0<=Marks <=100):
        raise ValueError(f"Invalid marks : {Marks} (must be 0-100)")
    if not(0<=Age<=150):
        raise ValueError(f"Invalid age : {Age}")
    try:
        with mysql.connector.connect(**DB_CONFIG) as connection:
            with connection.cursor() as cur:
                cur.execute("insert into students (student_id,name,age,course,marks) values (%s,%s,%s,%s,%s)",(Id,Name,Age,Course,Marks))
            connection.commit()
    except mysql.connector.IntegrityError as e:
        raise ValueError(f"Student ID {Add_student} already exists") from e
    print(f"Added student {Name} (ID {Id})")
    

def View_all_student():
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute("select student_id,name,age,course,marks from students")
            item = cur.fetchall()

    if not item:
        print("No students found")
        return
    
    #Header
    print(f"{"ID":<5}{"Name":<12}{"Age":<6}{"Course":<12}{"Marks":>6}")
    print("-" * 41)

    #Rows
    for sid,name,age,course,marks in item:
        print(f"{sid:<5}{name:<12}{age:<6}{course:<12}{marks:>6}")

    

def search_by_id(Id):
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute("select * from students where student_id = %s", (Id,))
            item = cur.fetchone()

    if item is None:
        print(f"No student found with ID {Id}")
        return
    print(f"{"ID":<5}{"Name":<12}{"Age":<6}{"Course":<12}{"Marks":>6}")
    print("-" * 41)

    sid,name,age,course,marks = item
    print(f"{sid:<5}{name:<12}{age:<6}{course:<12}{marks:>6}")


def update_student(student_id, new_marks):
    if not(0 <=new_marks<=100):
        raise ValueError(f"Invalid marks: {new_marks!r} (must be a number 0–100)")

    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute(
                "update students set marks = (%s) Where student_id = (%s)",
            (new_marks, student_id)
        )
            if cur.rowcount == 0:
                print(f"No student found with ID {student_id}")
                return
        connection.commit()

    print(f"Updated student {student_id} → marks = {new_marks}")
    View_all_student()

def Delete_student(Id):
    View_all_student()
    try:
        with mysql.connector.connect(**DB_CONFIG) as connection :
            with connection.cursor() as cur :
                cur.execute("delete from students where student_id = %s",(Id,)
                )
                if cur.rowcount == 0:
                    print(f"No student found with ID {Id}")
                    return
            connection.commit()
    except mysql.connector.Error as e:
        print(f"Database error : {e}")
        return
    print(f"Delete student with ID {Id}")
    View_all_student()

def main():
    while(1):
        print("----------WELCOME TO student database with sqlite----------")
        print("-" * 41)
        print("STUDENT DATABASE")
        print("")
        print("")
        print("1.Add student\n2.View all students\n3.Search Student\n4.Update student\n5.Delete student\n6.Exit")
        try:
            choice = int(input("Enter (1-6) from above queries : "))
        except ValueError:
            print("Enter a literal choice from above list.")
            continue

        if choice == 1:
            try:
                id = int(input("Enter ID of student : "))
                age = int(input("Enter the age of student : "))
                Marks = int(input("Enter the marks of student : "))
            except ValueError:
                print("Id,age and marks must be numbers...")
                continue
            
            name = input("Enter the name of student :")
            
            course = input("Enter the course of student : ")
            try:
                Add_student(id,name,age,course,Marks)
            except ValueError as e:
                print(f"Error : {e}")
        elif choice == 2:
            View_all_student()
        elif choice == 3:
            try:
                id = int(input("Enter ID of student : "))
            except ValueError:
                print("Id must be integer and positive....")
                continue
            search_by_id(id)
        elif choice == 4:
            try:
                id = int(input("Enter ID of student : "))
                new_marks = int(input("Enter the updated marks : "))
            except ValueError: 
                print("Id and new_marks must be number..")
                continue
            try:
                update_student(id,new_marks)
            except ValueError as e:
                print(f"Error : {e}")
        elif choice == 5:
            try:
                id = int(input("Enter ID of student : "))
            except ValueError :
                print("Id must be integer...")
                continue
            Delete_student(id)
        elif choice == 6:
            print("Thank you for using it...")
            break
        else:
            print("Please, Enter a valid input....")
            continue


main()