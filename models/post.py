"""This module has Post class"""
from google.appengine.ext import db
from models.user import User

class PostModel(db.Model):
    """This class is the model of a post"""
    user_id = db.IntegerProperty(required=True)
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def getUserName(self):
        """This method get the username of the post"""
        user = User.by_id(self.user_id)
        return user.name
