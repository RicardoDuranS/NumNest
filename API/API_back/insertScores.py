import sqlite3
import random
from datetime import datetime

# Establecer una conexión a la base de datos
conexion = sqlite3.connect("DB/aventuraMatematica.db")
cursor = conexion.cursor()

# Obtener los IDs de los estudiantes
cursor.execute("SELECT estudiante_id FROM estudiantes")
ids_estudiantes = cursor.fetchall()

# Iterar sobre los IDs de los estudiantes y generar scores
for estudiante_id in ids_estudiantes:
    for _ in range(2):  # Insertar al menos 2 scores para cada estudiante
        nivel_id = 1  # Nivel 1
        valor = random.randint(1, 50)  # Valor aleatorio entre 1 y 50

        # Insertar el score en la tabla puntajes
        cursor.execute(
            "INSERT INTO puntajes (nivel_id, estudiante_id, valor) VALUES ( ?, ?, ?)",
            (nivel_id, estudiante_id[0], valor),
        )

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Scores insertados exitosamente.")
