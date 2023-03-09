__author__ = 'Tarrok'

import uuid
import datetime
from web_1.class_2.terminal_blog.database import Database


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), post_id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.created_date = date
        self.post_id = uuid.uuid4().hex if post_id is None else post_id # crea un id, salvo que te entregue un id yo

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'post_id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   post_id=post_data['post_id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]

    def json(self):
        return{
            'post_id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }



