alumnos = input('Favor ingrese cantidad de alumnos en curso: ')
nota_percapita = input('Favor ingrese cantidad de notas por alumno: ')
aprob = 0
repro = 0
promedios = []

for x in range(int(alumnos)):
    lista = dict([(f'alumno {x + 1}', [])])
    for y in range(int(nota_percapita)):
        notas_alumno = float(input(f'dame la nota numero {y + 1} del alumno {x + 1}: '))
        lista[f'alumno {x + 1}'].append(notas_alumno)
    if sum(lista[f'alumno {x + 1}'])/int(nota_percapita) > 3.94:
        print(f'El alumno {x + 1} APROBO con promedio: ', sum(lista[f'alumno {x + 1}'])/int(nota_percapita), '\n')
        aprob += 1
    else:
        print(f'El alumno {x + 1} REPROBO con promedio: ', sum(lista[f'alumno {x + 1}']) / int(nota_percapita), '\n')
        repro += 1
    promedios.append(sum(lista[f'alumno {x + 1}'])/int(nota_percapita))

print(f"""Aprobaron {aprob} y Reprobaron {repro} de {int(aprob+repro)} alumnos.
Con promedio curso de {sum(promedios)/int(aprob+repro)}""")
