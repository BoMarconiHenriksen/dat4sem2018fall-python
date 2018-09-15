from flask import Flask


my_app = Flask(__name__)


@my_app.route('/')
def hello():
    return 'Hej from Bo - 10.50.130.46'


@my_app.route('/<book_id>/<pages>')
def read_books(pages):
    print(pages)
    return pages


if __name__ == '__main__':
    my_app.run(host='0.0.0.0')
