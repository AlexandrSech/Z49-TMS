from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, session, url_for, flash, redirect,abort

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'eb5dacdfd4409d82fe3386352f48fa7e77feba87'

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250), nullable=True)
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


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mes_username = db.Column(db.String, db.ForeignKey('users.username'))
    text = db.Column(db.String(), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return render_template('base.html', title='Главная страница')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html', title='Страница регистрации')
    elif request.method == 'POST':
        try:
            if len(request.form['username']) > 4 and request.form['password'] == request.form['password2'] \
                    and len(request.form['password']) > 8:
                hash = generate_password_hash(request.form['password'])
                print('Начало добавления нового пользователя')
                user = Users(username=request.form['username'], email=request.form['email'], password=hash)
                print(request.form['username'])
                print(request.form['email'])
                print(request.form['password'])
                db.session.add(user)
                db.session.flush()
                db.session.commit()
                flash('Вы удачно зарегистрировались')
                return redirect(url_for('login'))
            else:
                if len(request.form['password']) > 8:
                    flash('Ошибка регистрации пользователя. Пароль слишком короткий\n', category="error")
                if len(request.form['username']) < 4:
                    flash('Ошибка регистрации пользователя. Логин слишком короткий\n', category="error")
                if request.form['password'] != request.form['password2']:
                    flash('Ошибка регистрации пользователя. Пароли не совпадают\n', category="error")
        except Exception as e:
            flash('Ошибка регистрации пользователя', category="error")
            print(e)
            db.session.rollback()
            print('Ошибка добавления в БД')

    return render_template('registration.html', title='Регистрация пользователя')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Авторизация пользователя')
    if request.method == 'POST':
        res = Users.query.filter_by(username=request.form['username']).first()
        print(check_password_hash(res.password, request.form['password']))
        print(request.form['password'])
        print(request.form['username'])
        print(res.username)
        print(res.username == request.form['username'])

        if check_password_hash(res.password, request.form['password']) == True and res.username == request.form[
            'username']:
            session['username'] = request.form['username']
            session['id'] = res.id
            return redirect(url_for('add_info'))
    return render_template('login.html', title='Авторизация пользователя')


@app.route('/add_info', methods=['GET', 'POST'])
def add_info():
    if request.method == 'GET':
        res = Profiles.query.filter_by(user_id=session['id']).first()
        if res != None:
            return redirect(url_for('chat'))
        else:
            return render_template('add_info.html', title='Добавьте информацию о себе')
    elif request.method == 'POST':
        print(request.form['first_name'])
        print(request.form['last_name'])
        print(request.form['old'])
        print(request.form['city'])
        print(session['id'])
        try:
            p = Profiles(first_name=request.form['first_name'], last_name=request.form['last_name'],
                         old=request.form['old'], city=request.form['city'], user_id=session['id'])
            print(request.form['first_name'])
            print(request.form['last_name'])
            print(request.form['old'])
            print(request.form['city'])
            print(session['id'])
            db.session.add(p)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print('Ошибка добавления в БД')
        return render_template('successful.html')


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'GET':
        messages = Messages.query.all()
        return render_template('chat.html', title='Страница чата', messages=messages)
    if request.method == 'POST':
        try:
            m = Messages(mes_username=session['username'], text=request.form['text'])
            db.session.add(m)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print('Ошибка добавления в БД')
    return render_template('chat.html', title='Страница чата')


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username')


if __name__ == "__main__":
    app.run('127.0.0.1', 50550)
