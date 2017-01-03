"""This module is the entry point of Google App Engine application"""
import webapp2
from all_pages import (Register, Login, Logout, BlogFront, PostPage,
                       NewPost, DeletePost, EditPost, DeleteComment, EditComment)
app = webapp2.WSGIApplication([
    ('/?', BlogFront),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/new', NewPost),
    ('/blog/edit/([0-9]+)', EditPost),
    ('/blog/delete/([0-9]+)', DeletePost),
    ('/blog/deletecomment/([0-9]+)/([0-9]+)', DeleteComment),
    ('/blog/editcomment/([0-9]+)/([0-9]+)', EditComment),
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout)    
    ], debug=True)
