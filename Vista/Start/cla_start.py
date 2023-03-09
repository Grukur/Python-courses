import math

class Vistas:
    def __init__(self):
        return

    @classmethod
    def menu(cls):
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
            Vistas.outdistance()
        elif user == 'b':
            Vistas.outtime()
        elif user == 'c':
            Vistas.outspeed()
        else:
            print('por favor ingresa una de las opciones validas (a, b, c o q), gracias')
            Vistas.menu()

    @classmethod
    def calculo(cls):
        size = input(
            'por favor ingrese la altura del objeto en metros para continuar o presione Q para volver al Menu: \n')
        if size in ('q', 'Q'):
            Vistas.menu()
        try:
            size = float(size)
        except ValueError:
            return print('Ha ingresado letras, por favor ingresa numeros enteros o decimales usando . ', end='\n' * 2)

        minop = math.radians(0.025)
        agudo = math.radians(89.975)
        distancia = (size * math.sin(agudo)) / (math.sin(minop))
        return distancia

    @classmethod
    def outdistance(cls):
        dis = Vistas.calculo()

        try:
            if dis >= 1000:
                print(f'Dejaras de ver tu objeto a los {dis / 1000:,.2f} kilometros de distancia\n')
                Vistas.menu()

            elif dis < 1000:
                print(f'Dejaras de ver tu objeto a los {dis:,.2f} metros de distancia\n')
                Vistas.menu()
        except TypeError:
            Vistas.outdistance()

    @classmethod
    def outtime(cls):
        dis = Vistas.calculo()

        try:
            dis = int(dis)
        except TypeError:
            Vistas.outtime()

        user2 = (input('por favor ingrese la velocidad de escape en km/h: \n'))
        try:
            user2 = float(user2)
        except ValueError:
            print('Ha ingresado letras, por favor ingrese numeros o deciamles usando .')
            Vistas.outtime()

        tiempo = dis / (user2 * 1000) * 60

        if tiempo >= 1:
            print(f'El objeto desaparecera en {tiempo:,.2f} minutos y estará a {dis:,.2f} metros\n')
        elif tiempo < 1:
            tiempo = tiempo * 60
            print(f'El objeto desaparecera en {tiempo:,.2f} segundos y estará a {dis:,.2f} metros\n')
        Vistas.menu()

    @classmethod
    def outspeed(cls):
        dis = Vistas.calculo()
        try:
            dis = int(dis)
        except TypeError:
            Vistas.outspeed()
        user3 = (input('por favor ingrese el tiempo que demora en desaparecer: \n'))
        try:
            user3 = float(user3)
        except ValueError:
            print('Ha ingresado letras, por favor ingrese numeros o deciamles usando .')
            Vistas.outspeed()

        user4 = input('Ingreso (a, b o c): \n'
                      'a- horas\n'
                      'b- minutos\n'
                      'c- segundos\n')

        vel = ((dis / user3) * 60) / 1000

        if user4 == 'a':
            vel = vel / 60
            print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
            Vistas.menu()
        elif user4 == 'b':
            print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
            Vistas.menu()
        elif user4 == 'c':
            vel = vel * 60
            print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
            Vistas.menu()
        else:
            print('por favor ingresa una de las opciones validas (a, b o c), gracias')
            Vistas.outspeed()

Vistas.menu()

