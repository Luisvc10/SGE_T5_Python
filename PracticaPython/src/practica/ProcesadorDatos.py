# coding: utf-8
'''
Created on 20 feb 2024

@author: luigi
'''

# Importamos el módulo random para generar números aleatorios
import random

# Definimos una clase llamada ProcesadorArchivo
class ProcesadorArchivo:
    def __init__(self):
        # Método constructor de la clase
        # Inicializamos la variable nombre_archivo como una cadena vacía
        self.nombre_archivo = ""

    def generar_archivo(self):
        # Método para generar el archivo de datos
        # Solicitamos al usuario que ingrese el nombre del archivo de texto
        self.nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
        # Creamos una lista vacía para almacenar las características
        caracteristicas = []
        # Iteramos cinco veces para solicitar información sobre cada característica
        for i in range(5):
            # Solicitamos al usuario el nombre de la característica
            nombre_caracteristica = input("Ingrese el nombre de la característica {}: ".format(i+1))
            # Solicitamos al usuario el valor mínimo para la característica
            min_valor = float(input("Ingrese el valor mínimo para la característica {}: ".format(nombre_caracteristica)))
            # Solicitamos al usuario el valor máximo para la característica
            max_valor = float(input("Ingrese el valor máximo para la característica {}: ".format(nombre_caracteristica)))
            # Añadimos la característica a la lista de características como una tupla
            caracteristicas.append((nombre_caracteristica, min_valor, max_valor))

        # Abrimos el archivo en modo escritura ('w')
        with open(self.nombre_archivo, 'w') as f:
            # Escribimos los nombres de las características en la primera línea del archivo
            for caracteristica in caracteristicas:
                f.write(caracteristica[0] + "\t")
            # Escribimos un salto de línea para pasar a la siguiente fila
            f.write("\n")

            # Generamos 1000 filas de datos
            for _ in range(1000):
                # Para cada característica, generamos un valor aleatorio dentro del rango especificado
                for caracteristica in caracteristicas:
                    min_valor = caracteristica[1]
                    max_valor = caracteristica[2]
                    valor_aleatorio = random.uniform(min_valor, max_valor)
                    # Escribimos el valor aleatorio en el archivo seguido de un tabulador
                    f.write(str(valor_aleatorio) + "\t")
                # Escribimos un salto de línea para pasar a la siguiente fila
                f.write("\n")

        # Imprimimos un mensaje indicando que el archivo ha sido generado exitosamente
        print("Archivo generado exitosamente: {}".format(self.nombre_archivo))

    def analizar_archivo(self):
        # Método para analizar el archivo de datos
        # Verificamos si se ha generado algún archivo
        if not self.nombre_archivo:
            print("No se ha generado ningún archivo para analizar.")
            return

        # Abrimos el archivo en modo lectura ('r')
        with open(self.nombre_archivo, 'r') as f:
            # Leemos la primera línea para obtener los nombres de las características
            line = f.readline()
            nombres_caracteristicas = line.strip().split("\t")

            # Creamos una lista vacía para almacenar los datos
            datos = []
            # Iteramos sobre las líneas restantes del archivo
            for line in f:
                # Convertimos cada línea en una lista de valores separados por tabuladores
                datos.append([float(x) for x in line.strip().split("\t")])

        # Iteramos sobre los nombres de las características
        for i, caracteristica in enumerate(nombres_caracteristicas):
            # Extraemos los valores correspondientes a la característica actual
            valores = [fila[i] for fila in datos]
            # Calculamos la media de los valores
            media = sum(valores) / len(valores)
            # Calculamos la moda de los valores
            moda = max(set(valores), key=valores.count)
            # Encontramos el máximo valor
            maximo = max(valores)
            # Encontramos el mínimo valor
            minimo = min(valores)
            # Calculamos la varianza de los valores
            varianza = sum((x - media) ** 2 for x in valores) / len(valores)

            # Imprimimos las estadísticas para la característica actual
            print("\nEstadísticas para la característica {}: ".format(caracteristica))
            print("Media:", media)
            print("Moda:", moda)
            print("Máximo:", maximo)
            print("Mínimo:", minimo)
            print("Varianza:", varianza)

# Creamos una instancia de la clase ProcesadorArchivo
procesador = ProcesadorArchivo()
# Llamamos al método generar_archivo para generar el archivo de datos
procesador.generar_archivo()
# Llamamos al método analizar_archivo para analizar el archivo de datos generado
procesador.analizar_archivo()
