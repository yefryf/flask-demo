import sys

from flask import Flask


app = Flask(__name__)

HELLO_WORLD = 'Hello World'


@app.route('/', methods=['GET'])
def hello_world():
    return HELLO_WORLD


if __name__ == '__main__':
    if len(sys.argv) > 1:
        HELLO_WORLD = ' '.join(sys.argv[1:])

    app.run(host='0.0.0.0', port=80)
