"""
ENUNCUADO: 
        Se dispone de un termometro para medir con exactitud la temperatura en un determinado lugar, sin embargi, les basta con 
        saber de manera aproximada si la termpertura se ajusta a los rangos siguientes:

                | RANGO DE TEMPERATURA |  SENSACION TERMICA |
                | [-10 - 10)           |  MUCHO FRIO
                | [ 10 - 15)           |  POCO FRIO
                | [ 15 - 25)           |  TEMPERATURA NORMAL
                | [ 25 - 35)           |  POCO CALOR
                | [ 35 - 45)           |  MUCHO CALOR

        LEA LA TEMPERATURA Y DEVUELVA LA SENSACION TERMINCA CORRESPONDIENTE

EJEMPLOS

                | ENTRADA  (TEMP)      |  SALIDA ESPERADA
                | 28                   |  POCO CALOR
                | -9                   |  MUCHO FRIO
                | 53                   |  TEMPERATURA FUERA DE RANGO

OBJETIVO : INDICAR LA SENSACION TERMINCA
ANALISIS
    ENTRAA:     Temperatura valor numerico, float [Sobre-entendida la escala - centigrados]
    SALIDA:     Mensaje indicando la sensacion termica
    PROCESO:    UBICAR EL VALOR DE LA TEMPERATURA EN EL RANGO ADECUADO E IMPRIMIR LA SENSACION TERMICA CORRESPONDIENTE.    

ALGORITMO:
    V1. Utilizando SI anidados
    inicio
        lea temperatura
        SI temperatura >- 10 y temperatura < 10 entonces
            RTA <- "mucho frio"
        SINO
            SI temperatura > 10 y temperatura < 15 entonces
                RTA <- "Ppoco frio"
            SINO
                 SI temperatura > 15 y temperatura < 25 entonces
                    RTA <- "TEMPERATURA NORMAL"
                SINO
                     SI temperatura > 25 y temperatura < 35 entonces
                        RTA <- "POCO CALOR"
                    SINO
                        SI temperatura > 35 y temperatura < 45 entonces
                            RTA <- "MUCHO CALOR"
                        SINO
                            RTA <- "FUERA DE RANGO"
                        FIN_SI
                    FIN_SI
                FIN_SI
            FIN_SI
        FIN_SI
    FIN_SI  
FIN_SI
"""

temp = float(input("Ingrese Temperatura   "))
if temp >= -10 and temp < 10:
    rta = "Mucho frio"
else:
    if temp > 10 and temp < 15:
        rta = "poco frio"
    else:
        if temp >15 and temp < 25:
            rta = "Temperatura Normal"
        else:
            if temp > 25 and temp < 35:
                rta = "poco calor"
            else:
                if temp > 35 and temp < 45:
                    rta = "mucho calor"
                else:
                    rta = "Temperatura fuera de rango"
print(rta)                    


