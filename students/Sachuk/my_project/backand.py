from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.username} {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def connect_to_server():
    return render_template('base.html', title='Главная страница')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html', title='Страница регистрации')
    elif request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['password'])
            print('Начало добавления нового пользователя')
            user = Users(username=request.form['username'], email=request.form['email'], password=hash)
            print(request.form['username'])
            print(request.form['email'])
            print(request.form['password'])
            db.session.add(user)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            print('Ошибка добавления в БД')

    return render_template('add_info.html')


@app.route('/optional_info', methods=['GET', 'POST'])
def add_info():
    if request.method == 'GET':
        return render_template('add_info.html', title='Добавьте информацию о себе')
    elif request.method == 'POST':
        try:
            p = Profiles(first_name=request.form['first_name'], last_name=request.form['last_name'],
                         old=request.form['old'], city=request.form['city'])
            db.session.add(p)
            db.session.flush()
            db.session.commit()
        except:
            db.session.rollback()
            print('Ошибка добавления в БД')
        return render_template('successful.html')


if __name__ == "__main__":
    app.run('127.0.0.1', 50550)
