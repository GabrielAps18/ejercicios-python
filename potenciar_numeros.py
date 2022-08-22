#Programa para potenciar un numero las veces que quieras
def potenciar(numero, veces):
    potencia = 1
    while potencia <= veces:
        resultado = numero**potencia 
        print(f'{numero} elevado a {potencia} es igual a {resultado}.')
        potencia += 1

def run():
    numero = int(input("Ingrese el numero que desea potenciar: "))
    veces = int(input("Cuantas veces desea potenciar el numero: "))
    potenciar(numero, veces)

if __name__ == '__main__':
    run()