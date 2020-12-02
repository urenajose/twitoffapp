from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(30), nullable=False)

class Tweet(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	text = DB.Column(DB.Unicode(280), nullable=False)
	user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
	user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

	def __repr__(self):
		return f'<Tweet: {self.text}>'


# flask shell
# >>> from src.models import DB, User, Tweet
# >>> DB.create_all()
# >>> user1 = User(name='elonmusk')
# >>> user2 = User(name='billgates')
# >>> tweet1 = Tweet(text='What if Mars was like Earth?')
# >>> tweet2 = Tweet(text='coding is not difficult')
# >>> user1.tweets.append(tweet1)
# >>> user1.tweets.append(tweet2)
# >>> tweet3 = Tweet(text='Windows is amazing!!!')
# >>> user2.tweets.append(tweet3)
# >>> DB.session.add(user1)
# >>> DB.session.add(user2)
# >>> DB.session.commit()