from .database_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name, author):
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name, author))
#    cursor.execute(f'INSERT INTO books VALUES("{name}", "{author}", 0)') esto es suseptible a un atake {author} puede ser cambiado por una linea de atake


def get_all_books():
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def mark_books_as_read(name):
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))


def delete_book(name):
    with DatabaseConnection('data.db') as cursor:

        cursor.execute('DELETE FROM books WHERE name = ?', (name,))



