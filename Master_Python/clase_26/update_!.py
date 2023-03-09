import sqlite3
connection = sqlite3.connect('my_database1.db')
cursor = connection.cursor()

# sql = 'UPDATE employees SET phone="123123" WHERE id=2' # esta linea le cambia el phone a id 2
# cursor.execute(sql)

# sql = 'UPDATE employees SET department="IT"' # esta linea cambia a IT a todos
# cursor.execute(sql)

id = input('Enter the ID: ')
sql = 'UPDATE employees SET department="IT" WHERE id=?' # esta linea cambia a IT a todos
cursor.execute(sql, (id,)) # cuando es un valor que ingresa el usuario, hay que colocar un tuple

connection.commit()
connection.close()