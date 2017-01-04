"""This module has EditPost class"""
from google.appengine.ext import db
from pages.base_render import BlogHandler
from pages.global_helpers import blog_key

class EditPost(BlogHandler):
    """This class implements editing a blogpost"""
    def get(self, post_id):
        """This method implements editing a blogpost page"""
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post_to_be_edited = db.get(key)
            # Check if post existed
            if not post_to_be_edited:
                return
            if post_to_be_edited.user_id == self.user.key().id():
                self.render("editpost.html", subject=post_to_be_edited.subject,
                            content=post_to_be_edited.content, post_id=post_id)
            else:
                self.redirect("/blog/" + post_id + "?error=Editing other's post is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")

    def post(self, post_id):
        """This method process editing information"""
        if not self.user:
            self.redirect('/')
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            edited_post = db.get(key)
            # Check if edited post exist
            if not edited_post:
                return
            # Check if user owns that edited post
            if edited_post.user_id == self.user.key().id():
                edited_post.subject = subject
                edited_post.content = content
                edited_post.put()
                self.redirect('/blog/' + post_id)
            else:
                self.redirect("/blog/" + post_id + "?error=Editing other's post is prohibited.")
        else:
            error = "subject and content, please!"
            self.render("editpost.html", subject=subject,
                        content=content, error=error)
