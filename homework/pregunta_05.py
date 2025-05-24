"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos la librería pandas para análisis de datos

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
    """
    ruta_archivo = "files/input/tbl0.tsv"  # Definimos la ruta del archivo de entrada
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")  # Leemos el archivo TSV como un DataFrame
    maximos = tbl0.groupby("c1")["c2"].max()  # Agrupamos por 'c1' y obtenemos el valor máximo de 'c2'
    return maximos  # Retornamos los valores máximos agrupados por letra

print(pregunta_05())  # Mostramos en consola el resultado al ejecutar la función
