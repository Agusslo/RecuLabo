import re
import json
import csv
import os

#--------------------------------------------------------1----------------------------------------------------

def convertir_habilidades_a_minuscula(habilidades: list) -> list:
    """brief: convierte las habilidades que estan escritas en el csv en minuscula

    parametros: habilidades

    return: habilidades_minuscula """
    habilidades_minuscula = [habilidad.lower() for habilidad in habilidades]
    return habilidades_minuscula

def traer_archivos(path) -> list:
    """brief: crea el archivo principal donde estan todos los personajes y sus respectivos datos
    se utilizin regex para quitarles cualquier tipo de espacio y caracteres que puedan afectar a la hora de escribir el codigo


    parametros: path

    return: lista_personaje """
    lista_personaje = []
    with open(path, "r", encoding="utf8") as archivo:
        for line in archivo:
            registro = re.split(",|\n", line)
            personaje = {}
            personaje["id"] = int(registro[0])
            personaje["nombre"] = (registro[1])
            personaje["razas"] = [raza.strip().lower() for raza in registro[2].split(",")]
            personaje["poder_pelea"] = int(registro[3])
            personaje["poder_ataque"] = int(registro[4])
            personaje["habilidades"] = registro[5].strip().lower()
            if "|$%" in registro[5]:
                personaje["habilidades"] = [habilidad.strip().lower() for habilidad in registro[5].split("|$%")]
            lista_personaje.append(personaje)

    return lista_personaje



#--------------------------------------------------------5----------------------------------------------------

def crear_archivo_batalla(lista_personaje,fecha,ganador,perdedor):
    """brief: Crea un archivo de texto en el cual se pueden ver cuando se utiliza la funcion
    elegir_jugador se ven el ganador de la batalla, le perdedor y que fecha y hora se jugo

    parametros: lista_personaje, fecha, ganador, perdedor

    return: None """
    with open("resultados_batallas.txt", "a") as archivo:
        archivo.write("---------------------\n")
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(f"Ganador: {ganador['nombre']}\n")
        archivo.write(f"Perdedor: {perdedor['nombre']}\n")
        archivo.write("---------------------\n")


#--------------------------------------------------------6----------------------------------------------------

def guardar_json(habilidades, raza, habilidad):
    """brief: crea un archivo json, en el cual el nombre es la raza y la habilidad de cada personaje ingresado 
    por el usuario.En ese se pueden observar todos los personajes que tengan raza y habilidades iguales

    parametros: habilidades, raza, habilidad

    return: None """
    nombre_archivo = f"{raza}_{habilidad}.json"
    
    datos = []
    for personaje in habilidades:
        habilidades = [h for h in personaje["habilidades"] if h != habilidad]
        datos_personaje = {
            "Nombre": personaje["nombre"],
            "Poder de ataque": personaje["poder_ataque"],
            "Habilidad": personaje["habilidades"]
        }
        datos.append(datos_personaje)
    
    with open(nombre_archivo, "w") as archivo:
        json.dump(datos,archivo)

#--------------------------------------------------------7----------------------------------------------------


def leer_personajes_en_json(archivo):
    if not os.path.isfile(archivo):
        print(f"El archivo '{archivo}' no existe.")
        return
    
    with open(archivo, "r") as archivo_json:
        try:
            lista = json.load(archivo_json)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el archivo JSON: {e}")
            return
    for personaje in lista:
        print("--------------------------------------------------------")
        print("Nombre:", personaje.get('Nombre', 'Nombre desconocido'))
        print("Poder de ataque:", personaje.get('Poder de ataque', 'Poder de ataque desconocido'))
        habilidades = personaje.get('Habilidad', [])
        if habilidades:
            habilidades_str = ", ".join(habilidades)
            print("Habilidades:", habilidades_str)
        else:
            print("Habilidades: Habilidades desconocidas")
        print("--------------------------------------------------------")


#--------------------------------------------------------8----------------------------------------------------

def incrementar_poder(personajes):
    """brief: La función incrementar_poder aumenta el poder y habilidades de los personajes de la raza "Saiyan" en un porcentaje específico y agrega una nueva habilidad llamada "Transformación nivel dios". Devuelve la lista de personajes modificados.

    parametros: personajes poder_ataque poder_pelea habilidades un_personaje

    return: un_personaje"""
    un_personaje = []
    for personaje in personajes:
        if "saiyan" in personaje.get("razas"):
            poder_ataque = personaje.get("poder_ataque") + ((personaje.get("poder_ataque") * 70)//100)
            poder_pelea = personaje.get("poder_pelea") + ((personaje.get("poder_pelea") * 50)//100)
            habilidades = personaje.get("habilidades")
            habilidades.append("Transformación nivel dios")
            personaje.update({"habilidades":habilidades,"poder_ataque":poder_ataque,"poder_pelea":poder_pelea})
            un_personaje.append(personaje)
    return un_personaje

def guardar_saiyan_csv(personajes):
    """brief: recive los sayayines con los poderes aumentados y los guarda en un csv

    parametros: personajes fieldnames writer personaje

    return: """
    with open('aumento_poder_saiyan.csv', 'w', newline='',encoding="utf8") as csvfile:
        fieldnames = personajes[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader() #para escribir el csv
        for personaje in personajes:
            writer.writerow(personaje)
