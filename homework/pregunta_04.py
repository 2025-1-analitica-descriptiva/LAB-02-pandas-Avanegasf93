"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    ruta_archivo = "files/input/tbl0.tsv"  # Ruta relativa del archivo a procesar
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")  # Leemos el archivo TSV separando por tabulador
    promedio = tbl0.groupby("c1")["c2"].mean()  # Agrupamos por 'c1' y calculamos promedio de 'c2'
    return promedio  # Retornamos los valores promedio por grupo

print(pregunta_04())  # Muestra los resultados
