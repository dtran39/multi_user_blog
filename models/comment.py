"""This module has Comment class"""
from google.appengine.ext import db
from models.user import User
from models.post import PostModel


class Comment(db.Model):
    """This class is the model of a comment"""
    # Data redundancy to avoid table joining
    user = db.ReferenceProperty(User, collection_name='comments', required=True)
    post = db.ReferenceProperty(PostModel, collection_name='comments', required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
