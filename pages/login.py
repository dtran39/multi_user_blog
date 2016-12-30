from all_models import User
from base_render import BlogHandler

class Login(BlogHandler):
    def get(self):
        self.render('login.html', error=self.request.get('error'))

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            self.render('login.html', error = "Invalid username or password")
