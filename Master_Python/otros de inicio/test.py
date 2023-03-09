# a = 4.262656564
#
# print(f'{a:.3f}')
#
# b = round(a,3)
# print(b * 3)
#
# a = 3.4
# b = 2.3
# c = a + b
# print(c)
#
# print('casa'.center(180, "."))
# my_product = 1
#
# my_sum = sum(range(1, 26))
#
# for i in range(1,26):
#     my_product *= i
#
#
#
# list1 = list(range(-10, 99, 3))
#
# list2 = list(range(99, -4, -2))


# for x in range(100):
#     if x % 2 == 0:
#         print('else bobo', x)
#         continue # util para evitar que el flujo siga avanzando
#     if x % 2 == 1:
#         print('somi somi', x)
#         continue
#
#     print('final', x)

## YOUR CODE GOES HERE:
# Start a while loop that calculates the sum of odd numbers from 1 to 100.
# Use my_sum variable to save the value

# x = 100
# list1 = []
# while x > 0:
#     x -= 1
#     if x % 2 != 0:
#         list1.append(x)
#
# my_sum = sum(list1)
#
# print(my_sum)


# num = [1, 2 ,3]
#
# num.extend(['hello'])
# print(num)


# def gene (num):
#     for i in range(num):
#         yield i * i
#         i += 1
#
# inp = int(input('dame un numero: '))
# gene1 = gene(inp)
#
# # print(next(gene1))
# # print(next(gene1))
# # print(next(gene1))
# # print(next(gene1))
#
# for i in gene1:
#     print(f'{i}')


# sales = {2017: 30000, 2018: 40000, 2019: 50000}
#
# profit = {k: v*(1.15) for k, v in sales.items()}
#
# print(profit)


# visits = {'Monday': 5000,
#           'Tuesday': 3000,
#           'Wednesday': 4000,
#           'Thursday': 4500,
#           'Friday': 5000,
#           'Saturday': 2000,
#           'Sunday': 1500
#           }
#
# total_visits = 0
# for k, v in visits.items():
#     total_visits += v
# print(total_visits)
#
# percentage = {k: (v/total_visits)*100 for k, v in visits.items()}
# print(percentage)

#                   CHALLENGE

# user = int(input('Please give me a Number: '))
#
# for i in range(user):
#     print(i, 'base')
#     for x in range(1,i+1):
#         if i % x == 0:
#             print(x, 'divisor') # imprimir toma tiempo

# x = int(input('dame un numero: ')) # solucion Andrei
# divisors = []
# for i in range(2, x//2+1):
#     if x % i == 0:
#         divisors.append(i)
#
# print(divisors)


# nums = ('10,20,30,40,50').split(',') # split guarda en lista, siguen siendo string, pero en lista
# print(f'{" ".join([i for i in nums])}') the comprehension is useless, nums already a list
# print([int(i) for i in nums]) # para obtener int


# print([i for i in range(1500, 3201) if i % 7 == 0 and not i % 5 == 0], end=',')

# for i in numbers:
#     if i % 7 == 0 and not i % 5 == 0:
#         print(i, end=',')

# user_rev = input('Tell me 3 words pls: ').split(' ')
# print(f'{" ".join(user_rev[::-1])}')

# user = input('dame palabras separadas por "-", gracias: ').lower().split('-')
# user3 = sorted(user)
# print(f'{"-".join(user3)}')


# user = ('I love cat and dogs').split
#
# for i in user():
#     print(f'{i[::-1]}', end=" ")

# print(f'{" ".join([i[::-1] for i in user()])}', end=" ")


# user = ('I love cat and dogs').split(' ')
# usr2 = [i[::-1] for i in user]
# print(f'{" ".join(usr2)}')


# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# len_words = [len(i) for i in words]
# final = list(zip(words, len_words))
# print(final)

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash'] # solucion optima
# print([(w, len(w)) for w in words])

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# len_words = [len(i) for i in words]
# final = dict(zip(words, len_words))
# print(final)
#
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash'] # solucion optima
# print([(w, len(w)) for w in words])

# names, phones = ["Dan", "John", "Diana"], [11111, 2222, 3333]
# print(set(zip(names, phones)))


# l1 = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# l2 = ['Python', 'carlos', 'C++', 'adolfo', 'eureka', 'sami']
#
# final = set(l1).intersection(l2)
# print(final)

# 'parte 2 de ejecricios'

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# kd2 = {k: v for k, v in sorted(d1.items())}
# print(kd2)

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# vd1 = {k: v for k, v in sorted(d1.items(), key=lambda v: v[1])}
# print(vd1)

# employees = {'John': ('London', 4000, 28) ,'Diana': ('NYC', 3500, 31), 'Maria': ('Madrid', 4200, 40)}
# sort1 = {k: v for k, v in sorted(employees.items(), key=lambda i: i[1][1])}
# print(sort1)

# import Challange_country as country

# sort1 = {k: v for k, v in sorted(country.COUNTRY.items())}
# print(sort1)

# sort1 = {k: v for k, v in sorted(country.COUNTRY.items(), reverse=True ,key=lambda i: len(i[1]))}
# print(sort1)

# years, sales = [2015, 2016, 2017, 2018, 2019, 2020], [350000, 400000, 410000, 439000, 500000, 290000]
# print(list(zip(years, sales)))

# years, sales = [2015, 2016, 2017, 2018, 2019, 2020], [350000, 400000, 410000, 439000, 500000, 290000]
# print(dict(zip(years, sales)))

# years, sales = [2015, 2016, 2017, 2018, 2019, 2020], [350000, 400000, 410000, 439000, 500000, 290000]
# dict1 = (dict(zip(years, sales)))
#
# profit = {k: (v-(v/1.25)) for k, v in dict1.items()}
# print(profit)
#
# n = 2015
# for k, v in dict1.items():
#     print((dict1[n + 1] / dict1[n]) - 1)
#     if n < 2019:
#         n += 1


# a1, a2 = input('Please give me 2 numbers to work: ').split(' ')
# a1, a2 = int(a1), int(a2)
# b = a1
# a = 0
# while b > a2:
#     a += 1
#     if b % a2 > 0:
#         print('error')
#         break
#     else:
#         b /= a2
# else:
#     print(f'{a1} y {a2} son potencia de {a+1}')

# def first1():
#     """
#     this is my first func, this print a sting
#     """
#     print('aloha!')
#
# first1()
# print(first1.__doc__)
# help(first1) #me gusta mas

# def say_my_name(my_name):
#     print(f'My name is {my_name}')
#
# say_my_name('John')

# def get_vat(price, vat):
#     return price*vat
#
# vat = get_vat(200, .05)
# print(vat)

# x = 5
# def increment():
#     global x
#     x += 1
# increment()
# print(x)

# Use whatever name for the functions's parameter
# def reverse(string1):
#
#     return string1[::-1]
#
# s = reverse('comalon')
# print(reverse('comalon'))
# print(s)

# def vowel_count(my_str):
#     """
#     This function counts the number of vowels in a string and returns a dictionary.
#     """
#     vowels = 'aeiou'
#     my_str = my_str.lower()
#     vowels2 = list(vowels)
#
#     count1 = [x for x in my_str if x in vowels]
#     count2 = [str(my_str).count(y) for y in my_str if y in vowels2]
#     return dict(zip(count1, count2))

# result = {}
#
# for char in my_str:
#     if char in vowels:
#         if char in result.keys():
#             result[char] += 1
#         else:
#             result[char] = 1
#
# return result

# s = vowel_count('aloha amigo')
# print(s)

# def counter(my_str):
#     vowels = 'aeiou'
#     my_str = my_str.lower()
# 
#     vowls = len([x for x in my_str if x in vowels])
#     cons = len([x for x in my_str if x not in vowels])
# 
#     return vowls, cons
# 
# s = counter('aloha amigo mio querido')


# sample_list = [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
#
# def new_list(list1):
#     print(set(list1))
#
# new_list(sample_list)

# def perfection(number):
#     divs = [x for x in range(1, number) if number % x == 0]
#     if sum(divs) == number:
#         print(f'{number} is a perfect number')
#     else:
#         print(f'{number} is not a perfect number')
#
# perfection(6)

# def primus(number):
#     num = [x for x in range(1, number) if number % x == 0]
#     if len(num) < 2:
#         print(number, "True")
#     else:
#         print(f'{number} False')
#
# primus(7)

# def primus(number):
#     primes = []
#     while len(primes) < 5:
#         num = [x for x in range(1, number//2) if number % x == 0]
#         if len(num) < 2:
#             primes.append(number)
#         number += 1
#     print(primes)
#
# primus(1000000)

# def equilibrium(list1):
#     for x in range(len(list1)):
#         if sum(list1[x:]) == sum(list1[x::-1]):
#             print(f'El punto de quilibro esta en {list1[x]} en index = {x}')
#
# equilibrium([-7, 1, 5, 2, -4, 3, 0])

# word = open('a.txt', 'r')
#
# word.seek(4)
# content = word.read(5)
#
# print(str(content))
# word.close()




with open('ip.txt') as file:
    ip_list = file.read().split()

print(ip_list)












