
for i in range (10):
    rut = (input("Favor escribe tu RUT sin punto ni digito verificador: "))
    lista = [int(x) for x in str(rut)]
    lista.reverse()
    
    ctrl = [2,3,4,5,6,7,2,3,4]
    ver = 11 - (sum([ctrl[i] * lista[i] for i in range(len(rut))]) % 11) # se simplifican 4 variables
    print(ver)
    if ver == 10 and 9 > len(rut) > 6:
        print("Tu RUT es: ",rut,"-","K","\n")
    elif ver == 11 and 9 > len(rut) > 6:
        print("Tu RUT es: ",rut,"-","0","\n")    
    elif 0 < ver < 10 and 9 > len(rut) > 6:
        print("Tu RUT es: ",rut,"-",ver,"\n")  
    else:    
        print("Tu RUT no existe")
        break
