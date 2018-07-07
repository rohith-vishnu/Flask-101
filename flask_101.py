from flask import Flask


fb = Flask(__name__)


@fb.route('/home')
def hello_world():
    return 'Hello flask'


if __name__ == "__main__":
    fb.run()


