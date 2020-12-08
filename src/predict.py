import numpy as np
import spacy
from sklearn.neighbors import KNeighborsClassifier
from .models import User


def predict_user(user1_name, user2_name, tweet_text):
	user1 = User.query.filter(User.name == user1_name).one()
	user2 = User.query.filter(User.name == user2_name).one()

	user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
	user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
 	# X
	embeddings = np.vstack([user1_embeddings, user2_embeddings])
	# y
	labels = np.concatinate([np.ones(len(user1.tweets)), 
							 np.zeros(len(user2.tweets))]) 

	knnc = KNeighborsClassifier().fit(embedding, labels)
	nlp = spacy.load('en_core_web_lg')
	tweet_embedding = nlp(tweet_text).vector
	pred = knnc.predict(tweet_embedding)
	return pred