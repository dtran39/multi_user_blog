"""This module has Like class"""
from google.appengine.ext import db
from models.user import User
from models.post import PostModel


class Like(db.Model):
    """This class is the model of a like"""
    user = db.ReferenceProperty(User, collection_name='likes', required=True)
    post = db.ReferenceProperty(PostModel, collection_name='likes',
                                required=True)
