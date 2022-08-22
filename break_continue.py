def run():
    for contador in range(50):
        if contador % 2 != 0:
            continue #no se ejecuta la linea de abajo cuando se cumple la condicion
        print(contador)
        if contador == 40:
            break #interrumpe el código
if __name__ == '__main__':
    run()