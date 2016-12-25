import os
import re

import webapp2
import jinja2
from user import User
from base_render import BlogHandler
from signup import Register
from login import Login
from logout import Logout
from welcome import Welcome

class MainPage(BlogHandler):
  def get(self):
      self.write('Hello, Udacity!')

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/welcome', Welcome),
                               ],
                              debug=True)
