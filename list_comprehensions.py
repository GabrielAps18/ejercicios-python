def run():
#Save the squares from 1 to 100
#Guardar los cuadrados del 1 al 100
    squares1 = []
    for i in range(1, 101):
        squares1.append(i**2)
    print(squares1)

#Save the squares (from 1 to 100) that are not divisible by 3
#Guardar los cuadrados (del 1 al 100) que no sean divisibles entre 3
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(squares)
    
#Save numbers that are divisible by 4, 6 and 9
#Guardar numeros que sean divisibles entre 4, 6 y 9
    challenge = [i for i in range (1, 1000) if i % 36 == 0]
    print(challenge)
    
if __name__ == '__main__':
    run()