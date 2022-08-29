def run():
#Dictionary whose keys are the numbers from 1 to 100 and the values are the cube of each number
#Diccionario cuyas keys son los numeros del 1 al 100 y los valores son el cubo de cada numero

    #dict = {i: i**3 for i in range(1, 101)}

#Only save those that are not divisible by 3    
#Solo guardar los que no sean divisible entre 3

    #dict = {i: i**3 for i in range(1, 101) if i**3 % 3 != 0}
    
#Dictionary whose kays are numbers from 1 to 1000 and their values are the square root of each number
#Diccionario cuyas kays son numeros del 1 al 1000 y sus valores son la raiz cuadrada de cada numero
    dict = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(dict)
if __name__ == '__main__':
    run()