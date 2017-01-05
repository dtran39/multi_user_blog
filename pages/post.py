"""This module has Post(just the post itself) and PostPage (with comments and likes)"""
from google.appengine.ext import db
from all_models import PostModel, Comment, Like
from pages.global_helpers import jinja_render_str, blog_key
from pages.base_render import BlogHandler

class Post(PostModel):
    """This class render a single post and its meta information"""
    def render(self):
        """This method render a single post"""
        self._render_text = self.content.replace('\n', '<br>')
        return jinja_render_str("post.html", p=self)

class PostPage(BlogHandler):
    """This class render a single post, its meta info and its likes and comments"""
    def get(self, post_id):
        """This method render the a post, its like and comments"""
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            self.error(404)
            return
        likes = post.likes
        comments = post.comments.order("-created")
        self.render("permalink.html", post=post, numOfLikes=likes.count(),
                    comments=comments, error=self.request.get('error'))
    def post(self, post_id):
        """This method process adding/editing comments and adding like"""
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if not post:
            self.error(404)
            return
        new_comment = ""
        if self.user:
            # If user comment on the post, update db
            if self.request.get('comment'):
                new_comment = Comment(parent=blog_key(), user=self.user,
                                      post=post,
                                      comment=self.request.get('comment'))
                new_comment.put()
            # If user like the post, check and update db if needed
            if(self.request.get('like') and self.request.get('like') == "update"):
                # Prevent liking your own post
                if self.user.key().id() == post.user.key().id():
                    self.redirect("/blog/" + post_id +
                                  "?error=Liking your own post is prohibited")
                    return
                likes = post.likes.filter('user =', self.user)
                # If haven't like yet, like
                if likes.count() == 0:
                    new_like = Like(parent=blog_key(), user=self.user,
                                    post=post)
                    new_like.put()
                # If already like, unlike
                elif likes.count() == 1:
                    for a_like in likes:
                        a_like.delete()
        else:
            self.redirect("/login?error=Login required to like or comment")
            return
        likes = post.likes
        comments = post.comments.order("-created")
        self.render("permalink.html", post=post, numOfLikes=likes.count(),
                    comments=comments, new=new_comment)
