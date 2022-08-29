#Ejecircio para aprender a utilizar VS para depurar codigo y uso de try / except
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try: 
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")
    #else:   

if __name__ == '__main__':
    run()