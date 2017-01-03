"""This module has Comment class"""
from google.appengine.ext import db
from models.user import User


class Comment(db.Model):
    """This class is the model of a comment"""
    # Data redundancy to avoid table joining
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    def getUserName(self):
        """This method get the username of the comment"""
        user = User.by_id(self.user_id)
        return user.name
