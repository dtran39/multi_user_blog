"""This module has BlogFront class"""
from pages.base_render import BlogHandler
from pages.post import Post

class BlogFront(BlogHandler):
    """This class render the blog feed page of the app"""
    def get(self):
        """This method render the front page (blog feed) of the app"""
        deleted_post_id = self.request.get('deleted_post_id')
        posts = Post.all().order('-created')
        self.render('front.html', posts=posts, deleted_post_id=deleted_post_id)
