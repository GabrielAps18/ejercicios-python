#Programa para obtener las tablas de multiplicación de cualquier numero
def run():
    tabla = int(input("¿Qué tabla desea obtener?: "))
    #Definimos el rango del 1 al 10
    for i in range(1, 11):
        print(f'{tabla} x {i} = {tabla*i}')

if __name__ == '__main__':
    run()