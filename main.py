import os
import re

import webapp2
import jinja2
from all_pages import   (MainPage, Register, Login, Logout, Post,
                        BlogHandler, BlogFront,
                        PostPage, NewPost, DeletePost, EditPost,
                        DeleteComment, EditComment)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/editpost/([0-9]+)', EditPost),
                               ('/blog/deletepost/([0-9]+)', DeletePost),
                               ('/blog/deletecomment/([0-9]+)/([0-9]+)', DeleteComment),
                               ('/blog/editcomment/([0-9]+)/([0-9]+)', EditComment)
                               ],
                              debug=True)
