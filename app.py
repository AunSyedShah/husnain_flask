from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy()
db.init_app(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        stud_name = request.form.get('name')
        stud_age = request.form.get('age')
        student = Student(name=stud_name, age=stud_age)
        db.session.add(student)
        db.session.commit()
        return "<h1>Student added successfully</h1>"
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
