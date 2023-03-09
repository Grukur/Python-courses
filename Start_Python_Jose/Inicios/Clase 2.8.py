
"""
Control de Clases
"""

"""
Miercoles 17 de Junio llegamos a la clase: 2,10
"""

#ejercicio de lista con tople
 friends={"dad":(45, 60, 65, 70),"lily":45,"suky":35}

 for name, age in friends.items():
     print(name, age)


ejercicio para usar el else con for
cars=["ok","ok","ok","ok","faulty","ok","ok",]

    
for status in cars:
    if status == "faulty":
        print("Stop, bad car")
        break
    print("this car is ok")
    print("shipped")
else:
    print("todo ok, exito!")

 codigo para sacar numeros primos
origen=int(input("coloque un numero y veamos si es primo: "))
for i in range(2,origen):
    if origen%i == 0:
        break        
else:
    print("el numero ", origen, " es primo!")




