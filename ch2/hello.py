# init
from flask import Flask
#from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager


app = Flask(__name__)
manager =Manager(app)


@app.route('/')
def index():
	#response = make_response('<h1>This document carries a cookie!</h1>')
	#response.set_cookie('answer', '42')
	#return response
	return redirect('https://www.baidu.com')

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s!</h1>'% user.name

@app.route('/User/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
	manager.run()
