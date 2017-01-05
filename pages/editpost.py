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
            if post_to_be_edited.user.key().id() == self.user.key().id():
                self.render("editpost.html", subject=post_to_be_edited.subject,
                            content=post_to_be_edited.content, post_id=post_id)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Editing other's post is prohibited.")
        else:
            self.redirect("/login?error=Login is required.")

    def post(self, post_id):
        """This method process editing information"""
        if not self.user:
            return self.redirect('/login')
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post_to_be_edited = db.get(key)
            # Check if edited post exist
            if not post_to_be_edited:
                return
            # Check if user owns that edited post
            if post_to_be_edited.user.key().id() == self.user.key().id():
                post_to_be_edited.subject = subject
                post_to_be_edited.content = content
                post_to_be_edited.put()
                self.redirect('/blog/' + post_id)
            else:
                self.redirect("/blog/" + post_id +
                              "?error=Editing other's post is prohibited.")
        else:
            error = "subject and content, please!"
            self.render("editpost.html", subject=subject,
                        content=content, error=error)
