
menu = {
    "1": 254,
    "2": 293,
    "3": 127,
    "4": 336,
    "5": 132,
    "6": 370,
    "7": 267,
    "8": 144,
    "9": 26
}


def user_menu():
    user_kal = int(input('Favor digame cuantas calorias va a consumir hoy (ejemplo 500): '))
    user = input("""Favor elige el plato que deseas comer hoy: 
    1 - Carne mechada 
    2 - Empanada de carne 
    3 - Ensalada César 
    4 - Guiso de lentejas 
    5 - Lasaña 
    6 - Macarrones 
    7 - Pizza 
    8 - Pollo asado 
    9 - Tortilla de papas 
    : """)
    for x, y in menu.items():
        if user in x:
            total = (user_kal/y)*100
            print(f'{total:.2f} gramos')


user_menu()
