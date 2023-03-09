"""
user = input('Favor ingresa tres nombres de amigos: ').title().split()

my_file = open('amigos.txt', 'r')
amigos_2 = my_file.read().splitlines()
my_file.close()

amigos_3 = []
for i in amigos_2:
    for x in user:
        if x == i:
            amigos_3.append(x)
        else:
            continue

my_file_2 = open('amigos cercanos.txt', 'w')
for i in amigos_3:
    my_file_2.write("{0}\n".format(i))
my_file_2.close()

my_file_2 = open('amigos cercanos.txt', 'r')
file_2 = my_file_2.read()
my_file_2.close()
print(file_2)"""

# lo mismo pero con sets

user = input('Favor ingresa tres nombres de amigos: ').title().split()

my_file = open('Amigos.txt', 'r')
amigos_2 = my_file.read().splitlines()
my_file.close()

set_1 = set(user)
set_2 = set(amigos_2)
amigos_3 = set_1.intersection(set_2)

my_file_2 = open('Amigos cercanos.txt', 'w')
for i in amigos_3:
    my_file_2.write("{0}\n".format(i))
my_file_2.close()

my_file_2 = open('Amigos cercanos.txt', 'r')
file_2 = my_file_2.read()
my_file_2.close()
print(file_2)
