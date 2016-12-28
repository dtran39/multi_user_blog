from google.appengine.ext import db
from all_models import PostModel
from base_render import BlogHandler, render_str

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)
class Post(PostModel):
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self)
