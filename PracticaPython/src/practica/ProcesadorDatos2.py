import math
import random

from collections import Counter

# Definición de variables
nombre_fichero = "futbolistas.txt"

# Definición de funciones
def cargar_datos(fichero):
    with open(fichero, "r") as f:
        next(f)  # Skip the first line (assuming it's header)
        datos = [list(map(int, linea.split())) for linea in f]
    return datos

def calcular_media(datos, caracteristica):
    return sum(valor[caracteristica] for valor in datos) / len(datos)

def calcular_moda(datos, caracteristica):
    valores = [valor[caracteristica] for valor in datos]
    conteo = Counter(valores)
    moda = max(conteo, key=conteo.get)
    return moda

def calcular_maximo(datos, caracteristica):
    return max(valor[caracteristica] for valor in datos)

def calcular_minimo(datos, caracteristica):
    return min(valor[caracteristica] for valor in datos)

def calcular_varianza(datos, caracteristica):
    media = calcular_media(datos, caracteristica)
    varianza = sum((valor[caracteristica] - media)**2 for valor in datos) / len(datos)
    return varianza

# Carga de datos
datos = cargar_datos(nombre_fichero)

# Cálculo de estadísticas
caracteristicas = ["Goles", "Pérdidas de balón en área propia",
                  "Pérdidas de balón en área contraria",
                  "Pases efectivos", "Pases fallados"]

estadisticas = {}
for caracteristica in caracteristicas:
    estadisticas[caracteristica] = {
        "media": calcular_media(datos, caracteristica),
        "moda": calcular_moda(datos, caracteristica),
        "maximo": calcular_maximo(datos, caracteristica),
        "minimo": calcular_minimo(datos, caracteristica),
        "varianza": calcular_varianza(datos, caracteristica),
    }

# Impresión de resultados
for caracteristica, valores in estadisticas.items():
    print("{}:".format(caracteristica))
    for nombre, valor in valores.items():
        print("    {}: {}".format(nombre, valor))