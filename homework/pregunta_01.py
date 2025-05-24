"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos la librería pandas para el manejo de datos

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40
    """
    ruta_archivo = "files/input/tbl0.tsv"  # Define la ruta del archivo a leer
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")  # Lee el archivo TSV usando tabulador como separador
    return tbl0.shape[0]  # Retorna el número de filas (primer valor de la tupla shape)

print(pregunta_01())  # Imprime el resultado de la función