"""This module has Post class"""
from google.appengine.ext import db
from models.user import User

class PostModel(db.Model):
    """This class is the model of a post"""
    # Data redundancy to avoid table joining
    user = db.ReferenceProperty(User, collection_name='posts', required=True)    
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
