
"""
fruta={"manzana", "pera", "naranja", "uva", "lima", "limon"}

print(f"mis frutas son {fruta}")
"""


""" esta forma es la simple, la activa es una con loop

user=input("dame tu nombre: ")

if user:
    print("Aloha!!")
    
else:
    print("largo de aqui")
"""
    
for i in range(5):
    user=input("dame tu nombre: ")
    
    if user:
        if user == "999":
            print("Adios")
            break
        else:
            print("Hola")
    else:
        print("hasta luego")
        break