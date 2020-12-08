from flask import Flask, render_template
from .models import DB, User
from decouple import config


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
	DB.init_app(app)

	@app.route('/')
	def root():
		DB.create_all()
		users = User.query.all()
		return render_template('base.html', title='Home', users=users)

	@app.route('/reset')
	def reset():
		DB.drop_all()
		DB.create_all()
		return render_template('base.html', title='Reset database!')

	return app