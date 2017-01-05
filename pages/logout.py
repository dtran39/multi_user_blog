"""This module has the Logout class"""
from pages.base_render import BlogHandler


class Logout(BlogHandler):
    """This class implements logout functionality of the webapp"""
    def get(self):
        """This method implements logout functionality"""
        self.logout()
        self.redirect('/')
