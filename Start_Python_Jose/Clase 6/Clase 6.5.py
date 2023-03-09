import json

with open('friends_json.txt', 'w') as file:
    file_content = json.load(file) # read file and turns it to dictionary

cars = [
    {'make': 'Ford', 'Model': 'Fiesta'},
    {'make': 'Ford', 'Model': 'Focus'}
        ]

with open('friends_json.txt', 'w') as outfile:
    json.dump(cars, outfile, indent=4) # indent=4 sirve para indentar, genial!

json_string = '[{"name": "Alfa Romeo", "released": "1958"}]'

incorrect_car = json.loads(json_string) # revisar
print(incorrect_car[0]['name'])

