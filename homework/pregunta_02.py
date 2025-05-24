"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos la librería pandas

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4
    """
    ruta_archivo = "files/input/tbl0.tsv"  # Ruta del archivo
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")  # Lee el archivo TSV
    return tbl0.shape[1]  # Retorna la cantidad de columnas (segundo valor de shape)

print(pregunta_02())  # Muestra el resultado
