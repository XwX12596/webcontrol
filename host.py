from bottle import run, get, post, static_file, template
from face_recognition import GetFace as face

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
def test():
    face()

run(host='localhost', port=8080)

# @get('/')
# def login():
#     return '''
#         <form action="/index" method="post">
#             Username: <input name="username" type="text" />
#             Password: <input name="password" type="password" />
#             <input value="Login" type="submit" />
#         </form>
#     '''

# @post('/index')
# def do_login():
#     username = request.forms.get('username')
#     password = request.forms.get('password')
#     def check_login(username, password):
#         if username == 'xwx' and password == 'Hh20011212.':
#             return True
#     if check_login(username, password):
#         return template("index")
#     else:
#         return "<p>Login failed.</p>"

