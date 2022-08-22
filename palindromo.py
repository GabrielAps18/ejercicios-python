#Programa para detectar si una palabra es un palindromo (que se lea igual al derecho y al revés)
def palindromo(palabra):
    palabra_copia = palabra
    palabra = palabra.replace(' ', '').lower().strip()
    if palabra == palabra[::-1]:
        print(f'La palabra {palabra_copia} es un palindromo')
    else:
        print(f'La palabra {palabra_copia} no es un palindromo')
        
def run():
    palabra = input("Ingrese una frase o palabra: ")
    palindromo(palabra)
    

if __name__ == '__main__':
    run()