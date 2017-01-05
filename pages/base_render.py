"""This module has BlogHandler class"""
import webapp2
from pages.global_helpers import (jinja_render_str, make_secure_val,
                                  check_secure_val)
from all_models import User
# Base blog handler


class BlogHandler(webapp2.RequestHandler):
    """This class use jinja to render pages"""
    def render_str(self, template, **params):
        """This method render a string with user"""
        params['user'] = self.user
        return jinja_render_str(template, **params)

    def render(self, template, **kw):
        """This method write the rendered page"""
        self.response.out.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        """This method set the cookie"""
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        """This method double check the cookies"""
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        """This method implement login"""
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        """This method implements logout"""
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        """This method initialize handling"""
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
