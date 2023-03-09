
# def outer():
#     msg = 'Python'
#     x = 1
#     def inner():
#         print(f'{msg}')
#         y = 3
#         y = y+x
#         print(y)
#     return inner
#
# lf = outer()
#
# print(lf())

                    # ESTO FUNCIONA COMO UN GENERADOR, EL RETORNO ES LO ELEMENTAL, YA QUE LF GUARDA LA DATA

# def outer():
#     msg = 'Python'
#     x = 1
#     def inner():
#         print(f'{msg}')
#         nonlocal x
#         x += 1
#         print(x)
#     return inner
#
# lf = outer()
#
# lf()
# lf()
# lf()
# lf()


