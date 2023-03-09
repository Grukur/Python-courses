
def FirstGenerator_Yield():
    i = 0
    while i < 100:
        yield i # este es un generador, entrega un numero por cada llamado
        i += 1

g = FirstGenerator_Yield()
print(next(g)) # esto hace un llamado = un numero
print(list(g)) # esto manda a pedir todos los numeros


class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self): # esto es lo mismo que class FirstHundredIterable y ahora es iterable
        return self


my_gen = FirstHundredGenerator()

#print(sum(my_gen))
print(sum(FirstHundredGenerator()))

for i in my_gen:
    print(i)

"""
for i in range(101):
    print(next(my_gen))
"""

"""    
class FirstHundredIterable: # esto convierte en iterable
    def __iter__(self):
        return FirstHundredGenerator()
"""

class AnotherIterable:
    def __init__(self):
        self.cars = ['fiesta', 'focus', 'explorer']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

my_numbers = [x for x in [ 1,2,3,4,5]] # list comprehension definida
my_numbers_gen = (x for x in [1,2,3,4,5]) # esto es un Generator comprehension

print(next(my_numbers_gen))


