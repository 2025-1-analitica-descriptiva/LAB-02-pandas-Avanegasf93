"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos pandas para el manejo de datos

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64
    """
    ruta_archivo = "files/input/tbl0.tsv"  # Define la ruta del archivo a analizar
    tbl0 = pd.read_csv(ruta_archivo, sep="\t")  # Carga el archivo TSV
    conteo = tbl0['c1'].value_counts()  # Cuenta cuántas veces aparece cada valor único en la columna 'c1'
    conteo = conteo.sort_index()  # Ordena los resultados alfabéticamente por índice (letra)
    return conteo  # Devuelve el conteo por letra

print(pregunta_03())  # Imprime el conteo
