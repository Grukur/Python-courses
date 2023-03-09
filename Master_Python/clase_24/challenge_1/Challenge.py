# import requests, json
#
# r = requests.get('http://jsonplaceholder.typicode.com/todos')
#
# with open('api_1.json', 'w') as f:
#     f.write(r.text)
#
# with open('api_1.json', 'r') as f2:
#     l1 = json.load(f2)
#
# final = [x for x in l1 if x['completed'] == True]
#
# with open('api_2.json', 'w') as f:
#     json.dump(final, f, indent=2)

# import requests, json
#
# r = requests.get('http://jsonplaceholder.typicode.com/todos')
#
# l1 = json.loads(r.text)
# final = [x for x in l1 if x['completed'] == True]
#
# with open('api_2.json', 'w') as f:
#     json.dump(final, f, indent=2)


# friends1 = {'Anna': [35, 'Bucharest', 486128753], 'Rob': [25, 'London', 486128753], 'Raul': [45, 'Santiago', 486128753]}
# friends2 = {'Sam': [35, 'Paris', 486128753], 'Elie': [25, 'Moscu', 486128753], 'Bryan': [45, 'Chicago', 486128753]}
# friends = (friends1, friends2)
#
#
# def serialize(data, file, protocol):
#     if protocol == 'json':
#         import json
#         with open(file, 'w') as f:
#             json.dump(data, f, indent=2)
#     elif protocol == 'pickle':
#         import pickle
#         with open(file, 'wb') as f:
#             pickle.dump(data, f)
#
#
# serialize(friends, 'chall_1.json', 'json')
# print('#' * 150)
#
# def deserialize(file, protocol):
#     if protocol == 'json':
#         import json
#         with open(f'{file}', 'r') as f:
#             js = json.load(f)
#             print(js)
#     elif protocol == 'pickle':
#         import pickle
#         with open(f'{file}', 'rb+') as f:
#             ps = pickle.load(f)
#             print(ps)
#
#
# deserialize('chall_1.json', 'json')

import requests, json, csv

r = requests.get('https://jsonplaceholder.typicode.com/users')

l1 = json.loads(r.text)

with open('company_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for x in l1:
        name = (x['name'])
        city = (x['address']['city'])
        geo = ((x['address']['geo']['lat'], x['address']['geo']['lng']))
        company = (x['company']['name'])

        writer.writerow((name, city, geo, company))








