"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd  # Importamos pandas para manipular datos

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    ruta_archivo = "files/input/tbl1.tsv"  # Definimos la ruta del archivo
    tbl1 = pd.read_csv(ruta_archivo, sep="\t")  # Leemos el archivo TSV como un DataFrame
    agrupado = tbl1.groupby("c0")["c4"].apply(lambda x: ",".join(sorted(x)))  # Agrupamos por 'c0' y unimos los valores de 'c4' ordenados
    return agrupado.reset_index()  # Convertimos la Serie a DataFrame y restauramos el índice

print(pregunta_11())  # Mostramos la tabla resultante

