import sqlite3

# Establecer una conexión a la base de datos
conexion = sqlite3.connect("DB/aventuraMatematica.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO grupos(grupo_id, ano_escolar) VALUES (1,1)")

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Accion ejecutada exitosamente.")
import secrets

# Genera una clave segura de 16 bytes
clave_secreta = secrets.token_bytes(16)

print(clave_secreta)
