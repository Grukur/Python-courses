#               TRABAJANDO CON SETS

# friends = {'rolf', 'anna', 'bob', 'mike'}
# abroad = {'ron', 'anna', 'ed'}
#
# local_friends = abroad.difference(friends)  # extrae los que no se comparten
# print(local_friends)
#
# local_friends = abroad.union(friends)  # junta todo
# print(local_friends)
#
# local_friends = abroad.intersection(friends)  # extrae lo comun
# print(local_friends)

"""
para abrir un set vacio, debes usar set(), ya que {} significa diccionario
"""

#               THE IN KEYBOARD

# number = '7'
# user = input('You want play this game? Y/n ').lower()
#
# while user == 'y':
#     user_game = input('Guess the number or press "n" to finish the game: ').lower()
#     if user_game == 'n':
#         user = 'n'
#     elif user_game == number:
#         print('You got it!!')
#         break
#     elif abs(int(number) - int(user_game)) == 1:
#         print('You fail for 1, try again, you are close')
#     else:
#         print('you are wrong for far')

#           LIST COMPREHENSION

# number = [1, 3, 5]
#
# doubled = [x*2 for x in number]
# print(doubled)
#
#
# friends = {'rolf', 'sanna', 'sam', 'saurah', 'mike'}
# friends_s = [x for x in friends if x.startswith('s')]
# print(friends_s)

#           DICTIONARIES


# def add(x, y=5):
#     result = x + y
#     print(result)
#
#
# def say_hello(name, surname):
#     print(f'Hello {name} {surname}')
#
#
# add(5, 3)
# add(8)
# say_hello('Bob', 'Dylan')
# say_hello(name='Bob', surname='Marley')

#           LAMBDA


# def add(x, y):
#     return x + y
#
#
# add1 = lambda x, y: x + y
# add2 = ((lambda x, y: x + y)(8, 9)) # asi se usa el lambda para agregar valores
#
# print(add(5, 2))
# print(add1(5, 7))
# print(add2)
#
# def double(x):
#     return x *2
#
#
# sequence = [1, 2, 5, 8]
#
# doubled = [double(x) for x in sequence] # la forma en python
# doubled1 = map(double, sequence) # el map se usa en otros codigos, ya que no cuenta con comprehension
# doubled2 = [(lambda x: x * 2)(x) for x in sequence]
# este lambda funciona sin necesidad de la funcion, pero es algro tricky
# doubled3 = list(map(lambda x: x * 2, sequence)) # esto para que sea mas leible y sin usar la funcion

#           DICTIONARY COMPREHENSION

# users = \
#     [
#         (0, "Bob", "password"),
#         (1, 'Rolf', 'bob123'),
#         (2, 'Jose', 'lonp5487'),
#         (3, 'username', '1234')
#     ]
#
# username_mapping = {user[1]: user for user in users}
#
# for user in users:
#     if user[1] == "Bob": # esto es igual a el comprehension de arriba
#         print(user)
#
# print(username_mapping)
#
# username_input = input('Please write you username')
# password_input = input('Please write you password')
#
# _, username, password = username_mapping[username_input]
#
# if password_input == password:
#     print('welcome god')
# else:
#     print('You are not God')

#           UNPACKING


# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total *= arg
#
#
# def apply(*args, operator):
#     if operator == "*":
#         return multiply(*args)
#     elif operator == '+':
#         return sum(args)
#     else:
#         return 'No valid operator provided to apply()'
#
#
# print(apply(1, 3, 6, 7, operator='*'))
# print(multiply(1, 3, 5))
#
#
# def add(x, y):
#     return x + y
#
# nums = [3, 5]
# nums2 = {'x': 15, 'y': 25}
#
# print(add(*nums))   # unpackin en normal
# print(add(**nums2)) # unpackin en diccionarios
#
#
# def named(**kwargs):
#     print(kwargs)
#
#
# dictionary1 = {'name': 'Bobloop', 'age': "65"}
#
# named(name='bob', age=25)
# named(**dictionary1)
#
#
# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# both(1, 2, 3, name='Bobby', age='45')

#           OBJECT ROIENTED

# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True
#
#     def __str__(self):
#         return f'Device {self.name!r} ({self.connected_by})'
#
#     def disconneced(self):
#         self.connected = False
#         print('Disconnected')
#
# class Printer(Device):      # inherit, hereda todo de Device y suma nuevos entrys "capacity"
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining = capacity
#
#     def __str__(self):
#         return f'{super().__str__()} ({self.remaining} pages remaining'
#
#     def print(self, pages):
#         if not self.connected:
#             print('You printer is not connected')
#             return
#         print(f'Printing {pages} pages.')
#         self.remaining -= pages
#
#
# printer = Printer('Printer', 'USB', 500)
# printer.print(20)
#
# print(printer)

#           CLASS COMPOSITION

# class BookShelf:
#     def __init__(self, *books):
#         self.books = books
#
#     def __str__(self):
#         return f'BookShelf with {len(self.books)} books'
#
#
# class Book:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Book {self.name}'
#
#     def __repr__(self):
#         return f'Book {self.name}'
#
#
# book1 = Book('Harry Potter')
# book2 = Book('Python 101')
# shelf = BookShelf(book1, book2)
#
# print(shelf)            # aqui el usario llama a shelf
# print(shelf.books)      # aqui el usario llama a shelf, pero shelf (programa) llama a books, por eso usa repr

#           ERRORs

# class TooManyPagesReadError(ValueError):
#     pass
#
#
# class Book:
#     def __init__(self, name, page_count):
#         self.name = name
#         self.page_count = page_count
#         self.page_read = 0
#
#     def __repr__(self):
#         return f'Book {self.name}, read {self.page_read} pages out of {self.page_count}'
#
#     def read(self, pages):
#         if self.page_read + pages > self.page_count:
#             raise TooManyPagesReadError\
#                 (f'You tried to read {self.page_read + pages} pages, but this book only has {self.page_count} pages')
#         self.page_read += pages
#         print(f'You have now read {self.page_read} pages out of {self.page_count} pages')
#
#
# python101 = Book('python 101', 50)
#
# try:
#     python101.read(35)
#     python101.read(50)
# except TooManyPagesReadError as e:
#     print(e)

#           FIRST CLASS FUNCTIONs

"""
se refiere a que usamos una funcion para llamar a otra, como si fuesen clases, el origen de los decoradores
"""

#           DECORATORS

# import functools
#
# user = {'username': 'Jose', 'access': 'guest'}
#
#
# def make_secure(func):
#     @functools.wraps(func)  # con esto mantenemos la edintidad de la funcion que vamos a decorar y su funcionalidad
#     def secure(*args, **kwargs):  # cuando reemplazemos la funcion, podra tomar argumentos originales
#         if user['access'] == 'admin':
#             return func(*args, **kwargs)
#         else:
#             print(f'{user["username"]} has no permissions to access here')
#
#     return secure
#
#
# @make_secure
# def get_pass(panel):
#     if panel == 'admin':
#         return '1234'
#     elif panel == 'billing':
#         return 'super_secure_password'
#
#
# print(get_pass('billing'))

# import functools
#
# user = {'username': 'Jose', 'access': 'guest'}
#
#
# def make_secure(access_level):
#     def decorator(func):
#         @functools.wraps(func)  # con esto mantenemos la edintidad de la funcion que vamos a decorar y su funcionalidad
#         def secure(*args, **kwargs):  # cuando reemplazemos la funcion, podra tomar argumentos originales
#             if user['access'] == access_level:
#                 return func(*args, **kwargs)
#             else:
#                 return f'{user["username"]} has no {access_level} permissions to access here'
#
#         return secure
#     return decorator
#
#
# @make_secure('admin')
# def get_pass_admin():
#     return 'admin: 1234'
#
# @make_secure('user')
# def get_pass_dashboard():
#     return 'admin: 1234'
#
#
# print(get_pass_admin())
# print(get_pass_dashboard())
#
# user = {'username': 'Anna', 'access': 'admin'}
#
# print(get_pass_admin())
# print(get_pass_dashboard())

#           MUTABILITY

# a = []
# print(id(a))
# a += (15,)
# print(a)
# print(id(a))

# unmutable = tuple, strings, booleans, floats, int

# a = 'hello'
# b = a
# print(a)
# print(b)
# a += ' world'
#
# print(a)

#               MUTABLE PARAMETERS

# class Student:
#     def __init__(self, name, grades = ()):
#         self.name = name
#         self.grades = grades
#
#     def take_exam(self, result: int):
#         self.grades = self.grades + (result,)
# #        self.grades.append(result)
#
# bob = Student('bob')
# rob = Student('rob')
#
# bob.take_exam(90)
# rob.take_exam(50)
# bob.take_exam(30)
# rob.take_exam(40)
#
# print(bob.grades)
# print(rob.grades)


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student('bob')
rob = Student('rob')

bob.take_exam(90)
rob.take_exam(50)
bob.take_exam(30)
rob.take_exam(40)

print(bob.grades)
print(rob.grades)
