
numero = int(input('favor ingrese un numero entero a su eleccion: '))

for x in range(2, numero+1):
    list1 = [str(i) for i in range(1, x+1) if x % i == 0]
    if len(list1) <= 2:
        print(f'{x} {" ".join(list1)} es primo')
    else:
        print(f'{x} {" ".join(list1)}')
