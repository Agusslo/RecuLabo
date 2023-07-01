from archivos import *
import random
from datetime import datetime
import csv

# .get es un metodo de los objetos diccionarios que te permite acceder a un valor mediante la clave que se le pasa. En caso de no estar la clave en el diccionario puede devolver un valor por default. Por default devuleve None



#--------------------------------------------------------2----------------------------------------------------

def listar_cantidad_por_raza(personajes):
    """brief: La función cuenta la cantidad de personajes por raza en una lista y devuelve los resultados.

    parametros: razas listado_razas count raza personaje personajes

    return: razas"""
    razas = {}
    for personaje in personajes:
        listado_razas = personaje.get("razas")
        for raza in listado_razas:
            if raza in razas:
                count = razas.get(raza) + 1
                razas.update({raza:count})
            else:
                razas.update({raza:1})
    return razas

#--------------------------------------------------------3----------------------------------------------------

def listar_personajes_por_raza(personajes):
    """brief: La función recibe una lista de personajes y una habilidad. Retorna una lista de personajes que tienen esa habilidad, junto con su nombre, razas y promedio de poder.

    parametros: personaje personajes razas  raza listado_razas un_personaje

    return: razas"""
    
    razas = {}
    for personaje in personajes:
        listado_razas = personaje.get("razas")
        for raza in listado_razas:
            if raza in razas:
                un_personaje:list = razas.get(raza)
                un_personaje.append({"nombre": personaje.get("nombre"), "poder_ataque": personaje.get("poder_ataque")})
                razas.update({raza: un_personaje})
            else:
                razas.update({raza: [{"nombre": personaje.get("nombre"), "poder_ataque": personaje.get("poder_ataque")}]})
    for raza, personajes in razas.items():
        print(f"Raza: {raza}")
        for personaje in personajes:
            print(f" - Nombre: {personaje['nombre']}, Poder de ataque: {personaje['poder_ataque']}")
    return razas



#--------------------------------------------------------4----------------------------------------------------


def calcular_promedio(lista_personaje):
    """brief: Calcula el promedio del poder de ataque y poder de pelea

    parametros: lista_personaje

    return: promedio """
    promedio = (lista_personaje["poder_pelea"]+ lista_personaje["poder_ataque"]) // 2
    return promedio


def listar_personajes_por_habilidad(lista_personajes,respuesta):
    """brief: crea una lista de habilidades, donde se cargan nombre, raza y el promedio de poder

    parametros: lista_personaje, respuesta

    return:lista_habilidad  """
    
    lista_habilidad= []
    for personaje in lista_personajes:
        if respuesta in personaje["habilidades"]:
            lista_habilidad.append({"Nombre":personaje["nombre"],"Raza":personaje["razas"],"Promedio de Poder:":calcular_promedio(personaje)})
    return lista_habilidad

def mostrar_habilidades(lista_personaje):
    """brief: le pide al usuario una habilidad del personaje, muestra el nombre, raza, habilidad y el promedio de poder

    parametros: lista_personaje

    return: None """
    try:
        respuesta = input("INGRESE LA HABILIDAD DEL PERSONAJE: ").lower()
    except ValueError:
        print("ERROR AL INGRESAR EL TIPO DE DATO")
    except Exception:
        print("ERROR, VERIFICAR CODIGO")
    finally:
        lista = listar_personajes_por_habilidad(lista_personaje, respuesta)
        if lista:
            for personaje in lista:
                print("-----------------------------------------------------------------------------")
                print("Nombre:", personaje['Nombre'])
                print("Raza:", personaje['Raza'])
                print("Promedio de Poder:", personaje['Promedio de Poder:'])
        else:
            print("No existe un personaje con esta habilidad")




#--------------------------------------------------------5----------------------------------------------------


def elegir_jugador(lista_personaje): 
    """brief: el usuario ingresa un jugador y con la funcion random busca otro personaje
    y compara si el poder de ataque es mayor que el otro jugador gana, y tambien usa el datetime para 
    escribir la fecha y hora real

    parametros: lista_personaje

    return: archivo """
    try:
        jugador_1 = input("INGRESE UN PERSONAJE:").capitalize()
    except ValueError:
        print("ERROR, NO ES EL TIPO DE DATO CORRECTO")
    except Exception :
        print("Error verificar codigo")
    jugador_2 = random.choice(lista_personaje)

    for personaje in lista_personaje:
        if personaje["nombre"] == jugador_1:
            jugador_1 = personaje
            

    if jugador_1["poder_pelea"] > jugador_2["poder_pelea"]:
        ganador = jugador_1
        perdedor = jugador_2
    else:
        ganador = jugador_2
        perdedor = jugador_1

    fecha = datetime.now()
    archivo = crear_archivo_batalla(lista_personaje,fecha,ganador,perdedor)
    return archivo

#--------------------------------------------------------6----------------------------------------------------

def filtrar_habilidad(lista_personaje, raza, habilidad):
    """brief: filtra las razas y habilidades de los personajes 

    parametros: lista_personaje , raza, habilidad

    return: lista_filtrada """
    lista_filtrada = []
    for personaje in lista_personaje:
        if raza in personaje["razas"] and habilidad in personaje["habilidades"]:
            lista_filtrada.append(personaje)
    return lista_filtrada



def mostrar_json(lista_personaje):
    """brief: el usuario ingresa una raza y una habilidad, junto a la funcion filtrar_habilidad y 
    guardar_JSON, crean un archivo json donde se guardan los datos del personaje y los que tengas raza o habildades iguales


    parametros: lista_personaje

    return: None """
    razas = input("Ingrese una raza: ")
    habilidad = input("Ingrese una habilidad: ")

    filtrados = filtrar_habilidad(lista_personaje, razas, habilidad)
    archivo = guardar_json(filtrados, razas, habilidad)


#--------------------------------------------------------7----------------------------------------------------


def escribir_archivo_json(personaje):
    """brief: el usuario debe ingresar el nombre del archivo json que quiere
    ver para que se muestre

    parametros:personaje 

    return: nombre """
    nombre = input("Ingrese el nombre del archivo json: ")
    if not nombre.endswith(".json"):
        nombre += ".json"
    leer_personajes_en_json(nombre)
    return nombre



#--------------------------------------------------------9----------------------------------------------------


def ordenar_personajes_por_atributo(lista_personaje,atributo,orden):
    """brief: realiza un ordenamiento dependiendo la clave(atributo) y en el caso que los atributos 
    sean iguales los diferencia el poder de pelea de cada uno

    parametros: lista_personaje, atributo, orden

    return: lista_personaje """
    for i in range (len(lista_personaje)-1):
        for j in range (i+1,len(lista_personaje)):    
            if (lista_personaje[i][atributo] > lista_personaje[j][atributo] or 
                lista_personaje[i][atributo] == lista_personaje[j][atributo] and 
                lista_personaje[i]["poder_pelea"] > lista_personaje[j]["poder_pelea"]): 

                lista_personaje[i],lista_personaje[j] = lista_personaje[j],lista_personaje[i]

    return lista_personaje


def mostrar_atributos(lista_personaje):
    """brief: utilizando la funcion ordernar_personajes_por_atributo, va a ordernar la lista de forma
    asendente (a-z), por raaz

    parametros: lista_personajes

    return: ordenar  """
    ordenar = ordenar_personajes_por_atributo(lista_personaje,"razas",True)
    return ordenar


#--------------------------------------------------------10----------------------------------------------------


def generar_codigo_pokemon(personaje):
    #(Inicial Nombre)-([Ganador (A = Ataque | D = Defensa | AD = Empate])-(Valor más alto entre ataque y defensa)-(ID con los ceros restantes) 

    """brief: La función "generar_codigo_pokemon" crea un código único para un personaje de dbz basado en su nombre, poder de pelea, podes pelea, id

    parametros: ganador ataque mayor_valor defensa id_personaje p cant_ceros

    return: f"{p}-{cant_ceros}{id_personaje}" """
    ganador = "A"
    ataque = int(personaje.get("poder_pelea"))
    defensa = int(personaje.get("poder_ataque"))
    mayor_valor = ataque
    if defensa > ataque:
        ganador = "D"
        mayor_valor = defensa
    elif defensa == ataque:
        ganador = "AD"
    
    id_personaje = str(personaje.get('id'))
    p = f"{personaje.get('nombre')[0]}-{ganador}-{mayor_valor}"
    cant_ceros = "0"*(((18-len(p))-len(id_personaje))-1)
    return f"{p}-{cant_ceros}{id_personaje}"



def agregar_codigos_personajes(personajes):
    """brief: La función agregar_codigos_personajes asigna un código único a cada personaje en una lista y retorna la lista actualizada.

    parametros: personajes personaje codigo

    return: personajes """
    for personaje in personajes:
        codigo = generar_codigo_pokemon(personaje)
        personaje.update({"codigo":codigo})
    return personajes







