from flask import Flask, request


app = Flask(__name__)

@app.route('/')


def hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name'] + '!'
    else:
        return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
