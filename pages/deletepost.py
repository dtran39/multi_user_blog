from google.appengine.ext import db
from global_helpers import blog_key
from base_render import BlogHandler
class DeletePost(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if post.user_id == self.user.key().id():
                post.delete()
                self.redirect("/?deleted_post_id="+post_id)
            else:
                self.redirect("/blog/" + post_id + "?error=You don't have " +
                              "access to delete this record.")
        else:
            self.redirect("/login?error=You need to be logged, in order" +
                          " to delete your post!!")
