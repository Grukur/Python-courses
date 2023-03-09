
constante = -7.547078
e = 2.71828

factor_co_morbilidad = \
    {
     "Hipertenso": 2.003496,
     "Diabetes": 2.21035,
     "Cardiaca": 2.550317,
     "Respiratoria": 2.036501,
     "Cáncer": 1.925291
    }

factor_edad = {
    range(0, 19): 0,
    range(20, 29): -1.458102,
    range(30, 39): -1.196494,
    range(40, 49): -0.9109254,
    range(50, 59): 1.888158,
    range(60, 69): 2.93897,
    range(70, 79): 3.774616,
    range(80, 99): 4.456995,
}


def edad():
    edad_user = int(input('Favor ingrese su edad: '))
    for x, y in factor_edad.items():
        if edad_user in x:
            return float(y)


def sexo():
    user2 = input('Favor ingrese H si es Hombre o M si es Mujer: ').upper()
    if user2 == 'H':
        return 0.6176118
    else:
        return 0


def enfermedaduser1():
    comorbilidad = []
    for x, y in factor_co_morbilidad.items():
        resp = input(f'Responda S para si y N para no si, padece {x}: ').upper()
        if resp == 'S':
            comorbilidad.append(float(y))
    return sum(comorbilidad)


print('Por favor responda las siguientes preguntas, no se preocupe si usa mayusculas o no')
riesgo = (constante + edad() + sexo() + enfermedaduser1())
riesgo_total = ((e**riesgo) / (1 + e**riesgo))*100
print(f'Su probabilidad de morir por COVID-19, si se contagias, es de: {riesgo_total:.5f} %')
