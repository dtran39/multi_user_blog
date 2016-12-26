import os
import re

import webapp2
import jinja2
from all_pages import Register, Login, Logout, Welcome, Post, BlogFront, PostPage, NewPost, MainPage
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/welcome', Welcome),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ],
                              debug=True)
