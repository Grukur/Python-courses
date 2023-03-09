import sqlite3

# connection = sqlite3.connect('my_database1.db')
#
# cursor = connection.cursor()
# sql = '''
#     CREATE TABLE IF NOT EXISTS employees(
#     id INTEGER,
#     name VARCHAR(64),
#     department VARCHAR(32),
#     phone VARCHAR(16),
#     email VARCHAR(32)
#     );
#     '''
#
# cursor.execute(sql)
# connection.commit()
#
# connection.close()

# connection = sqlite3.connect('my_database1.db')
# cursor = connection.cursor()
#
# sql = '''
#     INSERT INTO employees(id, name, department, phone, email) VALUES (1, "john Smith", "IT", "+55555", "jfd@gmail.com");
#     INSERT INTO employees VALUES(2, "Anne Barker", "Accounting", "+447545", "aan@gmail.com");
#     INSERT INTO employees VALUES(3, "Enne Barker", "Sales", "+447545", "Ennan@gmail.com");
# '''
#
# cursor.executescript(sql) ## este metodo es plural, permite ingresar mas de un sql statments
# ## cursor.execute(sql) # este modo solo ingresa un sql
#
# connection.commit()
# connection.close()







