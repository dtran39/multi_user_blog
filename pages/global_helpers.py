import os
import jinja2
import hmac
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)
def jinja_render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)

def make_secure_val(val):
    secret = 'duc_tran'
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val
