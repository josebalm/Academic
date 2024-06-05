"""
Se necesita calcular el salario semanal que recibira un obrero, el salario se liquida de la siguiente forma:
Se le paga un salario de $6.500/hora por las primeras 40 horas trabajadas, y $8.300/ hora por las horas adicionales.
(Si trabaha mas de 40 horas a la semana).
Proponga un metodo que permita determinar el salario del obrero.

"""

ht = int(input("Ingrese las horas de trabajo:  "))
if ht <= 40 :
    salario = ht*6500
elif ht > 40:
    salario = (40*6500)+((ht-40)*8300)
print("$",salario)

