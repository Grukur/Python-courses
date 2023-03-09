'''Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then return that value.'''


# import math
#
# def rads2():
#     user = input('Please chose conversion needed:\na-Degrees to rads\nb-rads to degrees\n')
#     num = float(input('Please write the data to convert: '))
#
#     if user == 'a':
#         print('You Data is: ', num / (180 / math.pi))
#         if input('\nyou want convert another data? y/n\n') == 'y':
#             return rads2()
#         else:
#             quit()
#     if user == 'b':
#         print('You Data is: ', num * (180 / math.pi))
#         if input('\nyou want convert another data? y/n\n') == 'y':
#             return rads2()
#         else:
#             quit()
#     else:
#         print('pls choose a valid option')
#         return rads2()
#
# rads2()


'''Create a function in Python that accepts two parameters. 
The first will be a list of numbers. The second parameter will be a string 
that can be one of the following values: asc, desc, and none.

If the second parameter is "asc," then the function should return a list 
with the numbers in ascending order. If it's "desc," then the list should 
be in descending order, and if it's "none," it should return the original list unaltered. '''


# def lista():
#     ls = list(input('pls give me your numbers: ').split())
#     print(ls)
#     ord = input('pls chose how to order the list: asc, desc, none: ')
#     if ord == 'asc':
#         ls.sort(key=int)
#         print(ls)
#         return
#     if ord == 'desc':
#         ls.sort(key=int, reverse=True)
#         print(ls)
#         return
#     if ord == 'none':
#         print(ls)
#         return
#     else:
#         print('pls choose a valid option')
#         return lista()
#
# lista()


'''Write a function in Python that accepts a decimal number and returns 
the equivalent binary number. To make this simple, the decimal number 
will always be less than 1,024, so the binary number returned will always be 
less than ten digits long.'''


# ls = []
# nu = []
# def math():
#     ls.append(float(input('pls give me a number to convert in binary: \n')))
#
#     for x in range(int(ls[0])):
#         if int(ls[-1]) != 0:
#             nu.append(int(ls[-1])%2)
#             ls.append(int(ls[-1])//2)
#         else:
#             continue
#     nu.reverse()
#     print(*nu, sep=' ')
#
# math()

'''Other solution'''

# a = []
# def my_function():
#     i = int(input('pls give data: '))
#     while i > 0:
#         if (i % 2) == 0:
#             a.append(int(0))
#             i = i / 2
#         else:
#             a.append(int(1))
#             i = (i // 2)
#     a.reverse()
#     print(*a, sep='')
#
# my_function()


'''Create a function in Python that accepts a single word and returns the number of 
vowels in that word. In this function, only a, e, i, o, and u will be counted as 
vowels — not y.'''


# def Vowels():
#     user = str(input('Pleas write a sentence so i can count how many vowels are present: \n'))
#
#     fin = [x for x in user if x in ['a', 'e', 'i', 'o', 'u']]
#     print(f' you sentence have {len(fin)} vowels, and these are {fin}')
#
# Vowels()



'''Write a function in Python that accepts a credit card number. It should return 
a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent "4444444444444444", then it should return "4444".'''


# def Ccard():
#     user = input('Please give me you Credit Card number:\n')
#     ls = ['*' for x in user[0:11]]
#     ld = [x for x in user[12:16]]
#     print(*ls,*ld)
#
# Ccard()


'''Create a Python function that accepts a string. This function should count the 
number of Xs and the number of Os in the string. It should then return a boolean 
value of either True or False.

If the count of Xs and Os are equal, then the function should return True. 
If the count isn't the same, it should return False. If there are no Xs or Os in the string, 
it should also return True because 0 equals 0. The string can contain any type and number 
of characters.'''


# def CLeaner():
#     user = input('please give me a sentence so i can validate X and Os:\n')
#     lx = [x for x in user if x in ['x','X']]
#     lo = [x for x in user if x in ['o','O']]
#     if len(lx) == len(lo):
#         print(True)
#     else:
#         print(False)
#
# CLeaner()


'''Write a Python function that accepts three parameters. The first parameter is an integer. 
The second is one of the following mathematical operators: +, -, /, or . 
The third parameter will also be an integer.

The function should perform a calculation and return the results. For example, 
if the function is passed 6 and 4, it should return 24.'''


# def Cal():
#     user = input('Please enter first integer:\n')
#     user2 = input('Please enter operator (+, -, /, *:\n')
#     user3 = input('Please enter second integer:\n')
#
#     op = {'+': lambda x,y: x+y,
#           '-': lambda x,y: x-y,
#           '/': lambda x,y: x/y,
#           '*': lambda x,y: x*y}
#
#     print(op[user2](int(user), int(user3)))
#
# Cal()


'''Create a function in Python that accepts two parameters. 
The first should be the full price of an item as an integer. 
The second should be the discount percentage as an integer.

The function should return the price of the item after the 
discount has been applied. For example, if the price is 100 
and the discount is 20, the function should return 80.'''


# def Dsi():
#     user = input('please give me the price:\n')
#     user2 = input('give me how much discount we will apply: \n')
#
#     print(int(user)*(100-int(user2))/100)
#
# Dsi()


'''Write a function in Python that accepts a list of any length that contains a 
mix of non-negative integers and strings. The function should return a list with 
only the integers in the original list in the same order.'''


# def Lis():
#     user = input('pls give me you data so i can return the integers\n')
#
#     ls = [x for x in user if x.isdigit()]
#     print(*ls)
#
# Lis()


'''Create a Python function that accepts a string. The function should return a 
string, with each character in the original string doubled. If you send the function
"now" as a parameter, it should return "nnooww," and if you send "123a!", it should return 
"112233aa!!".
'''


# def Dob():
#     user = input('Please write the sentence you wish double each letter:\n')
#     ls = [x*2 for x in user]
#     print(*ls, sep='')
#
# Dob()


'''A simple one I like to throw at people, is to calculate the distance between 
any 2 points in 3D space... but that may be too easy for you'''


# def dis3d():
#     # ask user the coordinates of point A and B
#
#     usera = input('Please enter the coordinates of point A, Example: 10 20 30 ').split()
#     userb = input('Please enter the coordinates of point B: ').split()
#
#     # I create a list comprehension where we subtract the coordinates ((a(z) - b(z),
#     # a(x) - b(x), a(y) - b(y)) then apply power of 2 and that result is append to the list
#
#     headtail = [(float(x) - float(y)) ** 2 for x, y in zip(usera, userb)]
#
#     # with the values created on our list, we sum the values and apply square root of 2
#     # to get the final value = distance betwen the 2 points in a 3d space
#
#     distance = (sum(headtail)) ** (1 / 2)
#
#     print(distance)
#
#
# dis3d()

print('hello')

'''Solucion de Snugy'''


# usera = [10, 20, 30]
# userb = [1, 2, 3]
#
# def Dis3d():
#     # distance = ((((usera[0] - userb[0])**2) + ((usera[1] - userb[1])**2)) + ((usera[2] - userb[2])**2))**(1/2)
#
#     distX = ((usera[0] - userb[0]) ** 2)
#     distY = ((usera[1] - userb[1]) ** 2)
#     distZ = ((usera[2] - userb[2]) ** 2)
#     distance = (distX + distY + distZ) ** (1 / 2)
#
#     print(distance)
#
# Dis3d()

'''solucion dad'''






