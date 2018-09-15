import flask
import requests
import os
from datetime import datetime


my_app = flask.Flask(__name__)
user_file = './logs/clients.txt'
before = None


def create_directory(directory_name):
    try:
        cwd = os.getcwd()
        path_for_file = os.path.join(cwd, directory_name)

        if not os.path.exists(path_for_file):
            os.makedirs(path_for_file)
    except OSError:
        pass


def write_page_to_file():
    response = requests.get('https://news.ycombinator.com/')

    create_directory("templates")

    content_file = './templates/hackernews.html'
    with open(content_file, 'w', encoding='utf-8') as file:
        file.write(response.text)


def write_user_to_log(ip):
    # http://docs.python-requests.org/en/latest/api/?highlight=elapsed#requests.Response.elapsed
    #request_time = requests.get(ip).elapsed._to_microseconds()

    create_directory("logs")

    if (os.path.isfile(user_file)):
        attr = 'a'
    else:
        attr = 'w'

    with open(user_file, attr, encoding='utf-8') as file:
        file.write(f'{ip}')
        #file.write(f' - request served in {request_time} miliseconds\n')


@my_app.before_request
def start_timer():
    global before
    before = datetime.now()


@my_app.route('/')
def render_page():
    write_user_to_log(flask.request.remote_addr)
    return flask.render_template('hackernews.html')


# Skal laves med callback https://stackoverflow.com/questions/11939858/flask-nonetype-object-is-not-callable
@my_app.after_request
def per_request_timer(response):
    global before
    after = datetime.now()

    serve_time = after - before
    with open(user_file, 'a', encoding='utf-8') as file:
        file.write(f' - request served in {serve_time} miliseconds\n')


if __name__ == '__main__':
    write_page_to_file()
    my_app.run(host='0.0.0.0')
