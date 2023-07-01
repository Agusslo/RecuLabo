from funciones import *
from menu import *
from archivos import *


personaje= []

seguir = True

while seguir == True:
    mostrar_menu()
    try:
        respuesta = int(input("Ingrese Una Opcion: "))
        match respuesta:
            case 1:   
                personajes = traer_archivos("DBZ.csv")

            case 2:   
                data = listar_cantidad_por_raza(personajes)
                for personaje in data.keys():
                    print(data.get(personaje),"-",personaje)
            case 3:   
                data = listar_personajes_por_raza(personajes)
            case 4:
                mostrar_habilidades(personajes)
            case 5:
                elegir_jugador(personajes)
            case 6:
                mostrar_json(personajes)
            case 7:
                escribir_archivo_json(personajes)
            case 8:   
                personajes_actualizados = incrementar_poder(personajes)
                guardar_saiyan_csv(personajes_actualizados)
                print("csv generado correctamente")
            case 9:
                personajes_ordenados = mostrar_atributos(personajes)
                for personaje in personajes_ordenados:
                    print("\nNombre:", personaje["nombre"])
                    print("Raza:", personaje["razas"])
                    print("Poder de Ataque:", personaje["poder_ataque"])
                    print("----------------------------")
            case 10:
                personajes_con_codigos = agregar_codigos_personajes(personajes)
                for personaje in personajes_con_codigos:
                    codigo = personaje['codigo']
                    personaje_str = ', '.join(f"{k}: {v}" for k, v in personaje.items())
                    print(personaje_str)
                    print()
            case 11:
                seguir = False
    except ValueError:
        print("ERROR, NO INGRESO UN VALOR ENTERO")