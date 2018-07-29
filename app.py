from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Google Cloud Build app!!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
