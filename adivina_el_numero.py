#Juego para adivinar un numero random
from ast import main
import random
from turtle import mainloop

def adivina(numero):
    num_random = random.randint(1, 100)
    while numero != num_random:
        if numero < num_random:
            print("Busca un numero más grande")
        else:
            print("Busca un numero más pequeño")
        numero = int(input("Elige otro numero: "))
    print(f"FELICIADES, EL NUMERO ERA {numero}")

def run():
    numero = int(input("Ingresa un numero del 1 al 100: "))
    adivina(numero)
if __name__ == '__main__':
    run()

