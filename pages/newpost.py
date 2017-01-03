"""This module has NewPost class"""
from pages.global_helpers import blog_key
from pages.base_render import BlogHandler
from pages.post import Post

class NewPost(BlogHandler):
    """This class implements adding a new post"""
    def get(self):
        """This method render adding a new post page"""
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        """This method process new post information"""
        if not self.user:
            self.redirect('/')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            new_post = Post(parent=blog_key(), user_id=self.user.key().id(),
                            username=self.user.name, subject=subject, content=content)
            new_post.put()
            self.redirect('/blog/%s' % str(new_post.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error)
