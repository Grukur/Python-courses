""" Intento 1 para obtener digito """

for i in range (10):
    rut=int(input("favor escribe tu RUT sin digito verificador: "))
    lista = [int(x) for x in str(rut)]
    
    if len(lista) == 7:
        ctrl= [0,2,3,4,5,6,7,2]
        multi=[lista[-i]*ctrl[i]
        for i in range(1,len(ctrl))]
        su=sum(multi)
        c=su%11
        ver=11-c
        if ver ==10:
            print("el codigo verificador de tu RUT es: ","K","\n",
                  "por lo que tu rut es: ",rut,"-","K")
        elif ver==11:
            print("el codigo verificador de tu RUT es: ","0","\n",
                  "por lo que tu rut es: ",rut,"-","0")    
        else:
            print("el codigo verificador de tu RUT es: ",ver,"\n",
                  "por lo que tu rut es: ",rut,"-",ver)
        
    if len(lista) == 8:
        ctrl1= [0,2,3,4,5,6,7,2,3]
        multi1=[lista[-i]*ctrl1[i]
        for i in range(1,len(ctrl1))]
        su1=sum(multi1)
        c1=su1%11
        ver1=11-c1
        if ver1 ==10:
            print("el codigo verificador de tu RUT es: ","K","\n",
                  "por lo que tu rut es: ",rut,"-","K")
        if ver1==11:
            print("el codigo verificador de tu RUT es: ","0","\n",
                  "por lo que tu rut es: ",rut,"-","0") 
        if ver1 == 9:
            print("el codigo verificador de tu RUT es: ",ver1,"\n",
                  "por lo que tu rut es: ",rut,"-",ver1)
        else:
            print("Tu RUT no existe")
        break

    

    
"""
Rut George 13048784-k
Rut Amaya 25089006-0
Rut Dad   5637875
"""





    

