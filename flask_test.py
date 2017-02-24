from flask import Flask, render_template
import json

app = Flask(__name__)

students = [
    {"id": 1, "name": "Brendan", "age": 30},
    {"id": 2, "name": "Chris", "age": 28},
    {"id": 3, "name": "Kathrin", "age": 35},
    {"id": 4, "name": "Colleen", "age": 39},
    {"id": 5, "name": "Mark", "age": 40},
    {"id": 6, "name": "Daniel", "age": 45},
    {"id": 7, "name": "Tati", "age": 98},
]
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/students")
def show_Students():
    return render_template("students.html", students = students)

if __name__ == '__main__':
    app.run()
