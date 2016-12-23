from base_render import BaseHandler
# Welcome after finish signing up
class Welcome(BaseHandler):
    def get(self):
        self.render("welcome.html", username = self.request.get('username'))
