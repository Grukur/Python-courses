
# 1
# with open('data.txt', 'r') as file:
#     r = file.readlines()
#     print(str(r))
#

# # 2
# def tail(data, line):
#     with open(data, 'r') as file:
#         content = [x for x in file]
#         print(content[-line::])
#
# tail('data.txt', 5)
# #

# 3
# from time import sleep
# def tail(data, line):
#     with open(data, 'r') as file:
#         content = [x for x in file]
#         for _ in range(5):
#             print(content[-line::]); sleep(3)
#
# tail('data.txt', 5)

# # 4
# with open('data.txt', 'r+') as file:
#     lines = len([x for x in file])
# with open('data.txt', 'r+') as file:
#     words = len(file.read().split())
# with open('data.txt', 'r+') as file:
#     chars = [y for x in file for y in x]
#
# print(lines, 'Lineas', words, 'Palabras', len(chars), 'Letras')

# 5
# with open('bank.txt', 'r') as file:
#     data = [x.strip('\n').split(':') for x in file.readlines()]
#     bk = [int(y) for x, y in data if x == 'D']
#     bs = [int(y) for x, y in data if x == 'W']
#
# print('Final balance: ', sum(bk) - sum(bs))

# 6
# with open('data.txt', 'r') as file1:
#     lines1 = [x.strip('\n') for x in file1.readlines()]
#
# with open('data2.txt', 'r') as file2:
#     lines2 = [x.strip('\n') for x in file2.readlines()]
#
# x = 0
# while x < 30:
#     if len(lines1[x]) == len(lines2[x]):
#         x += 1
#     else:
#         print(f'Error en fila: {x}: {lines2[x]}')
#         break

# 7
# with open('american-english.txt') as file:
#     words = [x.strip('\n') for x in file]
#     lens = [len(x) for x in words]
#     dict1 = dict(zip(words, lens))
# print(dict1)

# 8
# with open('american-english.txt') as file:
#     words = [x.strip('\n') for x in file]
#     lens = [len(x) for x in words]
#     dict1 = dict(zip(words, lens))
#     order = sorted(dict1.items(), reverse=True, key=lambda x: len(x[0]))
#
# for x in range(1, 101):
#     print('Palabra nulmero: ',x , order[x])

# 9
# with open('american-english.txt') as file:
#     words = [x.strip('\n') for x in file]
#
# tim = [y for x in words for y in x]
# tot = {x: (tim.count(x)) for x in set(tim)}
# final = sorted(tot.items(), reverse=True, key=lambda x: x[1])
#
# print(final)

#                         # SOLUCION LARGA
# for x in words:
#     for y in x:
#         tim.append(y)
#
# for x in set(tim):
#     tot[x] = (tim.count(x))
#
# final = sorted(tot.items(), reverse=True, key=lambda x: x[1])
#
# print(final)

# 10
# with open('american-english.txt') as file:
#     words = [x.strip('\n') for x in file]
#
# tim = [y for x in words for y in x]
# dic1 = {x: (tim.count(x)) for x in set(tim)}
# tot = sorted(dic1.items(), reverse=True, key=lambda x: x[1])
#
# print(tot[:3:])







