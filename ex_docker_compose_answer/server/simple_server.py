from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def do_GET():
    return 'Hi! This is the response of the GET request'

@app.route('/', methods=["POST"])
def do_POST():
    return 'Hi! This is the response of the POST request'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8000)