
print('Aloha World we start!!!\n')

'''
# forma basica de crear lista que acepte nuevos items

ls = []
def add():
    user = input('Aloha, pls give me data uga uga\n').split()
    ls.extend(user)
    print(ls)
    return add()
add()
'''

'''
# lista que acepta nuevos items mas limpia

ls1 = []
def adder():
    ls1.extend(input('Aloha, pls give me data\n').split())
    print(ls1)
    return adder()
adder()

'''

'''
# lista que acpeta nuevos items y ademas cierra programa

ls2 = []
def addplus():
    ls2.extend(input('Pls give data:\n').split())
    if 'exit' in ls2:
        quit()
    else:
        print(ls2)
        return addplus()
addplus()

'''

