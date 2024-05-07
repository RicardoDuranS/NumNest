class Mundo:
    def __init__(self, mundo_id=None, nombre_mundo=None):
        self.mundo_id = mundo_id
        self.nombre_mundo = nombre_mundo

    # Métodos getters
    def get_mundo_id(self):
        return self.mundo_id

    def get_nombre_mundo(self):
        return self.nombre_mundo

    # Métodos setters
    def set_mundo_id(self, mundo_id):
        self.mundo_id = mundo_id

    def set_nombre_mundo(self, nombre_mundo):
        self.nombre_mundo = nombre_mundo

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Mundo(mundo_id={self.mundo_id}, nombre_mundo={self.nombre_mundo})"
