from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Nivel import Nivel

import sqlite3


class NivelDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def registrar(self, level):
        query = "INSERT INTO Level (level_ID, world, difficulty, tries, unlocked) VALUES (?, ?, ?, ?, ?)"
        try:
            self.cursor.execute(
                query,
                (
                    level.get_level_ID(),
                    level.get_world(),
                    level.get_difficulty(),
                    level.get_tries(),
                    level.get_unlocked(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al registrar el nivel: {e}")
            return False
        finally:
            self.close()
            return True

    def listar(self):
        query = "SELECT * FROM Level"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                level_obj = Nivel(*row)
                resultados.append(level_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar niveles: {e}")
            return []

    def modificar(self, level):
        query = "UPDATE Level SET world = ?, difficulty = ?, tries = ?, unlocked = ? WHERE level_ID = ?"
        try:
            self.cursor.execute(
                query,
                (
                    level.get_world(),
                    level.get_difficulty(),
                    level.get_tries(),
                    level.get_unlocked(),
                    level.get_level_ID(),
                ),
            )
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al modificar el nivel: {e}")
            return False
        finally:
            self.close()
            return True

    def eliminar(self, level):
        query = "DELETE FROM Level WHERE level_ID = ?"
        try:
            self.cursor.execute(query, (level.get_level_ID(),))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error al eliminar el nivel: {e}")
            return False
        finally:
            self.close()
            return True


def nivel_de_mundo_desbloqueado(self, mundo, user):
    query = "SELECT MAX(Level) FROM Level WHERE World = ? AND Unlocked = 1"
    try:
        self.cursor.execute(query, (mundo,))
        max_level = self.cursor.fetchone()[0]
        self.close()
        return max_level
    except Exception as e:
        print(f"Error al listar niveles: {e}")
        return None
