class Usuario:
    def __init__(
        self, usuario_id=None, nombre_usuario=None, contrasena=None, genero=None
    ):
        self.usuario_id = usuario_id
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.genero = genero

    # Métodos getters
    def get_usuario_id(self):
        return self.usuario_id

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_contrasena(self):
        return self.contrasena

    def get_genero(self):
        return self.genero

    # Métodos setters
    def set_usuario_id(self, usuario_id):
        self.usuario_id = usuario_id

    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def set_genero(self, genero):
        self.genero = genero

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Usuario(usuario_id={self.usuario_id}, nombre_usuario={self.nombre_usuario}, genero={self.genero})"
