from web_1.class_2.terminal_blog.database import Database
from web_1.class_2.terminal_blog.models.blog import Blog

__author__ = 'Tarrok'


class Menu(object):
    def __init__(self):
        self.user = input('Enter your author name: ')
        self.user_blog = None
        if self._user_has_account():
            print(f'Welcome back {self.user}')
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input('Enter blog title: ')
        description = input('Enter blog description: ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input('Do you want to read (R) or write (W) blogs? ').lower()
        if read_or_write == 'r':
            self._list_blogs()
            self._view_blog()
            pass # verificar porque esta ahi
        elif read_or_write == 'w':
            self.user_blog.new_post()
        else:
            print('Thank you for blogging')

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                               query={})
        for blog in blogs:
            print(f"ID: {blog['id']}, Title: {blog['title']}, Author: {blog['author']}")

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print(f"Date: {post['created_date']}, title {post['title']}\n\n{post['content']}")


