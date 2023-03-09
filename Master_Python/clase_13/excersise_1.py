
with open('devices.txt', 'r+') as file:
    list1 = [r.strip('\n').split(':') for r in file]

print(list1)

