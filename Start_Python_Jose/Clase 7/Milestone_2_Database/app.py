from Utils import database

USER_CHOICE = """
a - To add a new book.
l - To list all books.
r - To mark a book as read.
d - To delete a book.
q - To quit.

Your choice: """

READ_MENU = """
Please select how you need to find your book:

n - By name of the book.
q - To quit.

:  
"""

def menu():
    user = input(USER_CHOICE)
    while user != 'q':
        if user == "a":
            promt_add_book()
        elif user == "l":
            list_book()
        elif user == "r":
            promt_read_book()
        elif user == "d":
            delete_book()
        break

# def promt_add_book()      ask for book name and author
# def list_book()           show all the boks in our list
# def promt_read_book()     ask for book name and change it to "read" in our list
# def promt_delete_book()   ask for book name and remov from list

def promt_add_book():
    name = input('Pleas tell me the name of the book: ')
    author = input('Please tell me the name of author')

    database.add_book(name, author)
    return menu()

def list_book():
    print(database.books)
    return menu()

def promt_read_book():
    user_r = input(READ_MENU)
    while user_r != 'q':
        if user_r == 'n':
            name_r = input('Pleas tell me the name of the book: ')
            for i in database.books:
                if i['name'] == name_r: #por que no necesita 2 for, si la key esta en un diccionario dentro de una lista
                    i['read'] = True
                    print(i, 'se ha actualizado la biblioteca!')
        return menu()

def delete_book():
    user_r = input(READ_MENU)
    while user_r != 'q':
        if user_r == 'n':
            name_r = input('Pleas tell me the name of the book to delete: ')
            for i in database.books:
                if i['name'] == name_r:  # por que no necesita 2 for, si la key esta en un diccionario dentro de una lista
                    database.books.remove(i)
                    print(database.books, 'estos son los libros que hay en biblioteca')
        return  menu()


menu()
print(__name__)
