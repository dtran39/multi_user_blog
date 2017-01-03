"""This module has Like class"""
from google.appengine.ext import db
from models.user import User

class Like(db.Model):
    """This class is the model of a like"""
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)
