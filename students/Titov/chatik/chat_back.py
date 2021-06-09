from flask import Flask, session, request

app = Flask(__name__)
app.secret_key = b'\xcf\xb1\xbf\x92\x81\xbc\xbe\x9aB\xe0X\xdb$\xb0\x01\xffz0\x96\xdb\xb7\x05'

mess_list = {"rows": []}
message_template = {'u_name': '', 'time': '', 'message_text': ''}



@app.route('/')
def index():
    return 'wazzzaaaaaaap'


@app.route('/login', methods=['POST'])
def login():
    j = request.json
    if request.method == 'POST':
        session['u_name'] = j['u_name']
    return 'Connected'


@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'GET':
        return message_template
    elif request.method == 'POST':
        mess_list['rows'].append(request.json)
        return 'sended'


@app.route('/get_messages')
def get_messages():
    return mess_list


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('u_name')
    return 'You\'ve logout'


if __name__ == '__main__':
    app.run('127.0.0.1', 50550)
