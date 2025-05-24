"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos la librería pandas

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    ruta_archivo = "files/input/tbl1.tsv"  # Definimos la ruta al archivo (es .tsv, no .csv)
    tbl1 = pd.read_csv(ruta_archivo, sep="\t")  # Leemos el archivo TSV como DataFrame
    unicos = tbl1["c4"].str.upper().unique()  # Convertimos a mayúsculas y obtenemos los valores únicos
    lista_ordenada = sorted(unicos)  # Ordenamos alfabéticamente la lista
    return lista_ordenada  # Retornamos la lista final

print(pregunta_06())  # Imprimimos el resultado de la función
