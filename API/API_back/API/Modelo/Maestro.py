class Maestro:
    def __init__(self, maestro_id=None, grupo=None):
        self.maestro_id = maestro_id
        self.grupo = grupo

    # Métodos getters
    def get_maestro_id(self):
        return self.maestro_id

    def get_grupo(self):
        return self.grupo

    # Métodos setters
    def set_maestro_id(self, maestro_id):
        self.maestro_id = maestro_id

    def set_grupo(self, grupo):
        self.grupo = grupo

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Teacher(maestro_id={self.maestro_id}, grupo={self.grupo})"

        # Método para serializar el objeto a un diccionario

    def serialize(self):
        return {"maestro_id": self.maestro_id, "grupo": self.grupo}
