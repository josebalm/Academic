"""
Calcular el numero de dias de un mes

"""
try:
    mes = int(input("indique el numero del mes: "))
    if mes < 1 or mes > 12:
        print("Mes invalido")
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
        print("31 dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        print("30 dias")
    else :
        print("28 dias")
except Exception:
    print("el numero de mes debe ser un entero entre 1 y 12") 



"""
Tambien puedes usar el comenado PASS en la excepcion.

"""
try:
    mes = int(input("indique el numero del mes: "))
    if mes < 1 or mes > 12:
        print("Mes invalido")
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
        print("31 dias")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11 :
        print("30 dias")
    else :
        print("28 dias")
except:
    pass 

"""
El comando pass le indica que el programa no debe hacer nada.
"""
    



