from google.appengine.ext import db
from all_models import PostModel
from global_helpers import jinja_render_str
from base_render import BlogHandler

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)
class Post(PostModel):
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return jinja_render_str("post.html", p = self)
