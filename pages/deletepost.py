"""This method has DeletePost class"""
from google.appengine.ext import db
from pages.global_helpers import blog_key
from pages.base_render import BlogHandler
class DeletePost(BlogHandler):
    """This class implemetn deleting a blogpost"""
    def get(self, post_id):
        """This method implement deleting a blogpost"""
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if post.user_id == self.user.key().id():
                post.delete()
                # Remember to delete comments and likes
                likes = db.GqlQuery("select * from Like where post_id="+post_id)
                for a_like in likes:
                    a_like.delete()
                comments = db.GqlQuery("select * from Comment where post_id=" + post_id)
                for a_comment in comments:
                    a_comment.delete()
                self.redirect("/?deleted_post_id="+post_id)
            else:
                self.redirect("/blog/" + post_id + "?error=Deleting other's post is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")
