from flask import Flask, render_template

def create_app():
	app = Flask(__name__)

	@app.route('/')
	def index():
	    return 'Index page'

	@app.route('/hello/')
	@app.route('/hello/<name>')
	def hello(name=None):
	    return render_template('my_template.html', name=name)

	return app