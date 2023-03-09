juguetes = {
    'Cartas': (50, 2000),
    'Dibujanary': (320, 10000),
    'Duopoly': (250, 12500),
    'Ajedrez': (400, 4000),
    'Naipe': (75, 1000),
    'Guerra': (450, 8700)}

precio_peso = 100/50


def linda():
    total = []
    for x, y in juguetes.items():
        user = int(input(f'Ingrese la cantidad de {x} a comprar: '))
        if x in x:
            total.append((y[0]*user)+(y[1]*user))
    print(f'El total de su compra es: $ {sum(total):,.2f}')


linda()


"""def compra():
    user1 = int(input('Ingrese la cantidad de Cartas Dos comprados: '))
    if user1 >0:
        us1 = user1*((50*precio_peso) + (2000))
    else:
        us1 = 0
    user2 = int(input('Ingrese la cantidad de Dibujanary comprados: '))
    if user2 > 0:
        us2 = user2 * ((320 * precio_peso) + (10000))
    else:
        us2 = 0
    user3 = int(input('Ingrese la cantidad de Duopoly comprados: '))
    if user3 > 0:
        us3 = user3 * ((250 * precio_peso) + (12500))
    else:
        us3 = 0
    user4 = int(input('Ingrese la cantidad de Ajedrez comprados: '))
    if user4 > 0:
        us4 = user4 * ((400 * precio_peso) + (4000))
    else:
        us4 = 0
    user5 = int(input('Ingrese la cantidad de Naipe Español comprados: '))
    if user5 > 0:
        us5 = user5 * ((75 * precio_peso) + (1000))
    else:
        us5 = 0
    user6 = int(input('Ingrese la cantidad de Guerra Mundial comprados: '))
    if user6 > 0:
        us6 = user6 * ((450 * precio_peso) + (8700))
    else:
        us6 = 0
        
    print(us1 + us2 + us3 + us4 + us5 + us6)

compra()"""
