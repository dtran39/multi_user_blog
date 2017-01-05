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
            post_to_be_deleted = db.get(key)
            # Check that post exist
            if not post_to_be_deleted:
                return
            # Check that current user owns the post
            if post_to_be_deleted.user.key().id() == self.user.key().id():
                # Remember to delete comments and likes
                for a_like in post_to_be_deleted.likes:
                    a_like.delete()
                for a_comment in post_to_be_deleted.comments:
                    a_comment.delete()
                post_to_be_deleted.delete()
                self.redirect("/?deleted_post_id="+post_id)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Deleting other's post is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")
