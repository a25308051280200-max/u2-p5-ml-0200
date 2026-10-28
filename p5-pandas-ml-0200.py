import numpy as np 
import pandas as pd 

# Alejandra Rivera Valenzuela NC 0200
## datos matriz ()

datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# poner nombre a las columnas 
# y almacenar la tabla en la variable df dataframe
print("--- datos a partir de una materix 4x3 ---")
df = pd.DataFrame(datos_alumno, columns=['ci', 'marcas', 'paquete'])
print(df)

# datos a partir de un diccionario 
print("--- datos a partir de un diccionario ---")
alumno_diccionario = {
    "nombre": ["Abril", "Nicole", "Maria", "Alejandra", "Matias", "Barbara"],
    "califa": [60, 90, 100, 80, 70, 50],
    "edad": [64, 15, 16, 16, 18, 14]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)
print("Alejandra Rivera Valenzuela NC = 0200")