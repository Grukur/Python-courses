
# Intro to Files

my_file = open('class 6.1.txt', 'r') #'r' es para lectura solamente, no es necesario
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Give me your name user: ')
my_file = open('class 6.1.txt', 'w') # 'w' es para reescribir el archivo, ojo se bora todo
my_file.write(user_name)
