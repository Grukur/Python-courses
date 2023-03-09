############# como usar el unpackig de otras formas ################

"""def add_all(a1, a2, a3, a4):
    return a1+a2+a3+a4

print(add_all(1,2,3,4))"""

############# opcion 2 ################

"""def add_all(a1, a2, a3, a4):
    return a1+a2+a3+a4

val = (1,2,3,4)
print(add_all(*val))"""

############# opcion 3 ################

"""def add_all(a1, a2, a3, a4):
    return a1+a2+a3+a4

val = {'a1': 1, 'a2': 2, 'a3': 3, 'a4': 4}

print(add_all(**val))"""

############# opcion 4 para multi argumentos en la funcion ################

"""def add_all(*args):
    return sum(args)

val = (1, 2, 3, 4)

print(add_all(*val))"""

############# opcion 5 para multi arg y acepte palabras ################

def add_all(*args): # *args acepta cualquier numero de argumentos numericos
    return sum(args)

val = (1, 2, 3, 4)

def pretty_print(**kwargs): # *kwargs acepta cualquier numero de argumentos str
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')

print(add_all(*val))
pretty_print(**{'username':'jose123', 'acces_level': 'admin'})
print('\n')
pretty_print(username = 'jose2525', access_level = 'admin')


