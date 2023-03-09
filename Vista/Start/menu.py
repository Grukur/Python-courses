import math
'''
Un programa para determinar cuando un objeto desaparece de la vista humana en el espacio:

a- a que distancia desaparece segun su tamaño
b- cuanto demora en desaparecer segun la velocidad que se mueve y su tamaño
c- a que velocidad se mueve segun su tamaño y tiempo de perdida

Resolucion angular minima humana = 0.025 grados
'''



def menu():
    user = input('por favor selecciona que deseas hacer:\n'
                      'a- A que distancia desparece x objeto según su tamaño\n'
                      'b- Cuanto tiempo demora en desaparecer x objeto según velocidad '
                      'y tamaño\n'
                      'c- A que velocidad viaja x objeto según su tamaño y tiempo que '
                      'le lleva desaparecer\n'
                       'q- Si desea salir\n')

    if user in ('q', 'Q'):
        quit('Gracias por jugar, adios :D')
    elif user == 'a':
        outdistance(calculo())
    elif user == 'b':
        outtime(calculo())
    elif user == 'c':
        outspeed(calculo())
    else:
        print('por favor ingresa una de las opciones validas (a, b, c o q), gracias')
        menu()

def calculo():
    size = input('por favor ingrese la altura del objeto en metros para continuar o presione Q para volver al Menu: \n')
    if size in ('q', 'Q'):
        menu()
    try:
        size = float(size)
    except ValueError:
        return print('Ha ingresado letras, por favor ingresa numeros enteros o decimales usando . ', end='\n' * 2)


    minop = math.radians(0.025)
    agudo = math.radians(89.975)
    distancia = (size * math.sin(agudo)) / (math.sin(minop))
    return distancia

def outdistance(dis):
    # dis = calculo()

    try:
        if dis >= 1000:
            print(f'Dejaras de ver tu objeto a los {dis / 1000:,.2f} kilometros de distancia\n')
            menu()

        elif dis < 1000:
            print(f'Dejaras de ver tu objeto a los {dis:,.2f} metros de distancia\n')
            menu()
    except TypeError:
        outdistance(calculo())


def outtime(dis):
    # dis = calculo()

    try:
        dis = int(dis)
    except TypeError:
        outtime(calculo())

    user2 = (input('por favor ingrese la velocidad de escape en km/h: \n'))
    try:
        user2 = float(user2)
    except ValueError:
        print('Ha ingresado letras, por favor ingrese numeros o deciamles usando .')
        outtime(calculo())

    tiempo = dis / (user2 * 1000) * 60

    if tiempo >= 1:
        print(f'El objeto desaparecera en {tiempo:,.2f} minutos y estará a {dis:,.2f} metros\n')
    elif tiempo < 1:
        tiempo = tiempo * 60
        print(f'El objeto desaparecera en {tiempo:,.2f} segundos y estará a {dis:,.2f} metros\n')
    menu()


def outspeed(dis):
    # dis = calculo()
    try:
        dis = int(dis)
    except TypeError:
        outspeed(calculo())
    user3 = (input('por favor ingrese el tiempo que demora en desaparecer: \n'))
    try:
        user3 = float(user3)
    except ValueError:
        print('Ha ingresado letras, por favor ingrese numeros o deciamles usando .')
        outspeed(calculo())

    user4 = input('Ingreso (a, b o c): \n'
                  'a- horas\n'
                  'b- minutos\n'
                  'c- segundos\n')

    vel = ((dis / user3) * 60) / 1000

    if user4 == 'a':
        vel = vel / 60
        print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
        menu()
    elif user4 == 'b':
        print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
        menu()
    elif user4 == 'c':
        vel = vel * 60
        print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
        menu()
    else:
        print('por favor ingresa una de las opciones validas (a, b o c), gracias')
        outspeed(calculo())

menu()

