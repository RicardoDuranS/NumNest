import sqlite3

# Establish a connection to the database
conexion = sqlite3.connect("DB/aventuraMatematica.db")
cursor = conexion.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


# Insertar usuarios (3 mujeres y 2 hombres)
usuarios = [
    ("Ana", "contraseña1", "F"),
    ("María", "contraseña2", "F"),
    ("Elena", "contraseña3", "F"),
    ("Juan", "contraseña4", "M"),
    ("Pedro", "contraseña5", "M"),
    ("Maestro1", "contraseña1", "M"),
    ("Maestra2", "contraseña2", "F"),
]

for user in usuarios:
    cursor.execute(
        "INSERT INTO usuarios (nombre_usuario, contrasena, genero) VALUES (?, ?, ?)",
        user,
    )
# Insertar grupos
grupos = [
    (331, 2022),  # Grupo con ID 1 y año escolar 2022
    (332, 2023),  # Grupo con ID 2 y año escolar 2023
    (333, 2024),  # Grupo con ID 3 y año escolar 2024
]

for grupo in grupos:
    cursor.execute("INSERT INTO grupos (grupo_id, ano_escolar) VALUES (?, ?)", grupo)

# Insertar maestros
maestros = [("Maestro1", 331), ("Maestra2", 333)]

i = 6
for maestro in maestros:
    cursor.execute(
        "INSERT INTO maestros (maestro_id, grupo) VALUES (?, ?)", (i, maestro[1])
    )
    i = i + 1


# Insertar estdiantes
estudiantes = [(1, 1, 331), (2, 2, 331), (3, 3, 331), (4, 1, 333), (5, 2, 333)]

grupos_id = [grupo[0] for grupo in cursor.execute("SELECT grupo_id FROM grupos")]

for estudiante in estudiantes:
    if estudiante[2] in grupos_id:
        cursor.execute(
            "INSERT INTO estudiantes(estudiante_id, listnum, grupo) VALUES (?, ?, ?)",
            estudiante,
        )
    else:
        print(f"Error: Grupo {estudiante[2]} not found")

conexion.commit()
conexion.close()

print("Data estudiantes, maestros, usuarios inserted successfully.")
