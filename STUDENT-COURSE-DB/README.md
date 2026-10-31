# 🎓 Student Course Registration System

A command-line application that manages students, courses, and enrollments
in a **relational MySQL database**. Built in Python as a learning project
to demonstrate multi-table schemas, foreign keys, JOINs, and GROUP BY.

---

## 📌 What This Application Does

This app lets you register students in courses and track their marks —
all persisted in a real relational database. It demonstrates the step up
from single-table CRUD to **relational CRUD**, where data is split across
three linked tables instead of stored in one big spreadsheet.

The core idea: **don't duplicate data.** A student's name lives in one
row in the `students` table. A course's name lives in one row in the
`courses` table. The `enrollments` table just **points** at both by ID.
Rename a student, and every enrollment that references them is
automatically correct — no mass updates needed.

---

## ✨ Features

- **Add students** — register a new student with ID, name, and age.
  Validates that age is a positive integer.

- **Add courses** — register a new course with ID and a unique name.
  The database rejects duplicate course names.

- **Enroll a student** — link a student to a course with a mark (0–100).
  Enforces:
  - The student must exist
  - The course must exist
  - The same student cannot be enrolled in the same course twice
  - Marks must be between 0 and 100

- **View all enrollments** — a full table showing every enrollment with
  the student's name, the course name, and the mark. Built with a
  **three-way JOIN** across `students`, `courses`, and `enrollments`.

- **View a student's transcript** — all courses and marks for a single
  student, with their name shown at the top. Built with a **JOIN** on
  `enrollments` and `courses`, filtered by `student_id`.

- **Show course statistics** — per-course number of enrolled students
  and average mark. Built with **GROUP BY** and aggregate functions
  (`COUNT`, `AVG`).

- **Automatic sample data** — on first run, the app seeds itself with
  fictional students, courses, and enrollments so you can try every
  feature immediately. Uses `INSERT IGNORE` so re-runs don't crash or
  duplicate data.

- **Persistent storage** — all data lives in MySQL and survives program
  restarts. Close the app, reopen it, and everything is still there.

---

## 📋 Prerequisites

Before you can run this program, you need:

### 1. Python 3.8 or newer

Check with:

```bash
python --version