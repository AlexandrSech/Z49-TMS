from flask import Flask, session, request

app = Flask(__name__)

messeage_list = {'rows': []}
messeage = {'user_name': '', 'date': '', 'text_messeage': ''}


@app.route("/")
def hello():
    return "Welcome in my_simple_chat"


@app.route('/login', method=['POST'])
def login():
    j = request.json
    session['user_session'] = j['user_name']
    return f"{j['user_name']} connected"


@app.route('/logout', method=['POST'])
def logut():
    last_user = session.pop('user_session')
    return f'Bye-bye {last_user}'


@app.route('/get_messeage', method=['GET'])
def get_messeage():
    return messeage_list


@app.route('/send_messeage', method=['POST', 'GET'])
def send_messeage():
    if request.method == ['GET']:
        return messeage
    if request.method == ['POST']:
        messeage_list['rows'].append(request.json)
