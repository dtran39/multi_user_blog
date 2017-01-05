"""This module has DeleteComment class"""
from pages.base_render import BlogHandler
from pages.global_helpers import blog_key
from google.appengine.ext import db


class DeleteComment(BlogHandler):
    """This class implement deleting a comment"""
    def get(self, post_id, comment_id):
        """This method implement deleting a comment"""
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            comment_to_be_deleted = db.get(key)
            # Check if comment exist
            if not comment_to_be_deleted:
                return
            # Check if user owns that comment
            if comment_to_be_deleted.user.key().id() == self.user.key().id():
                comment_to_be_deleted.delete()
                self.redirect("/blog/"+post_id+"?deleted_comment_id=" +
                              comment_id)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Deleting other's comment is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")
