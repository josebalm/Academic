try:
    valor_compra = float(input("Ingrese el valor de la compra:  "))
    if valor_compra > 200000:
        descuento = 0.20
    else:
        descuento = 0
    
    print("usted debe pagar: ",valor_compra * (1-descuento))

except Exception:
    print("error")