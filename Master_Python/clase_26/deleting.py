import sqlite3
connection = sqlite3.connect('my_database1.db')
cursor = connection.cursor()

department = input('Enter department: ')
sql = 'DELETE FROM employees WHERE department=?'
cursor.execute(sql, (department,))

connection.commit()
connection.close()