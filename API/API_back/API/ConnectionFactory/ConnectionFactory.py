import sqlite3


class ConnectionFactory:
    def __init__(self):
        self.db_path = r"DB\aventuraMatematica.db"
        self.connection = None

    def getConnection(self):
        if self.connection is None:
            try:
                # Crear la conexión a la base de datos SQLite
                # Si el archivo no existe, SQLite lo creará automáticamente
                self.connection = sqlite3.connect(self.db_path)
                print("Conexión exitosa a la base de datos SQLite")
            except sqlite3.Error as e:
                print(f"Error al conectar a la base de datos SQLite: {e}")
        return self.connection
