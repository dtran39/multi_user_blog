"""This module has helper functions for other modules"""
import os
import hmac
import jinja2
from google.appengine.ext import db

def jinja_render_str(template, **params):
    """This module use jinja to render string"""
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                                   autoescape=True)
    template = jinja_env.get_template(template)
    return template.render(params)


def blog_key(name='default'):
    """this function get the blog key"""
    return db.Key.from_path('blogs', name)

def make_secure_val(val):
    """This module make a hash from a string"""
    secret = 'duc_tran'
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    """This function check if the hashed value matches"""
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val
