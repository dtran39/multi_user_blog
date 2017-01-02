"""This module has class Signup, and some regex functions to check info validity"""
import re
from all_models import User
from pages.base_render import BlogHandler

def valid_username(username):
    """Check username validity"""
    valid_username_regex = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return username and valid_username_regex.match(username)

def valid_password(password):
    """Check password validity"""
    valid_password_regex = re.compile(r"^.{3,20}$")
    return password and valid_password_regex.match(password)

def valid_email(email):
    """Check email validity"""
    valid_email_regex = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    return not email or valid_email_regex.match(email)

class Signup(BlogHandler):
    """This class implements signup functionality of the web app"""
    def __init__(self):
        self.username = ""
        self.password = ""
        self.verify = ""
        self.email = ""
    def get(self):
        """Render sign up page"""
        self.render("signup.html")

    def post(self):
        """Process signup info"""
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username=self.username, email=self.email)

        if not valid_username(self.username):
            params['error_username'] = "Invalid username"
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "Invalid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Passwords don't match"
            have_error = True

        if not valid_email(self.email):
            params['error_email'] = "Invalid email"
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        """This class implements what happens afterward"""
        raise NotImplementedError

class Register(Signup):
    """This class implement registration functionality"""
    def done(self):
        """This class check if username has already exist"""
        user = User.by_name(self.username)
        if user:
            self.render('signup.html', error_username="Username already taken")
        else:
            user = User.register(self.username, self.password, self.email)
            user.put()
            self.login(user)
            self.redirect('/')
