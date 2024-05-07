import sqlite3
from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Maestro import Maestro


class MaestroDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def crear(self, teacher):
        query = "INSERT INTO maestros (maestro_id, grupo) VALUES (?, ?)"
        try:
            self.cursor.execute(
                query,
                (
                    teacher.get_maestro_id(),
                    teacher.get_grupo(),
                ),
            )
            self.con.commit()
            return True  # Retorna True si la inserción es exitosa
        except sqlite3.Error as e:
            # Captura el error específico y retorna su mensaje como string
            error_message = str(e)
            print(f"Error al registrar el profesor: {error_message}")
            return False  # Retorna False en caso de error
        finally:
            self.close()

    def listar(self):
        query = "SELECT * FROM maestros"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                maestro_obj = Maestro(
                    row[0], row[1]
                )  # Asegúrate de que Maestro tenga un constructor que acepte los valores de row
                resultados.append(maestro_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar profesores: {e}")
            return []

    def modificar(self, teacher):
        query = "UPDATE maestros SET grupo = ? WHERE maestro_id = ?"
        try:
            self.cursor.execute(
                query,
                (
                    teacher.get_grupo(),
                    teacher.get_maestro_id(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar el profesor: {e}")
            return False
        finally:
            self.close()
            return True

    def eliminar(self, teacher):
        query = "DELETE FROM maestros WHERE maestro_id = ?"
        try:
            self.cursor.execute(query, (teacher.get_maestro_id(),))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar el profesor: {e}")
            return False
        finally:
            self.close()
            return True
