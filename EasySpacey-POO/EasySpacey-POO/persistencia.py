import json

#Persistencia de datos, guardando y recuperando datos con archivos JSON
#Funciona cambiando los objetos a diccionarios y listas
#Guardado
#Habitacion -> Mueble -> Punto3D -> Diccionario -> JSON
#Carga
#JSON -> Diccionario -> Punto3D -> Mueble -> Habitacion

from habitacion import Habitacion
from mueble import Mueble
from punto3d import Punto3D


# Convertir a Diccionarios (cada uno)

def punto_a_diccionario(punto):
    return {
        "x": punto.get_x(),
        "y": punto.get_y(),
        "z": punto.get_z()
    }


def mueble_a_diccionario(mueble):
    return {
        "nombre": mueble.nombre,
        "ancho": mueble.ancho,
        "largo": mueble.largo,
        "alto": mueble.alto,
        "utilidad": mueble.utilidad,
        "uso": mueble.uso,
        "posicion": punto_a_diccionario(mueble.posicion)
    }


def habitacion_a_diccionario(habitacion):
    muebles = []

    #para cada mueble...
    for mueble in habitacion.get_muebles():
        muebles.append(mueble_a_diccionario(mueble))

    return {
        "nombre": habitacion.get_nombre(),
        "ancho": habitacion.get_ancho(),
        "largo": habitacion.get_largo(),
        "alto": habitacion.get_alto(),
        "muebles": muebles
    }


# Guardar un Proyecto

def guardar_proyecto(habitacion, nombre_archivo):
    #Guarda los datos en un archivo JSON, con habitación y nombre de archivo.
    #W permite crear o sobreescribir el archivo
    datos = habitacion_a_diccionario(habitacion)

    #Abrir el archivo y escribir los datos
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print(f"Proyecto guardado correctamente en: {nombre_archivo}")


# De diccionarios a objetos

def diccionario_a_punto(datos):
    return Punto3D(
        datos["x"],
        datos["y"],
        datos["z"]
    )


def diccionario_a_mueble(datos):
    #Reconstruir muebles
    posicion = diccionario_a_punto(datos["posicion"])

    return Mueble(
        datos["nombre"],
        datos["ancho"],
        datos["largo"],
        datos["alto"],
        datos["utilidad"],
        posicion,
        datos["uso"]
    )


def diccionario_a_habitacion(datos):
    #Crea una habitación vacía
    habitacion = Habitacion(
        datos["nombre"],
        datos["ancho"],
        datos["largo"],
        datos["alto"]
    )

    #y agrega cada mueble
    for datos_mueble in datos["muebles"]:
        mueble = diccionario_a_mueble(datos_mueble)
        habitacion.agregar_mueble(mueble)

    return habitacion


# Cargar Proyecto

def cargar_proyecto(nombre_archivo):
    #Cargar un archivo JSON
    try:
        #Abrir el archivo JSON para lectura
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            #Reconstruir los objetos EasySpacey
        habitacion = diccionario_a_habitacion(datos)

        print(f"Proyecto cargado correctamente desde: {nombre_archivo}")

        return habitacion

    #A menos que no lo encuentre
    except FileNotFoundError:
        print("Error: No se encontro el archivo.")
        return None

    #O que no cumpla con el formato
    except json.JSONDecodeError:
        print("Error: El archivo JSON no tiene un formato valido.")
        return None


# PRUEBA

if __name__ == "__main__":

    # Crear habitacion
    habitacion = Habitacion(
        "Mi cuarto",
        5,
        4,
        3
    )

    # Crear cama
    cama = Mueble(
        "Cama",
        2.0,
        1.5,
        0.6,
        10,
        Punto3D(1, 1, 0),
        "Dormir"
    )

    # Crear escritorio
    escritorio = Mueble(
        "Escritorio",
        1.2,
        0.6,
        0.75,
        8,
        Punto3D(3, 2, 0),
        "Trabajar/Estudiar"
    )

    # Agregar muebles a la habitacion
    habitacion.agregar_mueble(cama)
    habitacion.agregar_mueble(escritorio)

    # Mostrar datos originales
    print("\n===== DATOS ORIGINALES =====")
    print(habitacion)

    for mueble in habitacion.get_muebles():
        print(mueble)

    # Guardar
    guardar_proyecto(
        habitacion,
        "mi_cuarto.json"
    )

    # Cargar
    habitacion_cargada = cargar_proyecto(
        "mi_cuarto.json"
    )

    # Mostrar lo recuperado
    if habitacion_cargada is not None:

        print("\n===== DATOS RECUPERADOS =====")
        print(habitacion_cargada)

        for mueble in habitacion_cargada.get_muebles():
            print(mueble)