class Nivel:
    def __init__(self, nivel_id=None, nombre_mundo=None, dificultad=None):
        self.nivel_id = nivel_id
        self.nombre_mundo = nombre_mundo
        self.dificultad = dificultad

    # Métodos getters
    def get_nivel_id(self):
        return self.nivel_id

    def get_nombre_mundo(self):
        return self.nombre_mundo

    def get_dificultad(self):
        return self.dificultad

    # Métodos setters
    def set_nivel_id(self, nivel_id):
        self.nivel_id = nivel_id

    def set_nombre_mundo(self, nombre_mundo):
        self.nombre_mundo = nombre_mundo

    def set_dificultad(self, dificultad):
        self.dificultad = dificultad

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Nivel(nivel_id={self.nivel_id}, nombre_mundo={self.nombre_mundo}, dificultad={self.dificultad})"
