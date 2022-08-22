#Conversor de dolares a monedas de LATAM con Python
def conversor(tipo_moneda, valor_dolar):
    cantidad = round(float(input(f"Ingrese la cantidad de {tipo_moneda} que desea convertir: ")), 2)
    conversion = round(cantidad*valor_dolar, 2)
    print(f'Los {cantidad} {tipo_moneda} a dólares son ${conversion} dolares.')

moneda = int(input('''
    ¿Qué moneda deseas convertir?: 
        1-. Peso colombiano a Dólar.
        2-. Peso Mexicano a Dólar.
        3-. Bolívar soberano a Dólar.
        4-. Peso argentino a Dólar.
    Ingresa tu opción: '''))
#
if moneda == 1:
    conversor("pesos colombianos", 0.00023)
elif moneda == 2:
    conversor("pesos mexicanos", 0.05)
elif moneda == 3:
    conversor("bolívares soberanos", 0.14)
elif moneda == 4:
    conversor("pesos argentinos", 0.0073)



    