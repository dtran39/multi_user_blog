import os
import re

import webapp2
import jinja2
from all_pages import   (MainPage, Register, Login, Logout, Post,
                        BlogHandler, BlogFront,
                        PostPage, NewPost, DeletePost)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/deletepost/([0-9]+)', DeletePost),
                               ],
                              debug=True)
