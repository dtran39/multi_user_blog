from google.appengine.ext import db
from all_models import PostModel, Comment, Like
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

        likes = db.GqlQuery("select * from Like where post_id="+post_id)
        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + " order by created desc")
        if not post:
            self.error(404)
            return
        error = self.request.get('error')
        self.render("permalink.html", post = post, numOfLikes = likes.count(),
            comments = comments, error = error)
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        c = ""
        if(self.user):
            # On clicking like, post-like value increases.
            if(self.request.get('like') and
               self.request.get('like') == "update"):
                likes = db.GqlQuery("select * from Like where post_id = " +
                                    post_id + " and user_id = " +
                                    str(self.user.key().id()))

                if self.user.key().id() == post.user_id:
                    self.redirect("/blog/" + post_id +
                                  "?error=You cannot like your " +
                                  "post.!!")
                    return
                elif likes.count() == 0:
                    l = Like(parent=blog_key(), user_id=self.user.key().id(),
                             post_id=int(post_id))
                    l.put()
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
        likes = db.GqlQuery("select * from Like where post_id="+post_id)
        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + "order by created desc")

        self.render("permalink.html", post=post, numOfLikes = likes.count(), comments = comments, new = c)
