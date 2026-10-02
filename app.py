from flask import Flask, render_template, request
from database import add_student, get_students

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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


if __name__ == "__main__":
    app.run(debug=True)