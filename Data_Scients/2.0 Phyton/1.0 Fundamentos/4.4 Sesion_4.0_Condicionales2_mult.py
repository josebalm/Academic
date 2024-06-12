"""
OBJETIVO : DETERMINAR EL VALOR A PAGAR POR UN CLIENTE, EN UNA COMPRA

ANALISIS :
    ENTRADA :   cantidad comprada ( Valor numerico Float > 0)
                Precio unitaroi ( pesos / Kg, Numerico , Float > 0)
    SALIDAS : Mensaje indicando. elvalor a pagar
    PROCESOS :  1) DETERMINAR EL % DE DCTO EN FUNCION DE LA CANTIDAD COMPRADA.
                2) CALCULAR EL VALR A PAGAR, UTILIZANDO LA FORMULA:
                VALOR A PAGAR = CANTIDAD COMPRADA * EL PRECIO UNITARIO * (1-Dcto) 

"""


try:
    cantidad_comprada = float(input("Ingres la cantidad comprada:  "))
    precio_unitario = float(input("ingrese precio unitario: " ))

    if cantidad_comprada > 0 and precio_unitario > 0 :
        if cantidad_comprada < 2:
            descuento = 0
        elif cantidad_comprada < 5:
            descuento = 0.10
        elif cantidad_comprada < 10 :
            descuento = 0.15
        else:
            descuento = 0.20
        apagar= cantidad_comprada*precio_unitario*(1-descuento)
        print(f"Valor a pagar :  {apagar:.2f} ")


    else :
        print("La cantidad comprada y el precio unitario deben cer mayores o iguales que cero")

except Exception :
    print("datos invalidos")
