from flask import Flask, render_template, request, redirect
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
        if "search" in request.form:
            stud_name = request.form.get('name')
            # search database for student name
            students = Student.query.filter_by(name=stud_name).all()
            context = {
                'students': students
            }
            return render_template('index.html', **context)
        if "submit" in request.form:
            stud_name = request.form.get('name')
            stud_age = request.form.get('age')
            student = Student(name=stud_name, age=stud_age)
            db.session.add(student)
            db.session.commit()
            return redirect('/')
    if request.method == 'GET':
        students = Student.query.all()
        context = {
            'students': students
        }
        return render_template('index.html', **context)


# delete all students
@app.route('/delete')
def delete():
    students = Student.query.all()
    for student in students:
        db.session.delete(student)
        db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run()
