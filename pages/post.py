from google.appengine.ext import db
from all_models import PostModel
from global_helpers import jinja_render_str, blog_key
from base_render import BlogHandler

class Post(PostModel):
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return jinja_render_str("post.html", p = self)

class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        self.render("permalink.html", post = post)
