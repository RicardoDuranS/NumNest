from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.UsuarioDAO import UsuarioDAO


class UsuarioController:
    def __init__(self):
        factory = ConnectionFactory()
        self.usuarioDAO = UsuarioDAO(factory)

    def validar(self, usuario):  # Que me retorne el id del usuario
        var = self.usuarioDAO.validar(usuario)
        try:
            if var:
                return {"usuario_id": var}
            else:
                return {"message": "Usuario no valido"}
        except Exception as e:
            print(f"Error al validar usuario: {e}")
            return {"error": "Error desconocido", "code": -1}

    def crearUsuario(self, usuario):
        try:
            user_id = self.usuarioDAO.crear(usuario)
            if user_id:
                # Si user_id es un valor verdadero (no False), retorna el ID del usuario
                return user_id
            else:
                # Si user_id es False, asumimos que hubo un error en la inserción
                return {
                    "error": "Error al crear el usuario en base de datos",
                    "code": -1,
                }
        except Exception as e:
            print(f"Error al crear usuario en base de datos: {e}")
            return {"error": "Error desconocido", "code": -1}

    def tipo(self, usuario):
        try:
            # Llamada a la función tipo en usuarioDAO
            user = self.usuarioDAO.tipo(usuario)

            # Verificación del resultado y construcción del mensaje
            if user:
                return {"usuario": "estudiante"}
            else:
                return {"usuario": "no estudiante"}
        except Exception as e:
            print(f"Error al crear usuario en base de datos: {e}")
            return {"error": "Error desconocido", "code": -1}
