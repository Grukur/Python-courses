from Utils_SQLite import database_sqlite

USER_CHOICE = """
a - To add a new book.
l - To list all books.
r - To mark a book as read.
d - To delete a book.
q - To quit.

Your choice: """


def menu():
    database_sqlite.create_book_table()
    user = input(USER_CHOICE)
    while user != 'q':
        if user == "a":
            promt_add_book()
        elif user == "l":
            list_books()
        elif user == "r":
            promt_read_book()
        elif user == "d":
            delete_book()
        else:
            print('wrong choice')
        break

# def promt_add_book()      ask for book name and author
# def list_book()           show all the boks in our list
# def promt_read_book()     ask for book name and change it to "read" in our list
# def promt_delete_book()   ask for book name and remov from list


def promt_add_book():
    name = input('Pleas tell me the name of the book: ')
    author = input('Please tell me the name of author: ')

    database_sqlite.add_book(name, author)
    return menu()


def list_books():
    books = database_sqlite.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")
    return menu()


def promt_read_book():
    user_r = input('Enter the name of the book you just finish: ')

    database_sqlite.mark_books_as_read(user_r)
    return menu()


def delete_book():
    name = input('Enter the name of the book you want to delete: ')

    database_sqlite.delete_book(name)
    return menu()


menu()
