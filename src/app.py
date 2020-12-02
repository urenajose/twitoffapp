from flask import Flask, render_template
from .models import DB

def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_db.sqlite'
	DB.init_app(app)

	@app.route('/')
	def index():
	    return 'Index page'

	@app.route('/hello/')
	@app.route('/hello/<name>')
	def hello(name=None):
	    return render_template('my_template.html', name=name)

	return app