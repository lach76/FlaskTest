import flask
import json
from flask_socketio import SocketIO

app = flask.Flask(__name__)
socket = SocketIO(app, async_mode='threading')

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('base.html')

@socket.on('users')
def users():
    socket.emit('users', json.dumps([{
        'id': 1,
        'name': 'gildong',
    }, {
        'id': 2,
        'name': 'chulsoo'
    }]))

if __name__ == "__main__":
    # app.run(debug = True, host = "0.0.0.0", port = 5020)
    socket.run(app, host = "0.0.0.0", port = 5020)
