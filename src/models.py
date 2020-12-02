from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(30), nullable=False)

class Tweet(DB.Model):
	id = DB.Column(DB.Integer, primary_key=True)
	text = DB.Column(DB.Unicode(280), nullable=False)


# flask shell
# >>> from src.models import DB, User
# >>> DB.create_all()
# >>> user1 = User(name='elonmusk')
# >>> DB.session.add(user1)
# >>> DB.session.commit()
# >>> user2 = User(name='billgates')
# >>> DB.session.add(user2)
# >>> DB.session.commit()
# >>> from src.models import Tweet
# >>> tweet1 = Tweet(text='this is my tweet!!!')
# >>> DB.session.add(tweet1)
# >>> DB.session.commit()