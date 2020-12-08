"""Prediction of Users based on Tweet embeddings."""
import numpy as np
import spacy

from sklearn.neighbors import KNeighborsClassifier
from .models import User


def predict_user(user1_name, user2_name, tweet_text):
    """Determine and return which user is more likely to say a given Tweet."""

    user1 = User.query.filter(User.name == user1_name).one()
    user2 = User.query.filter(User.name == user2_name).one()
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweets])
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweets])
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([np.ones(len(user1.tweets)),
                             np.zeros(len(user2.tweets))])
    knnc = KNeighborsClassifier(weights='distance', metric='cosine').fit(embeddings, labels)
    nlp = spacy.load('en_core_web_lg')
    tweet_embedding = list(nlp(tweet_text).vector)
    return knnc.predict(np.array(tweet_embedding).reshape(1, -1))
