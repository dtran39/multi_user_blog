import os
import re
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db
# Global variables:
# String full path of the template directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# Jinja environment (load template directory to jinja)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)
# Base Handler
class BaseHandler(webapp2.RequestHandler):
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.response.out.write(self.render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
# Hello world main page
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
class Signup(BaseHandler):
    def get(self):
        self.render("signup-form.html")
class Welcome(BaseHandler):
    def get(self):
        self.render("welcome.html", username = "trananhduc1004")
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
