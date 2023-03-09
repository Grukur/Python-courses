import math
'''
Un programa para determinar cuando un objeto desaparece de la vista humana en el espacio:

a- a que distancia desaparece segun su tamaño
b- cuanto demora en desaparecer segun la velocidad que se mueve y su tamaño
c- a que velocidad se mueve segun su tamaño y tiempo de perdida

Resolucion angular minima humana = 0.025 grados
'''


def vista():
    size = input('por favor presione Q para salir o ingrese la altura del objeto en metros para continuar: \n')
    if size in ('q', 'Q'):
        quit('Gracias por jugar, adios :D')
    else:
        size = float(size)
        user1 = input('por favor selecciona que deseas hacer:\n'
                      'a- A que distancia desparece x objeto según su tamaño\n'
                      'b- Cuanto tiempo demora en desaparecer x objeto según velocidad '
                      'y tamaño\n'
                      'c- A que velocidad viaja x objeto según su tamaño y tiempo que '
                      'le lleva desaparecer\n')
        minop = math.radians(0.025)
        agudo = math.radians(89.975)
        distancia = (size * math.sin(agudo)) / (math.sin(minop))

        if user1 == 'a':
            print(f'Dejaras de ver tu objeto a los {distancia:,.2f} metros de distancia\n')
            return vista()

        elif user1 == 'b':
            user2 = float(input('por favor ingrese la velocidad de escape en km/h: \n'))
            tiempo = distancia/(user2*1000)*60
            if tiempo >= 1:
                print(f'El objeto desaparecera en {tiempo:,.2f} minutos y estará a {distancia:,.2f} metros\n')
            elif tiempo < 1:
                tiempo = tiempo * 60
                print(f'El objeto desaparecera en {tiempo:,.2f} segundos y estará a {distancia:,.2f} metros\n')
            return vista()

        elif user1 == 'c':
            user3 = float(input('por favor ingrese el tiempo que demora en desaparecer en minutos:\n'))
            vel = ((distancia/user3)*60)/1000
            print(f'El objeto viaja a una velocidad de {vel:,.2f} Km/h\n')
            return vista()

        else:
            print('error de seleccion\n')
            return vista()


vista()
