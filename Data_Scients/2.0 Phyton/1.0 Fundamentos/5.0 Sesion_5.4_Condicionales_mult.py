"""
Calcular la utilida que un trabajador recibe en el reparto anual de utilidades, si la decision se toma
con base a la antiguedad en la empresa


< 1 año     ----> 5%
1 - 2 años  ----> 7%
2 - 5 años  ----> 10%
5 - 10 años ----> 15%
> 10 años   ----> 25%

"""

antiguedad = int(input("ingrese antiguedad: "))
salario = float(input("ingrese salario : "))

if antiguedad <= 1 :
    utilidad = 0.05
    
elif antiguedad > 1 and antiguedad <= 2 :
    utilidad = 0.07

elif antiguedad > 2 and antiguedad <= 5 :
    utilidad = 0.1

elif antiguedad > 5 and antiguedad <= 10 :
    utilidad = 0.15

elif antiguedad > 10 :
    utilidad = 0.25

ganado = salario * utilidad
print(f"lo ganado fue ${ganado:.2f},\ny el salario total fue ${(ganado+salario):.2f}")













