import os
import re
from string import letters
from base_render import BaseHandler
import webapp2

from google.appengine.ext import db
# Hello world main page
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
# Signup page
class Signup(BaseHandler):
    def get(self):
        self.render("signup-form.html")
    def post(self):
        self.redirect('/welcome')
# Welcome after finish signing up
class Welcome(BaseHandler):
    def get(self):
        self.render("welcome.html", username = "trananhduc1004")
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
