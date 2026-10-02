import sqlite3


def create_database():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            course TEXT,
            year INTEGER,
            address TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_student(name, email, phone, course, year, address):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, email, phone, course, year, address)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, email, phone, course, year, address))

    connection.commit()
    connection.close()

def get_students():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return students



def get_student(student_id):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    return student


def update_student(student_id, name, email, phone, course, year, address):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET name = ?,
            email = ?,
            phone = ?,
            course = ?,
            year = ?,
            address = ?
        WHERE id = ?
    """, (name, email, phone, course, year, address, student_id))

    connection.commit()

    connection.close()
    

def delete_student(student_id):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    connection.close()


create_database()

def get_dashboard_stats():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    # Total students
    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    # Total courses
    cursor.execute("""
        SELECT COUNT(DISTINCT course)
        FROM students
        WHERE course IS NOT NULL
        AND course != ''
    """)
    total_courses = cursor.fetchone()[0]

    # Academic years
    cursor.execute("""
        SELECT COUNT(DISTINCT year)
        FROM students
        WHERE year IS NOT NULL
    """)
    total_years = cursor.fetchone()[0]

    connection.close()

    return total_students, total_courses, total_years