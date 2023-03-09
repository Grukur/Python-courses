

name=input("Hola! dime tu nombre para poder avanzar : ")

age=int(input("Dime tu edad: "))
segundos=age*31536000
horas=age*8760

print("\n", f"Buen dia", name, "como te encuentras hoy?", """
          
          Elige una opcion:
          1 - Deseas conocer cuantos segundos has vivido?
          2 - Quieres saber cuantas horas has vivido?
          3 - Quieres crear una lista magica?
          4 - Para salir""","\n")


for i in range (60):  
              
    opcion=int(input())
      
    if opcion == 4:
            print("\n","Adios y buena suerte!","\n")
            break
    elif opcion == 1:
        print("\n","Has vivido un total de ", segundos, "segundos, impactante!","\n")
    elif opcion == 2:
        print("\n","Has vivido un total de ", horas, "horas, para pensar en ello!","\n")
    elif opcion == 3:
        print("\n","Elige un numero para comenzar, este sera tu umero magico: ","\n")
        magic=int(input("Dime tu numero magico "))
        for i in range (10):
            print("Ahora dime otro numero, veamos si recuerdas tu primer numero xD","\n")
            number=int(input("Dime otro numero "))
            if number == magic:
                print("Wow, tienes una gran memoria!!!","\n")
                break
    break
    print("\n",name, """Elige otra opcion:
          1 - Deseas conocer cuantos segundos has vivido?
          2 - Quieres saber cuantas horas has vivido?
          3 - Quieres crear una lista magica?
          4 - Para salir""","\n")
       
        
    



