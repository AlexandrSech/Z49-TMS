from flask import Flask, session, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route('/index')
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/first_template', methods=['GET', 'POST'])
def first_template():
    if request.form:
        return render_template('ft.html',
                               fn=request.form['first_name'],
                               ln=request.form['second_name'],
                               aa=request.form['age'])
    return render_template('ft.html')


@app.route('/new_data/<str:user_name>')
def new_data(user_name):
    print(user_name)
    return ''


if __name__ == "__main__":
    app.run('127.0.0.1', 50550)
