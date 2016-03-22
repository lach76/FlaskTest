import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('base.html')
    
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5020)
