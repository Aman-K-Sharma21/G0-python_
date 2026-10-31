import mysql.connector

DB_CONFIG = {
    "host" : "localhost",
    "user" : "root",
    "password" : "aman2029",
    "database" : "student_course_db"
}


def init_db():
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id   int           primary key,
                name         varchar(100)  not null,
                age          int           not null check(age > 0)
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS courses (
                course_id     int            primary key,
                course_name   varchar(100)   not null unique
                )""")
            cur.execute("""CREATE TABLE IF NOT EXISTS enrollments (
                student_id        int      not null,
                course_id         int      not null,
                marks             float    not null check(marks between 0 and 100),
                primary key(student_id,course_id),
                foreign key (student_id) references students(student_id),
                foreign key (course_id) references courses(course_id)
                )""")
        connection.commit()

def add_student(student_id,name,age):
    if not isinstance(age,int) or age <=0:
        raise ValueError (f"Invalid age : {age} must be positive integer")
    if not name or not name.strip():
        raise ValueError("Name cannot be empty")

    try:
        with mysql.connector.connect(**DB_CONFIG) as connection:
            with connection.cursor() as cur:
                cur.execute("""insert into students(student_id , name , age) values (%s,%s,%s)""",(student_id,name,age)
                )
            connection.commit()
    except mysql.connector.IntegrityError as e:
        raise ValueError (f"Student ID {student_id} already exists") from e
    print(f"Added student {name} (ID {student_id})")

def add_course(course_id,course_name):
    if not course_name:
        raise ValueError ("Course cannot be empty.")

    try:
        with mysql.connector.connect(**DB_CONFIG) as connection:
            with connection.cursor() as cur:
                cur.execute("""insert into courses(course_id,course_name) values (%s,%s)""",(course_id,course_name))
            connection.commit()
    except mysql.connector.IntegrityError as e:
        raise ValueError (f"Course ID {course_id} or name {course_name} already exists") from e
    print(f"Added course {course_name} (ID {course_id})")

def enroll_student(student_id,course_id,marks):
    if not isinstance(marks,(int,float)) or not (0<= marks <=100):
        raise ValueError (f"Invalid marks {marks} (must be positive number)")
    try:
        with mysql.connector.connect(**DB_CONFIG) as connection:
            with connection.cursor() as cur:
                cur.execute("""insert into enrollments (student_id,course_id,marks) values (%s,%s,%s)""",(student_id,course_id,marks))
            connection.commit()
    except mysql.connector.IntegrityError as e:
        msg = str(e)

        if "1452" in msg or "foreign key" in msg.lower():
            raise ValueError(f"Invalid student {student_id}or course {course_id} - one of them doesn't exists") from e
        if "1062" in msg or "duplicate" in msg.lower():
            raise ValueError(
                f"Student {student_id} is already enrolled in course {course_id}"
            ) from e
        

    print(f"Enrolled student {student_id} in course {course_id} (marks={marks})")

def view_enrollment():
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute("""select s.name, c.course_name,e.marks
                            from enrollments e
                            join students s on s.student_id = e.student_id
                            join courses c on c.course_id = e.course_id
                            order by s.name,c.course_name
                            """)
            rows = cur.fetchall()

    if not rows:
        print("No enrollments found")
        return

    print(f"{'Student':<12}{'Course':<14}{'Marks':>6}")
    print("-" * 32)
    for name, course, marks in rows:
        print(f"{name:<12}{course:<14}{marks:>6}")

def view_student_transcript(student_id):
    with mysql.connector.connect(**DB_CONFIG) as connection:
        with connection.cursor() as cur:
            cur.execute("""select name from students where student_id = %s""",(student_id,))
            student = cur.fetchone()

            if student is None:
                print(f"No student found with ID {student_id}")
                return

            cur.execute("""select c.course_name, e.marks from enrollments e join courses c on c.course_id = e.course_id where e.student_id = %s order by c.course_name """,(student_id,))

            rows = cur.fetchall()

    name = student[0]
    print(f"Transcript for {name} (ID {student_id})")
    print("-" * 32)

    if not rows:
        print("No enrollments yet")
        return

    print(f"{'Course':<14}{'Marks':>6}")
    print("-" * 20)
    for course,marks in rows:
        print(f"{course:<14}{marks:>6}")

def show_course_statistics():
    """Print per-course enrolment count and average marks."""
    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.course_name,
                COUNT(e.student_id) AS num_students,
                AVG(e.marks)        AS avg_marks
                FROM enrollments e
                JOIN courses c ON c.course_id = e.course_id
                GROUP BY c.course_id, c.course_name
                ORDER BY c.course_name
            """)
            rows = cur.fetchall()

    if not rows:
        print("No course statistics yet — enroll some students first")
        return

    print(f"{'Course':<14}{'Students':>10}{'Avg Marks':>12}")
    print("-" * 36)
    for course, count, avg in rows:
        avg_display = f"{float(avg):.2f}" if avg is not None else "—"
        print(f"{course:<14}{count:>10}{avg_display:>12}")