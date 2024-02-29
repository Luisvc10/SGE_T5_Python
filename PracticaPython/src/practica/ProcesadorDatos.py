'''
Created on 20 feb 2024

@author: luigi
'''
# Importamos los módulos necesarios

import random  # Para generar números aleatorios
import numpy as np  # Para realizar cálculos estadísticos

# Definimos una clase llamada ProcesadorArchivo
class ProcesadorArchivo:
    def __init__(self):
        self.nombre_archivo = ""  # Inicializamos el nombre del archivo como una cadena vacía

    # Método para generar el archivo con datos aleatorios
    def generar_archivo(self):
        # Solicitamos al usuario el nombre del archivo de texto
        self.nombre_archivo = input("Ingrese el nombre del archivo de texto: ")

        # Solicitamos al usuario las características y sus rangos de valores permitidos
        caracteristicas = []
        for i in range(5):
            nombre_caracteristica = input("Ingrese el nombre de la característica {}: ".format(i+1))
            min_valor = float(input("Ingrese el valor mínimo para la característica {}: ".format(nombre_caracteristica)))
            max_valor = float(input("Ingrese el valor máximo para la característica {}: ".format(nombre_caracteristica)))
            caracteristicas.append((nombre_caracteristica, min_valor, max_valor))

        # Generamos el archivo con 1000 registros aleatorios
        with open(self.nombre_archivo, 'w') as f:
            # Escribimos los nombres de las características en el archivo separados por tabulaciones
            for caracteristica in caracteristicas:
                f.write(caracteristica[0] + "\t")
            f.write("\n")

            # Generamos 1000 registros aleatorios
            for _ in range(1000):
                for caracteristica in caracteristicas:
                    min_valor = caracteristica[1]
                    max_valor = caracteristica[2]
                    valor_aleatorio = random.uniform(min_valor, max_valor)  # Generamos un valor aleatorio dentro del rango
                    f.write(str(valor_aleatorio) + "\t")  # Escribimos el valor en el archivo
                f.write("\n")  # Agregamos una nueva línea para cada registro

        print("Archivo generado exitosamente: {}".format(self.nombre_archivo))

    # Método para analizar el archivo generado
    def analizar_archivo(self):
        # Cerramos el archivo antes de analizarlo para asegurarnos de que no esté siendo utilizado
        if not self.nombre_archivo:
            print("No se ha generado ningún archivo para analizar.")
            return

        # Cargamos el archivo y leemos los datos
        with open(self.nombre_archivo, 'r') as f:
            # Leemos la primera línea que contiene los nombres de las características
            line = f.readline()
            nombres_caracteristicas = line.strip().split("\t")

            # Leemos el resto del archivo y almacenamos los datos en una lista de listas
            datos = []
            for line in f:
                datos.append([float(x) for x in line.strip().split("\t")])

        # Calculamos las estadísticas para cada característica
        for i, caracteristica in enumerate(nombres_caracteristicas):
            valores = np.array([fila[i] for fila in datos])  # Extraemos los valores de la característica actual
            media = np.mean(valores)  # Calculamos la media de los valores
            moda = np.argmax(np.bincount(valores.astype(int)))  # Calculamos la moda de los valores
            maximo = np.max(valores)  # Encontramos el valor máximo
            minimo = np.min(valores)  # Encontramos el valor mínimo
            varianza = np.var(valores)  # Calculamos la varianza de los valores

            # Imprimimos las estadísticas para la característica actual
            print("\nEstadísticas para la característica {}: ".format(caracteristica))
            print("Media:", media)
            print("Moda:", moda)
            print("Máximo:", maximo)
            print("Mínimo:", minimo)
            print("Varianza:", varianza)


# Instanciamos la clase ProcesadorArchivo
procesador = ProcesadorArchivo()

# Llamamos al método generar_archivo para crear el archivo con datos aleatorios
procesador.generar_archivo()

# Llamamos al método analizar_archivo para analizar los datos del archivo generado
procesador.analizar_archivo()