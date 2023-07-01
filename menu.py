def mostrar_menu():
    """brief: crea un menu de opciones

    parametros: None

    return:None  """
    for opcion in menu:
        print(opcion)


menu = ["\n\n| 1. Traer datos desde archivo",
        "| 2.  Listar cantidad por raza",
        "| 3.  Listar personajes por raza",
        "| 4.  Listar personajes por habilidad ",
        "| 5.  Jugar batalla",
        "| 6.  Guardar Json",
        "| 7.  Leer Json",
        "| 8. Crear Dios.csv",
        "| 9. Ordenar personaje por atributo",
        "| 10. Pokemon",
        "| 11.  Salir del programa"]