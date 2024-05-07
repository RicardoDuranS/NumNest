import sqlite3

# Full path where the database will be created (if it doesn't exist, it will be created)
ruta_db = "DB/aventuraMatematica.db"

# Create the connection to the database (if it doesn't exist, it will be created)
conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Creation of the Users table
cursor.execute(
    "CREATE TABLE usuarios (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario VARCHAR(50) UNIQUE, contrasena VARCHAR(16), genero VARCHAR(10))"
)

# Creation of the Groups table
cursor.execute(
    "CREATE TABLE grupos (grupo_id INTEGER PRIMARY KEY UNIQUE, ano_escolar INT)"
)

# Creation of the Teachers table
cursor.execute(
    "CREATE TABLE maestros (maestro_id INTEGER PRIMARY KEY UNIQUE, grupo INTEGER, FOREIGN KEY (maestro_id) REFERENCES usuarios (usuario_id), FOREIGN KEY (grupo) REFERENCES grupos (grupo_id))"
)

# Creation of the Students table
cursor.execute(
    "CREATE TABLE estudiantes (estudiante_id INTEGER PRIMARY KEY UNIQUE, listnum INTEGER , grupo INTEGER, progreso INTEGER DEFAULT 1, FOREIGN KEY (estudiante_id) REFERENCES usuarios (usuario_id), FOREIGN KEY (grupo) REFERENCES grupos (grupo_id))"
)

# Creation of the Worlds table
cursor.execute(
    "CREATE TABLE mundos (mundo_id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_mundo VARCHAR(50) UNIQUE)"
)

# Creation of the Levels table
cursor.execute(
    "CREATE TABLE niveles (nivel_id INTEGER PRIMARY KEY, nombre_mundo VARCHAR(50), dificultad INTEGER, FOREIGN KEY (nombre_mundo) REFERENCES mundos(nombre_mundo))"
)

# Creation of the Scores table
cursor.execute(
    "CREATE TABLE puntajes (puntaje_id INTEGER PRIMARY KEY AUTOINCREMENT, nivel_id INTEGER, estudiante_id INTEGER, fecha TEXT DEFAULT (datetime('now')), valor INTEGER, FOREIGN KEY (nivel_id) REFERENCES niveles (nivel_id), FOREIGN KEY (estudiante_id) REFERENCES estudiantes (estudiante_id))"
)

# Save changes and close the connection
conexion.commit()
conexion.close()

print("Database created and tables created successfully.")
