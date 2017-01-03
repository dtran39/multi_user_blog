"""This module is the entry point of Google App Engine application"""
import webapp2
from all_pages import (Register, Login, Logout, BlogFront, PostPage,
                       NewPost, DeletePost, EditPost, DeleteComment, EditComment)
app = webapp2.WSGIApplication([
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/?', BlogFront),
    ('/blog/new', NewPost),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/([0-9]+)/edit', EditPost),
    ('/blog/([0-9]+)/delete', DeletePost),
    ('/blog/([0-9]+)/([0-9]+)/delete', DeleteComment),
    ('/blog/([0-9]+)/([0-9]+)/edit', EditComment),
    ], debug=True)
