from base_render import BaseHandler
# Signup page
class Signup(BaseHandler):
    def get(self):
        self.render("signup-form.html")
    def post(self):
        self.redirect('/welcome')
