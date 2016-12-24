import re
from base_render import BaseHandler
# Signup page
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def check_valid_field(field, field_re):
    return field and field_re.match(field)
class Signup(BaseHandler):
    def get(self):
        self.render("signup-form.html")
    def post(self):
        error = False
        # Creat a list of parameters for to store if post is invalid
        params = {}
        # Get and validate each field:
        # username
        username = self.request.get('username')
        if not check_valid_field(username, USER_RE):
            params['username'] = username
            params['error_username'] = "That's not a valid username."
            error = True
        # email
        email = self.request.get('email')
        if not check_valid_field(email, EMAIL_RE):
            params['email'] = email
            params['error_email'] = "That's not a valid email."
            error = True
        # password
        password = self.request.get('password')
        if not check_valid_field(password, PASS_RE):
            params['error_password'] = "That's not a valid password."
            error = True
        # password verification
        password_verify = self.request.get('verify')
        if password_verify != password:
            params['error_verify'] = "Password doesn't match verification."
            error = True
        if error:
            self.render('signup-form.html', **params)
        else:
            self.redirect('/welcome?username=' + username)
