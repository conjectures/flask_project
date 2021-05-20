from flask import Flask
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


app.run(debug=DEBUG, port=PORT, host=HOST)
