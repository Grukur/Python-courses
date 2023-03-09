from web_1.class_2.terminal_blog.database import Database
from web_1.class_2.terminal_blog.menu import Menu
from web_1.class_2.terminal_blog.models.blog import Blog
from web_1.class_2.terminal_blog.models.post import Post

__author__ = 'Tarrok'

Database.initialaize()


# import pymongo
#
# uri = 'mongodb://127.0.0.1:27017'
# client = pymongo.MongoClient(uri)
# database = client['test']
# collection = database['students']
#
# # students = collection.find({})
#
# print([student for student in collection.find({})])

# post = Post(blog_id='123',
#             title='Testeando el blog por segunda vez',
#             content='cuando uno quiere ir de vacaciones, falta el tiempo o la energia',
#             author='Tarrok')

# post.save_to_mongo()

# [print(post) for post in Post.from_blog('123')]

# blog = Blog(author='Tarrok',
#             title='Novedades',
#             description='esta es una prueba de Blog_1')
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = blog.from_mongo(blog.id)
#
# print(blog.get_posts())

menu = Menu()
menu.run_menu()

