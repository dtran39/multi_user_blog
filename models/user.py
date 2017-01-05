"""This module has User class and some global functions to handle user data"""
import hashlib
import random
from string import letters
from google.appengine.ext import db


def make_salt(length=5):
    """This function create salt"""
    return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, password, salt=None):
    """This function create hash"""
    if not salt:
        salt = make_salt()
    hashed = hashlib.sha256(name + password + salt).hexdigest()
    return '%s,%s' % (salt, hashed)


def valid_pw(name, password, hashed):
    """This function check two hashes to see if it matches"""
    salt = hashed.split(',')[0]
    return hashed == make_pw_hash(name, password, salt)


def users_key(group='default'):
    """This function get user key"""
    return db.Key.from_path('users', group)


class User(db.Model):
    """This class represent an user"""
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, uid):
        """This method get user object's id"""
        return User.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        """This method get user by looking at their username"""
        user = User.all().filter('name =', name).get()
        return user

    @classmethod
    def register(cls, name, password, email=None):
        """This method register user to the db"""
        pw_hash = make_pw_hash(name, password)
        return User(parent=users_key(),
                    name=name,
                    pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, name, password):
        """This method perform login to the db"""
        user = cls.by_name(name)
        if user and valid_pw(name, password, user.pw_hash):
            return user
