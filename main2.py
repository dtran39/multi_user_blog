import webapp2
from base_render import BaseHandler
from signup import Signup
from welcome import Welcome


# Hello world main page
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signup', Signup),
    ('/welcome', Welcome)
], debug=True)
