
"""read_1 = open('csv.txt', 'r')
content_read = read_1.read().title().splitlines()
read_1.close()

content_read = [x.replace(',', ' ') for x in content_read]

print(*content_read, sep='\n')"""

# esta forma es sin list comprehension, solo usando loop y creando nueva lista para guardar los datos nuevos
# la forma con list comprehension es mucho mas elegante y rapida

"""new_content = []

for coma in content_read:
    no_coma = coma.replace(",", " ")
    new_content.append(no_coma)

print(*new_content, sep='\n')"""

# codigo de Jose, increible
#

read_1 = open('csv.txt', 'r')
lines = read_1.readlines()
read_1.close()

lines = [line.strip() for line in lines[1:]] # crea list comprehension y una slice para no mostrar los headers

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age} old, studyng {degree} at {university}.')

