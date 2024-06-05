concentracion = float(input("Digite valor de la concentración de PM10 24h en μg/m3.  "))

if concentracion >= 0 and concentracion <= 55 :
    Ii = 0
    Ih = 50
    BPi = 0
    BPh = 54
    ICA=  round((((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii)),0)
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")
    
    
elif concentracion > 55 and concentracion <= 155 :
    Ii = 51
    Ih = 100
    BPi = 55
    BPh = 154
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")

elif concentracion > 155 and concentracion <= 255 :
    Ii = 101
    Ih = 150
    BPi = 155
    BPh = 254
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")

elif concentracion > 255 and concentracion <= 355 :
    Ii = 151
    Ih = 200
    BPi = 255
    BPh = 354
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")

elif concentracion > 355 and concentracion <= 425 :
    Ii = 201
    Ih = 300
    BPi = 355
    BPh = 424
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")

elif concentracion > 425 and concentracion <= 505 :
    Ii = 301
    Ih = 400
    BPi = 425
    BPh = 504
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")

elif concentracion > 505 and concentracion <= 605 :
    Ii = 401
    Ih = 500
    BPi = 505
    BPh = 604
    ICA=  float(((Ih - Ii) / (BPh - BPi) * ( concentracion - BPi )+ Ii))
    if ICA >= 0 and ICA <= 50 :
        print('%.2f' %ICA, "VERDE")
    elif ICA > 50 and ICA <= 100 :
        print('%.2f' %ICA, "AMARILLO")
    elif ICA > 100 and ICA <= 150 :
        print('%.2f' %ICA, "NARANJA")
    elif ICA > 150 and ICA <= 200 :
        print('%.2f' %ICA, "ROJO")
    elif ICA > 200 and ICA <= 300 :
        print('%.2f' %ICA, "MORADO")
    elif ICA > 300 :
        print('%.2f' %ICA, "MARRON")
    else:
        print (-1, "Error en los datos. ")
else:
        print (-1, "Error en los datos. ")