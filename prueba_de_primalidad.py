#Programa para saber si un numero es primo
def es_primo(numero):
    for i in range(2, numero - 1):
        if numero % i == 0:
            return True
    return False

def run():
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        print(f'El numero {numero} no es primo.')
    else:
        print(f'El numero {numero} es primo.')

if __name__ == '__main__':
    run()