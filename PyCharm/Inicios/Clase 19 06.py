

"""
19 julio
empezamos en el 2.11 y terminamos en el 
"""
"""
friends= ["Rolf", "ruth", "charlie","Jen"]
guest = ["jose", "Bob","Rolf","Charlie","michael"]

friends_title = [f.title() for f in friends]
#guest_lower = [g.title() for g in guest]

invitados = [g for g in guest if g.title() in friends_title]
print(invitados)

"""
"""

friends= ["Rolf", "ruth", "charlie","Jen"]
guest = ["jose", "Bob","Rolf","Charlie","michael"]

friends_title = set([f.title() for f in friends])
guest_title = set([g.title() for g in guest])

print(friends_title.intersection(guest_title))

"""

"""zip"""

"""
friends = ["carlos","klaus","renata","jorge"]
numbers = [45,87,69,21,54,65,32,77]
colors = ["amarillo","rojo", "azul", "verde", "cafe", "morado"]

test = list(zip(friends, numbers, colors))
print(test)
"""
""" prbando funcion sep y join """
"""
test2 = [1,2,3,4,5,6,7,8]
# print(test2, sep=" - ") # estas solucion no funciona
print(" - ".join(map(str,test2)))
"""

