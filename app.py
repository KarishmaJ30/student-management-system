from flask import Flask, render_template, request
from database import (
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student,
    get_dashboard_stats
)

app = Flask(__name__)


@app.route("/")
def home():

    total_students, total_courses, total_years = get_dashboard_stats()

    return render_template(
        "index.html",
        total_students=total_students,
        total_courses=total_courses,
        total_years=total_years
    )


@app.route("/add-student", methods=["GET", "POST"])
def add_student_page():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]
        year = request.form["year"]
        address = request.form["address"]

        add_student(
            name,
            email,
            phone,
            course,
            year,
            address
        )

        return "Student added successfully!"

    return render_template("add_student.html")

@app.route("/students")
def students():

    student_list = get_students()

    return render_template(
        "students.html",
        students=student_list
    )


@app.route("/edit-student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    student = get_student(student_id)

    if student is None:
        return "Student not found"

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]
        year = request.form["year"]
        address = request.form["address"]

        update_student(
            student_id,
            name,
            email,
            phone,
            course,
            year,
            address
        )

        return "Student updated successfully!"

    return render_template(
        "edit_student.html",
        student=student
    )


@app.route("/delete-student/<int:student_id>")
def delete_student_page(student_id):

    delete_student(student_id)

    return "Student deleted successfully!"



if __name__ == "__main__":
    app.run(debug=True)