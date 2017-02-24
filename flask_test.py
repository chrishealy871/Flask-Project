from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Brendan", "Age": 30},
    {"name": "Chris", "Age": 30},
    {"name": "Mark", "Age": 30},
    {"name": "Kathrin", "Age": 30},
    {"name": "Colleen", "Age": 30},
    {"name": "Tati", "Age": 30},
    {"name": "Nikita", "Age": 30}
]
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/students")
def show_Students():
    return render_template("students.html")

if __name__ == '__main__':
    app.run()
