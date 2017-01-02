from base_render import BlogHandler
from post import Post

class BlogFront(BlogHandler):
    def get(self):
        deleted_post_id = self.request.get('deleted_post_id')
        posts = greetings = Post.all().order('-created')
        self.render('front.html', posts = posts, deleted_post_id=deleted_post_id)
