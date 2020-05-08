from flask import Flask

app = Flask(__name__)


@app.route('/',methods=["post", "get"])
def hello_world():
    return 'Hello World!'


@app.route('/orders/<int:id>')
def get_orders(id):
    return 'orders%s' % id


if __name__ == '__main__':
    app.run()
