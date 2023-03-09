'''
Resolver el problema matematico de n3 +1:
si n es par, entonces lo dividimos por 2
si n es inpar, lo multiplicamos por 3 y le sumamos 1
'''

# def problem1():
#     user = int(input('Please enter a number to caclulate in 3n + 1 problem: \n'))
#     while user != 1:
#         if user % 2 == 0:
#             user = user / 2
#             print(f'{user:,.2f} is odd')
#         elif user % 2 != 0:
#             user = user * 3 + 1
#             print(f'{user} is even')
#     print(f'{user:,.0f} we finish')
#
# problem1()

'''
Usando List comprehension
'''

# def problema2():
#     user = input('Please enter a number to caclulate in 3n + 1 problem: \n')
#     num = [int(user)]
#     while num[0] != 1:
#         num = [num[0] / 2 if num[0] % 2 == 0 else num[0] * 3 + 1 for x in user]
#         print(num[0])
#     print(f'For {int(user):,.0f} given by you, is finish with {num[0]:,.0f}')
#
# problema2()


def problema3():
    user = [int(input('Please enter a number to caclulate in 3n + 1 problem: \n'))]
    while user[0] != 1:
        user = [user[0] / 2 if user[0] % 2 == 0 else user[0] * 3 + 1 for x in user]
        print(user[0])
    print(f'Finish in *** {user[0]:,.0f} ***')

problema3()

