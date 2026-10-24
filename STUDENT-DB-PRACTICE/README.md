📘 Student Database Management System — README

Here's your complete README, built on the intro you already wrote. I've kept your voice and filled in every remaining section in plain, beginner-friendly language.

### 1. What the application does?

A nice interactive CLI input asking you to enter the required information. The main objective of this application is to store data in a database for as long as we need — I use SQLite, a Python in-built database module.

In simple words: you open the program, you get a menu, and you can add students, view all of them, search by ID, update marks, and delete records. All the data lives in a file called students.db on your computer. When you close the program and reopen it, the data is still there — that's what "persistent" means. It does not disappear on every run like a normal Python variable would.

### 2. Features
Here's what the app can do:

Add a student — enter ID, name, age, course, and marks. The app checks that marks are between 0 and 100 and age is between 0 and 150 before saving. If the ID already exists, it tells you politely instead of crashing.

View all students — shows the entire table in a neat, aligned format with a header row. If the database is empty, it says "No students found" instead of printing a blank screen.

Search by ID — type an ID, and the app shows only that student's record. If no student has that ID, it tells you clearly.

Update marks — change the marks of an existing student by ID. The same 0–100 validation applies. If the ID doesn't exist, the app says so.

Delete a student — removes a student by ID. Before deleting, it shows the full table so you can double-check. After deleting, it shows the table again so you can confirm the row is gone.

Interactive menu — a simple numbered menu (1–6) lets you pick what to do. If you type something invalid (like "abc" instead of a number), the app doesn't crash — it shows a friendly message and brings the menu back.

Data safety — all database changes are committed automatically when they succeed. If something goes wrong (like a duplicate ID), the change is rolled back automatically, so your database never ends up in a half-written state.

### 3. Prerequisites and run instructions
Prerequisites
You only need Python 3.8 or newer. That's it. No extra installations.

Why? Because sqlite3 is part of Python's standard library — it comes bundled with Python itself. There is nothing to pip install. You can check your Python version with:

bash
python --version
If it says Python 3.8 or higher, you're ready.

Run instructions
Save the code to a file called student_db.py (or any name you like, as long as it ends in .py).

Open a terminal and navigate to the folder where you saved the file.

Run it:

bash
python student_db.py
Follow the menu. On the very first run, the app automatically creates students.db and the students table for you. On later runs, it opens the existing database — so any students you added before are still there.

To exit, choose option 6 from the menu.

If you ever want to start with a completely fresh database, just delete the students.db file and run the program again. A new one will be created with an empty table.

### 4. Database schema
The app uses one table called students. Here's what it looks like:

Column 	           Type	        Constraint	                              Meaning
student_id	    INTEGER	       PRIMARY KEY	                      Unique ID for each student. Used to identify records.
name	          TEXT	        NOT NULL	                      Student's name. Cannot be empty/null.
age	             INTEGER	    NOT NULL	                      Student's age. Cannot be null.
course	           TEXT	        NOT NULL	                      Course the student is enrolled in. Cannot be null.
marks	           REAL	        NOT NULL, 	                      Student's marks. Must be a number between 0 and 100.
                            CHECK(marks >= 0 AND marks <= 100)

### What those constraints mean in plain English?

PRIMARY KEY— every student must have a unique student_id. The database will refuse to store two students with the same ID. This is how the app prevents duplicates.

NOT NULL — you can't leave that column blank. If a student has no name, no age, no course, or no marks, the record is rejected.

CHECK — a rule the database enforces itself. Even if the Python code has a bug, the database will still reject any marks outside 0–100. This is called a safety net at the database level.

The CREATE TABLE statement
sql
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name       TEXT    NOT NULL,
    age        INTEGER NOT NULL,
    course     TEXT    NOT NULL,
    marks      REAL    NOT NULL CHECK(marks >= 0 AND marks <= 100)
);
The IF NOT EXISTS part means: "if a table called students is already there, don't try to create it again — just leave it alone." This is why you can run the program many times without losing data.

### 5. Example operations
Here's what a real session looks like:

Adding a student
text
Enter (1-6): 1
Enter ID of student: 1
Enter age of student: 20
Enter marks of student: 92.5
Enter name of student: Alice
Enter course of student: Mathematics

Added student Alice (ID 1)
Viewing all students
text
Enter (1-6): 2

ID   Name        Age   Course       Marks
-----------------------------------------
1    Alice       20    Mathematics  92.5
2    Bob         22    Physics      88.0
Searching for a student
text
Enter (1-6): 3
Enter ID of student: 2

ID   Name        Age   Course       Marks
-----------------------------------------
2    Bob         22    Physics      88.0

### If you search for an ID that doesn't exist:

Enter ID of student: 99 ------>  No student found with ID 99


### Updating marks

Enter (1-6): 4
Enter ID of student: 1
Enter updated marks: 95

Updated student 1 → marks = 95.0


Deleting a student

Enter (1-6): 5
Enter ID of student: 2

ID   Name        Age   Course       Marks
-----------------------------------------
1    Alice       20    Mathematics  95.0
2    Bob         22    Physics      88.0

Deleted student with ID 2

ID   Name        Age   Course       Marks
-----------------------------------------
1    Alice       20    Mathematics  95.0


Notice how the table is shown before and after the delete, so you can visually confirm the row actually disappeared.

6. Tests performed and their outcomes
Here's a checklist of scenarios I tested manually, and what happens in each case:

#	Test	Expected behavior	Result
1	Add a new student with valid data	Student saved, success message printed	✅ Pass
2	Add a student with the same ID as an existing one	Friendly error: Student ID X already exists — no crash	✅ Pass
3	Add a student with marks = 150	Friendly error: Invalid marks: 150 — nothing saved	✅ Pass
4	Add a student with marks = -5	Friendly error: Invalid marks: -5 — nothing saved	✅ Pass
5	Add a student with age = 200	Friendly error: Invalid age: 200	✅ Pass
6	View all students when table is empty	No students found message	✅ Pass
7	View all students after adding several	All rows printed as an aligned table	✅ Pass
8	Search for a valid ID	That student's row shown	✅ Pass
9	Search for a non-existent ID	No student found with ID X	✅ Pass
10	Update marks with a valid ID and valid marks	Marks changed, success message	✅ Pass
11	Update marks with a non-existent ID	No student found with ID X — no update happens	✅ Pass
12	Update marks with an invalid value (e.g. 200)	Invalid marks error — nothing changed	✅ Pass
13	Delete a valid ID	Row removed, table shown before and after	✅ Pass
14	Delete a non-existent ID	No student found — no deletion	✅ Pass
15	Type "abc" at the main menu	Enter a number from 1 to 6 — menu reappears, no crash	✅ Pass
16	Type "abc" at an ID prompt	ID must be an integer — menu reappears, no crash	✅ Pass
17	Close the app and reopen it	All previously added students are still there	✅ Pass
18	Run the app twice in the same folder	Table not recreated, no data lost	✅ Pass


Every one of these passes without a traceback. If you run the program and hit a case that behaves differently, that's the bug to hunt.

7. A short explanation of JSON versus SQLite
Both JSON and SQLite can store data permanently. So why did this project choose SQLite? Let me explain the difference in plain terms.

JSON — a plain text file
JSON is a text format. Think of it as a well-organized text file that looks like a Python dictionary:

json
[
    {"student_id": 1, "name": "Alice", "age": 20, "marks": 92.5},
    {"student_id": 2, "name": "Bob",   "age": 22, "marks": 88.0}
]
Advantages of JSON:

Human-readable — you can open it in any text editor and understand it.

Dead simple — Python's json module can read and write it in two lines.

Great for small amounts of data and config files.

Problems with JSON for this project:

No built-in rules. JSON doesn't know that student_id must be unique. You have to check duplicates in Python yourself by loading the entire file and looping through every record.

No built-in search. To find student 2, you load the whole file and loop through it. With 100,000 students, that's slow.

No partial updates. To change one student's marks, you rewrite the entire file. If the app crashes halfway through writing, the file can become corrupted — and you lose every record.

No concurrency safety. If two copies of the program write to the file at the same time, they can clobber each other.

SQLite — a real database
SQLite is an actual relational database stored in a single file. It looks like a file (students.db) to your operating system, but inside, it's a proper database engine that understands tables, columns, indexes, and constraints.

Advantages of SQLite:

Rules are enforced by the database. You declare student_id INTEGER PRIMARY KEY, and the database guarantees no duplicates — even if your Python code has a bug.

Fast search. Looking up a student by ID uses an index — the database jumps straight to the row. With JSON, you'd scan the whole file.

Safe partial updates. Changing one row only rewrites a small part of the file, and SQLite's write process is crash-safe. You never lose the whole file.

Transactions. If something goes wrong mid-operation, SQLite automatically rolls back — the database stays consistent.

No extra install. SQLite is built into Python.

Which should you use?
Situation	Best choice
Saving a small config file, a settings dictionary, or a few records	JSON
Storing many records that need searching, filtering, updating, and safety rules	SQLite
You want a human to be able to open and edit the file in Notepad	JSON
You want guarantees about data integrity	SQLite
For a student database, SQLite is the right tool. JSON would work for a tiny class of 5 students, but the moment you want "find student 2 quickly" or "make sure no two students have the same ID," you're re-implementing what SQLite already does — badly.

8. Known limitations and possible improvements
This is a learning project, not a production app. Here are the things it doesn't do yet, and how you could add them.

Known limitations
No login or security. Anyone who opens the program can do anything. There's no password, no permissions, no user accounts.

Only one field can be updated. update_student only changes marks. You can't update a student's name, age, or course after adding them. (To fix, add more UPDATE statements or a menu inside the update option.)

IDs must be typed manually. The app doesn't auto-generate the next available ID. If you forget which IDs you've used, you'll get duplicate-ID errors. (To fix, use INTEGER PRIMARY KEY AUTOINCREMENT and don't ask the user for the ID.)

No input length checks. You can add a student named "" (empty string) or a name with 10,000 characters. The NOT NULL constraint doesn't stop empty strings. (To fix, add if not name.strip(): raise ValueError(...).)

No delete confirmation. Pressing 5 and typing an ID deletes immediately. A real app would ask "Are you sure? (y/n)" first.

Not safe for multiple users at once. SQLite handles concurrency well, but this app doesn't — two copies running at the same time could produce strange results.

No way to list or filter beyond "all." You can't sort by name, filter by course, or find students with marks above 90. The menu is fixed.

Data is stored locally. If you move students.db to another computer without the code, or delete the file, the data is gone.

Possible improvements
Auto-generate IDs. Stop asking the user for student_id. Let the database assign the next available one automatically with AUTOINCREMENT. Removes a huge class of user errors.

Update all fields, not just marks. Extend the update option to let the user choose which field to edit: name, age, course, or marks.

Search by name. Add a "search by name" option using SELECT ... WHERE name LIKE ? — for example, finding all students whose name contains "Ali".

Sort and filter. Let the user sort by name, marks, or age. Add "show top 10 students by marks."

Delete confirmation. Ask "Delete student Alice (ID 1)? [y/N]" before removing.

Export to CSV. Add an option to export the whole table to a .csv file that opens in Excel.

A simple GUI. Use tkinter (also built into Python) to replace the CLI menu with buttons and text boxes.

Password protection. Add a simple login screen before entering the menu.

Better error messages. Catch sqlite3.Error at the main() level too, so any unexpected database issue is shown nicely instead of crashing the whole app.

Unit tests. Write a test_student_db.py file that programmatically tests each function against a temporary in-memory database (':memory:'). This is how real projects verify that nothing breaks when you refactor.

