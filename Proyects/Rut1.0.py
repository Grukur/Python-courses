
def rut():

    name = input('please give me you name: \n')
    ru = input('give me you rut without VD (last digit): \n')
    seri = '23456723'

    ruf = 11 - sum([int(x) * int(y) for x, y in zip(reversed(ru), seri)]) % 11

    if ruf == 11:
        ruf = 0
    if ruf == 10:
        ruf = 'k'

    print(f'{name} you Rut is: {ru}-{ruf}, thanks for participate!')


rut()

