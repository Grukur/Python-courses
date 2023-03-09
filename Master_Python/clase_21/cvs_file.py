import csv

# with open('airtravel.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     year_1958 = {}
#     for row in reader:
#         year_1958[row[0]] = row[1]
#
#     max_1958 = max(year_1958.values())
#
#     for k, v in year_1958.items():
#         if max_1958 == v:
#             print(f'Busiest Month in 1958:{k}, Flight:{v}')

# people = [
# ['Dan', 34, 'Bucharest'],
# ['Andrei',21, 'London'],
# ['Maria', 45, 'Paris']
# ]
#
# with open('people1.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     for x in people:
#         writer.writerow(x)

# people = [
# ['Dan', 34, 'Bucharest'],
# ['Andrei',21, 'London'],
# ['Maria', 45, 'Paris']
# ]
#
# csv.register_dialect('colon', delimiter=':', quoting=csv.QUOTE_NONE, lineterminator='\n')
#
# with open('people1.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, dialect='colon')
#     for x in people:
#         writer.writerow(x)

# people = [
# ['Dan', 34, 'Bucharest'],
# ['Andrei',21, 'London'],
# ['Maria', 45, 'Paris']
# ]
#
# with open('people1.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=':')
#     for x in people:
#         writer.writerow(x)
#
# with open('people1.csv', 'r', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)





