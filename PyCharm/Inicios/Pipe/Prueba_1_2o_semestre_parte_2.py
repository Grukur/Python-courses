combustible = {'a': .25, 'b': .15, 'c': .05}

valor = float(input('Por favor ingrese valor automovil: '))
fuel = input("""eliga su combustible por favor: 
a - Fosil
b - Mixto
c - Electrico
 """)
for x, y in combustible.items():
    if fuel in x:
        print(f'El precio final es de $ {valor + (valor * y):,.2f} ')
