#Example of Nested Lists and Dictionaries
#Ejemplo de Listas y Diccionarios anidados
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Gabriel", "lastanme": "Pacheco"}
#List of dictionaries
#Lista de diccionarios
    super_list = [
        {"firstname": "Gabriel", "lastanme": "Pacheco"},
        {"firstname": "Miguel", "lastanme": "Torres"},
        {"firstname": "Pepe", "lastanme": "Silva"},
        {"firstname": "María", "lastanme": "Llanos"},
        {"firstname": "José", "lastanme": "García"},
    ]
#Dictionary of lists
#Diccionario de listas
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1 ,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f'The {key} are {value}')

    for values in super_list:
        for key, value in values.items():
            print(f'{key}: {value}')

if __name__ == '__main__':
    run()