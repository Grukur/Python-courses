

"""def starts_with_r(friends):
    return friends.startswith('R')

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(starts_with_r, friends)

# print(next(start_with_r)) # con esta funcion, comprobamos que filtro contiene yield

for i in start_with_r: # filter es un filtro que funciona como yield, con esta funcion forzamos a drnos todo
    print(i)"""

# una forma mas corta seria agregando un lambda

"""friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)
for i in start_with_r: # filter es un filtro que funciona como yield, con esta funcion forzamos a drnos todo
    print(i)

other_way = (f for f in friends if f.startswith('R')) # es otra forma de hacer lo mismo  que con lambda
print(next(other_way))"""

# veremos Map y sus equivalentes
"""friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']

friends_lowwer = map(lambda x: x.lower(), friends) # es generico, para otros programers
friends_lowwer2 = [friend.lower() for friend in friends] # cuando quieres obtener una lista
friends_lowwer3 = (friend.lower() for friend in friends) # normal

print(next(friends_lowwer))
print(friends_lowwer2)
print(next(friends_lowwer3))"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users_l = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'dad', 'password': '147'}
]

users = [User.from_dict(x) for x in users_l]
for i in users:
    print(i)

users_2 = map(User.from_dict, users)
print(users_2)

# todo esto devuelve falso =
# 0 or 0.0
# None
# [] {} ()
# False

# any se usa para ver si existe a lo menos 1 verdadero, mientras que all, es para ver si todos son verdaderos



