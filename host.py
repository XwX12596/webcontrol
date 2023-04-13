from lib.bottle import run, get, post, static_file, template
from picam import fetch
from bell import warning

@get('/')
def index():
    return template('index')

@get('/<filename:re:.*\.jpg>')
def get_image(filename):
    return static_file(filename, root='./image', mimetype='image/jpg')

@post('/<name:re:cam-[^.]+>')
def response(name):
    print(name)

@post('/fetch')
def picture():
    fetch()

@post('/warning')
def bell():
    warning()

run(host='0.0.0.0', port=8080)
