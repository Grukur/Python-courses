

"""def multi():
    origen = []
    for number in range(100):
        origen.append(number)
"""

"""    print(number)
def multi():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(number, 'its a freaking Fiz&Buz!!!')
        elif number % 3 == 0:
            print(number, 'its a Fiz!')
        elif number % 5 == 0:
            print(number, 'its a buz!')
        else:
            print(number)

multi()"""

"""def multi():
    origen = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            origen.append('its a freaking Fiz&Buz!!!')
            #print(number, 'its a freaking Fiz&Buz!!!')
        elif number % 3 == 0:
            origen.append('its a Fiz!')
            #print(number, 'its a Fiz!')
        elif number % 5 == 0:

            origen.append('its a buz!')
            #print(number, 'its a buz!')
        else:
            origen.append(number)
            #print(number)
    print(*origen, sep=' \n')

multi()"""

"""def multi():
    origen = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            val1 = str(number) + ' its a freaking Fiz&Buz!!!'
            origen.append(val1)
        elif number % 3 == 0:
            val2 = str(number) + ' its a freaking Fiz!'
            origen.append(val2)
        elif number % 5 == 0:
            val3 = str(number) + ' its a freaking Buz!'
            origen.append(val3)
        else:
            origen.append(number)
    print(*origen, sep=' \n')

multi()"""

#una oracion de str tiene que imprimirse al reves

"""origen = input("dame una oracion de 3 palabras o mas: ") #[::-1] inversor de contenido
final = origen.split()[::-1] #gracias al split, puedo reverse por palabra
print(*final, sep=' ')"""

"""origen = input("dame una oracion de 3 palabras o mas: ") #[::-1] inversor de contenido
final = origen.split()
final.reverse() #aqui damos vuelta todo con un reverse, funciona con variables, listas, todo
print(*final, sep=' ')"""

#tengo un array con x cantidad de elementos y quiero desplazarlos hacia la isquierda x cantidad de espacios

#list = [15, 25, 35, 45, 55, 65, 75, 85]
#print(list)
#list2 = []
#x = int(input("""cuanto deseas desplazar el contenido de la lista y hacia donde?
#            si es hacia la derecha, introduce un valor negativo
#            si es hacia la isquieda, introduce un valor positivo: """))
#for i in range(len(list)):
#    list2.append(list[(i + x) % len(list)])

#print(list2)


#tengo 2 strings, verificar si son isomorficos = es posible hacer un mapeo entre esos strings, aab = xxy

"""list_1 = 'aab'
list_2 = 'xxy'

if len(list_1) == len(list_2):
    dict_1 = {}
    for i in range(len(list_1)):
        if list_1[i] in dict_1:
            if dict_1[list_1[i]] == list_2[i]:
                continue
            elif list_2[i] != dict_1.get(i):
                dict_1 = {list_1[i]: list_2[i]}
        elif list_2[i] not in dict_1:
            dict_1 = {list_1[i]: list_2[i]}
    print('exito, las listas',list_1, 'y', list_2, 'si son isomorficas')"""













