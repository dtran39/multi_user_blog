from google.appengine.ext import db
from all_models import PostModel, Comment
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

        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + " order by created desc")
        if not post:
            self.error(404)
            return
        error = self.request.get('error')
        self.render("permalink.html", post = post, comments = comments, error = error)
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        c = ""
        if(self.user):
            # On commenting, it creates new comment tuple
            if(self.request.get('comment')):
                c = Comment(parent=blog_key(), user_id=self.user.key().id(),
                            post_id=int(post_id),
                            comment=self.request.get('comment'))
                c.put()
        else:
            self.redirect("/login?error=You need to login before " +
                          "performing edit, like or commenting.!!")
            return

        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + "order by created desc")

        self.render("permalink.html", post=post, comments = comments, new=c)
