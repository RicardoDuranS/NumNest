import sqlite3

# Establecer una conexión a la base de datos
conexion = sqlite3.connect("DB/aventuraMatematica.db")
cursor = conexion.cursor()

mundos = ["Mundo1", "Mundo2", "Mundo3", "Mundo4"]

# Insertar los mundos en la tabla
for mundo in mundos:
    cursor.execute(
        "INSERT INTO mundos (nombre_mundo) VALUES (?)", (mundo,)
    )  # Usar una tupla como argumento

# Lista de mundos y dificultades
niveles = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 1),
    (2, 2),
    (2, 3),
    (3, 1),
    (3, 2),
    (3, 3),
    (4, 1),
    (4, 2),
    (4, 3),
]

# Insertar los niveles en la tabla niveles
for mundo, dificultad in niveles:
    cursor.execute(
        "INSERT INTO niveles (nombre_mundo, dificultad) VALUES (?, ?)",
        (mundo, dificultad),
    )
conexion.commit()
conexion.close()

print("Datos de puntajes, mundos y niveles insertados correctamente.")
