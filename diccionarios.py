def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'lalve2': 2,
    #     'lalve2': 3,
    # }
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    #print(poblacion_paises['Argentina'])

    # Devuelve las keys
    # for pais in poblacion_paises.keys():
    #     print(pais)

    #Devulelve el valor de la key
    # for pais in poblacion_paises.values():
    #     print(pais)

    #Devuelve ambos valores, key + value
    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes.')
if __name__ == '__main__':
    run()