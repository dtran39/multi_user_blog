import os
import re

import webapp2
import jinja2
from all_pages import   (MainPage, Register, Login, Logout, Post,
                        BlogHandler, BlogFront, PostPage, NewPost)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ],
                              debug=True)
