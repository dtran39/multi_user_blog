"""This module has Login class"""
from all_models import User
from pages.base_render import BlogHandler

class Login(BlogHandler):
    """This class implements login functionality of the web app"""
    def get(self):
        """Rendering login page"""
        self.render('login.html', error=self.request.get('error'))

    def post(self):
        """Processing login information"""
        username = self.request.get('username')
        password = self.request.get('password')

        user = User.login(username, password)
        if user:
            self.login(user)
            self.redirect('/')
        else:
            self.render('login.html', error="Invalid username or password")
