from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(300), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/one', methods=['GET','POST'])
def one():
    return render_template('one.html')

@app.route('/two', methods=['GET','POST'])
def two():
    return render_template('two.html')

@app.route('/three', methods=['GET','POST'])
def three():
    return render_template('three.html')

@app.route('/four', methods=['GET','POST'])
def four():
    return render_template('four.html')

@app.route('/five', methods=['GET','POST'])
def five():
    return render_template('five.html')

@app.route('/six', methods=['GET','POST'])
def six():
    return render_template('six.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'b',
            'q2': 'c',
            "q3": "b",
            'q4': 'a',
            'q5': 'c',
            'q6': 'c'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5'),
            'q6': request.form.get('q6')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("one.html", result=result)

@app.route('/quiz_two', methods=['GET', 'POST'])
def quiz_two():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'c',
            'q2': 'c',
            "q3": "a",
            'q4': 'a',
            'q5': 'c',
            'q6': 'b',
            'q7': 'c'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5'),
            'q6': request.form.get('q6'),
            'q7': request.form.get('q7')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("two.html", result=result)

@app.route('/quiz_three', methods=['GET', 'POST'])
def quiz_three():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'b',
            'q2': 'a',
            "q3": "b",
            'q4': 'c',
            'q5': 'c',
            'q6': 'a',
            'q7': 'c'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5'),
            'q6': request.form.get('q6'),
            'q7': request.form.get('q7')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("three.html", result=result)

@app.route('/quiz_four', methods=['GET', 'POST'])
def quiz_four():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'b',
            'q2': 'a',
            "q3": "b",
            'q4': 'a',
            'q5': 'b'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("four.html", result=result)

@app.route('/quiz_five', methods=['GET', 'POST'])
def quiz_five():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'c',
            'q2': 'b',
            "q3": "a",
            'q4': 'c',
            'q5': 'c'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("five.html", result=result)

@app.route('/quiz_six', methods=['GET', 'POST'])
def quiz_six():
    result = None
    if request.method == 'POST':
        correct_answers = {
            'q1': 'b',
            'q2': 'a',
            "q3": "b",
            'q4': 'c',
            'q5': 'a',
            'q6': 'b'
        }

        user_answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5'),
            'q6': request.form.get('q6')
        }

        score = sum(1 for q, a in correct_answers.items() if user_answers.get(q) == a)
        total = len(correct_answers)

        if score == total:
            result = "Отлично! Все ответы верны 🎉"
        elif score >= total / 2:
            result = f"Неплохо! Ты ответил(а) правильно на {score} из {total}."
        else:
            result = f"Ты ответил(а) правильно на {score} из {total}. Но ты на верном пути, не сдавайся 💪"

    return render_template("six.html", result=result)



@app.route('/feedback', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email= request.form['email']
        text = request.form['text']
        
        user = User(email=email, text=text)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

app.run(debug=True)