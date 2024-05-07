from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Grupo import Grupo
import sqlite3


class GrupoDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def listar(self):
        query = "SELECT * FROM grupos"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                school_group_obj = Grupo(*row)
                resultados.append(school_group_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar grupos escolares: {e}")
            return []

    def crear(self, grupo):
        query = "INSERT INTO grupos (grupo_id) VALUES (?)"
        try:
            # Ejecutar la consulta
            self.cursor.execute(
                query, (grupo.get_grupo_id(),)
            )  # Nota el uso de una tupla con una coma al final
            self.con.commit()
            self.close()
            return True
        except Exception as e:
            print(f"Error al registrar el grupo: {e}")
            return str(e)

    def eliminar(self, grupo):
        query = "DELETE FROM grupos WHERE grupo_id = ?"
        try:
            # Ejecutar la consulta
            self.cursor.execute(
                query, (grupo.get_grupo_id(),)
            )  # Nota el uso de una tupla con una coma al final
            self.con.commit()
            self.close()
            return True
        except Exception as e:
            print(f"Error al registrar el grupo: {e}")
            return str(e)
