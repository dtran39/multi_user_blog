from base_render import BlogHandler
class MainPage(BlogHandler):
  def get(self):
      self.write('Hello, Udacity!')
