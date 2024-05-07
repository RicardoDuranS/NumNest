from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Puntaje import Puntaje
import sqlite3


class PuntajeDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def crear(self, puntaje):
        query = (
            "INSERT INTO puntajes (nivel_id, estudiante_id, valor) VALUES ( ?, ?, ?)"
        )
        try:
            self.cursor.execute(
                query,
                (
                    puntaje.get_nivel_id(),
                    puntaje.get_estudiante_id(),
                    puntaje.get_valor(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al registrar el puntaje: {e}")
            return False
        finally:
            self.close()
            return True

    def listar(self):
        query = "SELECT * FROM puntajes"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                puntaje_obj = Puntaje(*row)
                resultados.append(puntaje_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar puntajes: {e}")
            return []

    def eliminar(self, puntaje):
        query = "DELETE FROM puntajes WHERE puntaje_id = ?"
        try:
            self.cursor.execute(query, (puntaje.get_puntaje_id(),))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar el puntaje: {e}")
            return False
        finally:
            self.close()
            return True

    def ultimo(self, estudiante_id, nivel_id):
        query = """
        SELECT valor FROM puntajes
        WHERE estudiante_id = ? AND nivel_id = ?
        ORDER BY fecha DESC, puntaje_id DESC
        LIMIT 1
        """
        try:
            self.cursor.execute(query, (estudiante_id, nivel_id))
            row = self.cursor.fetchone()
            if row is None:
                return (
                    -1
                )  # No hay puntajes registrados para el estudiante y nivel especificados
            else:
                return row[0]  # Retorna el valor del último puntaje
        except sqlite3.Error as e:
            error_message = str(e)  # Convertir el objeto de error en un string
            print(f"Error al obtener el último puntaje: {error_message}")
            return error_message  # Retorna el mensaje de error como string
        finally:
            self.close()

    def listar_top_puntajes(self):
        # Consulta SQL modificada para sumar los puntuajes por alumno y ordenar por la suma total
        query = """
        SELECT estudiantes.estudiante_id, usuarios.nombre_usuario, SUM(puntajes.valor) as total_puntaje
        FROM estudiantes
        JOIN usuarios ON estudiantes.estudiante_id = usuarios.usuario_id
        JOIN puntajes ON estudiantes.estudiante_id = puntajes.estudiante_id
        GROUP BY estudiantes.estudiante_id, usuarios.nombre_usuario
        ORDER BY total_puntaje DESC
        LIMIT 5
        """
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                # Crear un diccionario con el ID del alumno, el nombre y la suma total de sus puntuajes
                top_puntaje = {
                    "estudiante_id": row[0],
                    "nombre_usuario": row[1],
                    "valor": row[2],
                }
                resultados.append(top_puntaje)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar niveles: {e}")
            return []
