import os
import re

import webapp2
import jinja2
from all_pages import   (Register, Login, Logout, Post,
                        BlogHandler, BlogFront,
                        PostPage, NewPost, DeletePost, EditPost,
                        DeleteComment, EditComment)

app = webapp2.WSGIApplication([
                               ('/signup', Register),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/new', NewPost),
                               ('/edit/([0-9]+)', EditPost),
                               ('/delete/([0-9]+)', DeletePost),
                               ('/deletecomment/([0-9]+)/([0-9]+)', DeleteComment),
                               ('/editcomment/([0-9]+)/([0-9]+)', EditComment)
                               ],
                              debug=True)
