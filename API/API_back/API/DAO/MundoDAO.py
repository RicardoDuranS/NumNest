from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Usuario import Usuario
import sqlite3


class MundoDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def lista_stadistica_mundos_completados(self):
        query = """
            SELECT
                CASE
                    WHEN estudiantes.progreso BETWEEN 1 AND 3 THEN 1
                    WHEN estudiantes.progreso BETWEEN 4 AND 6 THEN 2
                    WHEN estudiantes.progreso BETWEEN 7 AND 9 THEN 3
                    WHEN estudiantes.progreso BETWEEN 10 AND 12 THEN 4
                END AS Mundo,
                COUNT(*) AS CantidadEstudiantes
            FROM
                estudiantes
            GROUP BY
                Mundo;
            """
        try:
            self.cursor.execute(query)
            resultados = self.cursor.fetchall()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar los mundos: {e}")
            return []
