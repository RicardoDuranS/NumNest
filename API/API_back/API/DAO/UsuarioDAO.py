from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.Modelo.Usuario import Usuario
import sqlite3


class UsuarioDAO:
    def __init__(self, con):
        self.con = ConnectionFactory().getConnection()
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def crear(self, user):
        query = (
            "INSERT INTO usuarios (nombre_usuario, contrasena, genero) VALUES (?, ?, ?)"
        )
        try:
            self.cursor.execute(
                query,
                (
                    user.get_nombre_usuario(),
                    user.get_contrasena(),
                    user.get_genero(),
                ),
            )
            self.con.commit()
            # Obtener el ID del usuario recién creado
            user_id = self.cursor.lastrowid
            return user_id
        except sqlite3.Error as e:
            print(f"Error al registrar al usuario: {e}")
            return False
        finally:
            self.close()

    def listar(self):
        query = "SELECT * FROM usuarios"
        try:
            self.cursor.execute(query)
            resultados = []
            row = self.cursor.fetchone()
            while row is not None:
                user_obj = Usuario(*row)
                resultados.append(user_obj)
                row = self.cursor.fetchone()
            self.close()
            return resultados
        except Exception as e:
            print(f"Error al listar usuarios: {e}")
            return []

    def validar(self, usuario):
        query = "SELECT * FROM usuarios WHERE nombre_usuario = ? AND contrasena = ?"
        try:
            self.cursor.execute(
                query, (usuario.get_nombre_usuario(), usuario.get_contrasena())
            )
            result = self.cursor.fetchone()
            if result is None:
                print("Usuario no encontrado o contraseña incorrecta.")
                return False
            else:
                # Retornar el ID del usuario
                return result[
                    0
                ]  # Asume que el ID del usuario es el primer campo en el resultado
        except sqlite3.Error as e:
            print(f"Error al validar el usuario: {e}")
            return False
        finally:
            self.close()

    def tipo(self, usuario):
        # Consulta para verificar si el usuario existe en la tabla usuarios y si está registrado como estudiante
        query = """
        SELECT usuarios.nombre_usuario
        FROM usuarios
        INNER JOIN estudiantes ON usuarios.usuario_id = estudiantes.estudiante_id
        WHERE usuarios.nombre_usuario =?
        """
        try:
            self.cursor.execute(query, (usuario.get_nombre_usuario(),))
            result = self.cursor.fetchone()
            if result is None:
                print("Usuario no encontrado o no está registrado como estudiante.")
                return False
            else:
                # Si el usuario existe y está registrado como estudiante, retorna True
                return True
        except sqlite3.Error as e:
            print(
                f"Error al verificar si el usuario está registrado como estudiante: {e}"
            )
            return False
        finally:
            self.close()
