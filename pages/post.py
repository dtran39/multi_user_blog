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

        likes = db.GqlQuery("select * from Like where post_id="+post_id)
        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + " order by created desc")
        if not post:
            self.error(404)
            return
        error = self.request.get('error')
        self.render("permalink.html", post=post, numOfLikes=likes.count(),
                    comments=comments, error=error)
    def post(self, post_id):
        """This method process adding/editing comments and adding like"""
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return
        new_comment = ""
        if self.user:
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
                    new_like = Like(parent=blog_key(), user_id=self.user.key().id(),
                                    post_id=int(post_id))
                    new_like.put()
            if self.request.get('comment'):
                new_comment = Comment(parent=blog_key(), user_id=self.user.key().id(),
                                      post_id=int(post_id),
                                      comment=self.request.get('comment'))
                new_comment.put()
        else:
            self.redirect("/login?error=You need to login before " +
                          "performing edit, like or commenting.!!")
            return
        likes = db.GqlQuery("select * from Like where post_id="+post_id)
        comments = db.GqlQuery("select * from Comment where post_id = " +
                               post_id + "order by created desc")

        self.render("permalink.html", post=post, numOfLikes=likes.count(),
                    comments=comments, new=new_comment)
