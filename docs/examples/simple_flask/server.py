from flask import Flask, session, render_template, request
app = Flask(__name__, template_folder='templates')

# {'login': '', 'id': ''}


@app.route('/login', methods=['POST'])
def login():
    j = request.json
    '''for k in j.keys():
        session[k] = j[k]'''
    session['bip'] = 0
    return 'login ok'


@app.route('/bip')
def bip():
    session['bip'] += 1
    return 'you made bip'


@app.route('/logout')
def logout():
    del session
    return 'buy buy'


if __name__ == "__main__":
    app.run('127.0.0.1', 50550)
