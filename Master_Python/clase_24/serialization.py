import pickle
import json

friends1 = {'Anna': [35, 'Bucharest', 486128753], 'Rob': [25, 'London', 486128753], 'Raul': [45, 'Santiago', 486128753]}
friends2 = {'Sam': [35, 'Paris', 486128753], 'Elie': [25, 'Moscu', 486128753], 'Bryan': [45, 'Chicago', 486128753]}
friends = (friends1, friends2)
#
# with open('friends.dat', 'wb') as f:
#     pickle.dump(friends, f)
#
# with open('friends.dat', 'rb') as f:
#     obj = pickle.load(f)
#     print(obj)

with open('friends.json', 'w') as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)
