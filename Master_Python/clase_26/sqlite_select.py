import sqlite3
connection = sqlite3.connect('my_database1.db')

cursor = connection.cursor()
# sql = 'select name, phone from employees' # aqui podemos ordenar que quremos, * es para obtener toda la data
# sql = 'select * from employees where name like "A%"' # muestra solo las row que nombre empieza con A
# sql = 'select * from employees where name like "A%" order by if desc' # se ordena por descending

# id = input('Enter an ID: ')
# sql = 'SELECT * FROM employees WHERE id=?' # ? se deja abierto para que usuario defina (tambien se puede cambiar = por >, etc)
record = (10, 'Leonardo Amaro', 'Marketing', '+411111', 'leos@gmail.com')
sql = 'INSERT INTO employees VALUES(?,?,?,?,?)'


# cursor.execute(sql,(id,)) # se deja como tuple
cursor.execute(sql, record) # se deja como tuple
sql = 'SELECT * FROM employees'

cursor.execute(sql)

for row in cursor.fetchall(): # fetchall se puede ignorar en esta situacion
    print(row)

# row = cursor.fetchone() # solo muestra solo 1
# print(row)

connection.close()