from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Estudiante import Estudiante
from API.Modelo.Puntaje import Puntaje

import sqlite3


class EstudianteDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def crear(self, estudiante):
        query = "INSERT INTO estudiantes (estudiante_id, listnum, grupo) VALUES (?, ?, ?, ?)"
        try:
            self.cursor.execute(
                query,
                (
                    estudiante.get_estudiante_id(),
                    estudiante.get_listNum(),
                    estudiante.get_grupo(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            error_message = str(e)
            print(f"Error al registrar el profesor: {error_message}")
            return error_message
        finally:
            self.close()
            return True

    def listar(self):
        query = "SELECT * FROM estudiantes"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                estudiante_obj = Estudiante(row[0], row[1], row[2], row[3])
                resultados.append(estudiante_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar estudiantes: {e}")
            return []

    def modificar(self, estudiante):
        query = "UPDATE estudiantes SET progreso = ? WHERE estudiante_id = ?"
        try:
            self.cursor.execute(
                query,
                (
                    estudiante.get_progreso(),
                    estudiante.get_estudiante_id(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar el estudiante: {e}")
            return False
        finally:
            self.close()
            return True

    def modificarEstudiante(self, estudiante):
        query = "UPDATE estudiantes SET listNum = ?, grupo = ? WHERE estudiante_id = ?"
        try:
            self.cursor.execute(
                query,
                (
                    estudiante.get_listNum(),
                    estudiante.get_grupo(),
                    estudiante.get_estudiante_id(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar el estudiante: {e}")
            return False
        finally:
            self.close()
            return True

    def eliminar(self, estudiante):
        query = "DELETE FROM estudiantes WHERE estudiante_id = ?"
        try:
            self.cursor.execute(query, (estudiante.get_estudiante_id(),))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar el estudiante: {e}")
            return False
        finally:
            self.close()
            return True

    def validar(self, estudiante):
        query = "SELECT estudiante_id, listNum, grupo, progreso FROM estudiantes WHERE listNum = ? AND grupo = ?"
        try:
            self.cursor.execute(
                query, (estudiante.get_listNum(), estudiante.get_grupo())
            )
            result = self.cursor.fetchone()
            if result is None:
                print("Estudiante no encontrado o contraseña incorrecta.")
                return False
            else:
                # Convertir el resultado en un diccionario con claves específicas
                estudiante_dict = {
                    "user_id": result[0],
                    "listNum": result[1],
                    "grupo": result[2],
                    "progreso": result[3],
                }
                return estudiante_dict
        except sqlite3.Error as e:
            print(f"Error al validar el estudiante: {e}")
            return False
        finally:
            self.close()

    def listarPorGenero(self):
        query = """
            SELECT
                SUM(CASE WHEN usuarios.genero = 'M' THEN 1 ELSE 0 END) AS Masculinos,
                SUM(CASE WHEN usuarios.genero = 'F' THEN 1 ELSE 0 END) AS Femeninas
            FROM
                usuarios
            LEFT JOIN
                maestros ON usuarios.usuario_id = maestros.maestro_id
            WHERE
                maestros.maestro_id IS NULL;
            """
        try:
            self.cursor.execute(query)
            resultados = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar estudiantes: {e}")
            return []

    def cantidad_estudiantes_activos_y_registrados(self):
        query = """
            SELECT
                (SELECT COUNT(*) FROM estudiantes) AS total_estudiantes,
                (SELECT COUNT(DISTINCT estudiante_id) FROM puntajes
                WHERE fecha BETWEEN date('now', '-7 days') AND date('now')) AS estudiantes_con_puntaje
        """
        try:
            self.cursor.execute(query)
            resultados = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al retornar estadisticas de estudiantes: {e}")
            return []

    def estudiante_info(self, estudiante):
        # Consulta SQL para seleccionar información específica del estudiante
        query = """
            SELECT * FROM estudiantes
            WHERE estudiante_id = ?
        """
        try:
            self.cursor.execute(query, (estudiante.get_estudiante_id(),))
            resultados = self.cursor.fetchone()
            # Verifica si resultados es None antes de intentar crear una instancia de Estudiante
            if resultados is None:
                print("No se encontraron resultados para el estudiante.")
                return None
            # Convertir el resultado en un objeto Estudiante deserializado
            estudiante_obj = Estudiante(*resultados)
            return estudiante_obj
        except Exception as e:
            print(f"Error al retornar la info del estudiante: {e}")
            return None
        finally:
            self.close()

    def estudiante_scores(self, estudiante):
        # Consulta SQL para seleccionar los scores del estudiante
        query = """
            SELECT * FROM puntajes
            WHERE estudiante_id =?
        """
        try:
            self.cursor.execute(query, (estudiante.get_estudiante_id(),))
            resultados = self.cursor.fetchall()
            self.close()
            # Convertir cada fila de resultados en un objeto Puntaje deserializado
            scores = [Puntaje(*row) for row in resultados]
            return scores
        except Exception as e:
            print(f"Error al retornar los scores del estudiante: {e}")
            return []
