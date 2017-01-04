"""This module has EditComment class"""
from pages.base_render import BlogHandler
from pages.global_helpers import blog_key
from google.appengine.ext import db

class EditComment(BlogHandler):
    """This class implement editing a comment"""
    def get(self, post_id, comment_id):
        """This method render the comment edition page"""
        if self.user:
            key = db.Key.from_path('Comment', int(comment_id),
                                   parent=blog_key())
            comment_to_be_edited = db.get(key)
            # Checking comment exist
            if not comment_to_be_edited:
                return
            # Checking user owns the comment
            if comment_to_be_edited.user_id == self.user.key().id():
                self.render("editcomment.html", comment=comment_to_be_edited.comment)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Editing other's comment is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")

    def post(self, post_id, comment_id):
        """This method process comment edition information"""
        if not self.user:
            self.redirect('/')

        comment = self.request.get('comment')

        if comment:
            key = db.Key.from_path('Comment',
                                   int(comment_id), parent=blog_key())
            edited_comment = db.get(key)
            # Checking comment exist
            if not edited_comment:
                return
            # Checking that user owns that edited comment
            if edited_comment.user_id == self.user.key().id():
                edited_comment.comment = comment
                edited_comment.put()
                self.redirect('/blog/' + post_id)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Editing other's comment is prohibited.")
        else:
            error = "comment needed"
            self.render("editcomment.html", comment=comment, error=error)
