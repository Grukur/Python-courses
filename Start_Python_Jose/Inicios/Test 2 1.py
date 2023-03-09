
# estamos viendo sets

fruta1={"Manzana", "Pera", "Naranja", "Uva", "lima", "limon"}
verduras1={"lechuga", "Beterraga", "Zanahoria", "Tomate"}



print("\n","En set, veremos 2 conjuntos, frutas y verduras", "\n","\n",
      "Fruta contiene", "\n","\n", fruta1, "\n", "\n", 
      "verduras contiene","\n", "\n", verduras1, "\n", "\n")
    
fruta1.update(["Toronja", "Kiwi", "Tomate"])



print("Querido usuario, favor dime que operacion deseas realizar","\n", "\n",
      "1 - para imprimir fruta", "\n",
      "2 - para imprimir verduras", "\n",
      "3 - para buscar elementos repetidos", "\n",
      "4 - para salir")


for i in range (10):
    user=int(input("favor dimer tu opcion: "))
    if user == 4:
        print("\n","Adios, has salido")
        break
    elif user == 1:
        fruta=", ".join(fruta1)
        print("\n","las frutas son: ", "\n",fruta)
    elif user == 2:
        verduras=", ".join(verduras1)
        print("\n","las verduras son: ", "\n",verduras)
    elif user == 3:
        inter=fruta1.intersection(verduras1)
        inter1=", ".join(inter)
        print("\n","Los objetos que existen en la interseccion de Frutas y Verduras, son ","\n","\n",inter1)
    




# hay que trabajar con los comandos de set y hacerlos funcionales con usuario
#
# abajo se ven list, basicamente tienen 2 comandos hasta ahora, .append() y .remove()

"""
autos=["chevrolet", "audi", "mercedez"]
motos=["harley","honda","audi"]

print("en List veremos dos grupos, autos y motos", "\n", "\n", "autos contiene:","\n", autos, "\n","\n","motos contiene:","\n", motos)


autos.append("nissan")

print(autos)
"""



    


    
