'''
def Rana():
    print('Problema logico de la rana, a continuacion se haran 3 preguntas, favor contestar:\n')
    user1 = input('la rana comienza: \na- dia \nb- noche: \n')
    print(user1)
    if user1 not in ('a', 'b'):
        print('invalid choise')
        return
    user2 = input('Cuanto metros tiene el pozo?: \n')
    if int(user2) < 1:
        print('Pozo debe tener mas de 1 metro')
        return
    user3 = input('Cuantos metros avanza la rana de día?: \n')
    if int(user3) > int(user2):
        print('El pozo es muy pequeño parece')
        return
    user4 = input('Cuantos metros retrocede la rana de noche?: \n')
    if int(user4) > int(user3):
        print('es mejor que esta rena siempre retroceda')
        return
    n = 0
    if user1 == 'a':
        while int(user2) > 0:
            n = n + 1
            user2 = int(user2) - int(user3)
            if user2 > 0:
                user2 = int(user2) + int(user4)
    if user1 == 'b':
        while int(user2) > 0:
            n = n + 1
            user2 = int(user2) + int(user4)
            if user2 > 0:
                user2 = int(user2) - int(user3)

    print(n)

Rana()
'''

'''
def facto():
    user = int(input('por favor dame un numero para calcular el factorial: \n'))
    fact = user
    while user > 1:
        fact = (fact * (user - 1))
        user = user - 1
    print(fact)

facto()
'''



