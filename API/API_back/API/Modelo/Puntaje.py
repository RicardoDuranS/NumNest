class Puntaje:
    def __init__(
        self, puntaje_id=None, estudiante_id=None, nivel_id=None, fecha=None, valor=None
    ):
        self.puntaje_id = puntaje_id
        self.estudiante_id = estudiante_id
        self.nivel_id = nivel_id
        self.fecha = fecha
        self.valor = valor

    # Métodos getters
    def get_puntaje_id(self):
        return self.puntaje_id

    def get_estudiante_id(self):
        return self.estudiante_id

    def get_nivel_id(self):
        return self.nivel_id

    def get_fecha(self):
        return self.fecha

    def get_valor(self):
        return self.valor

    # Métodos setters
    def set_puntaje_id(self, puntaje_id):
        self.puntaje_id = puntaje_id

    def set_estudiante_id(self, estudiante_id):
        self.estudiante_id = estudiante_id

    def set_nivel_id(self, nivel_id):
        self.nivel_id = nivel_id

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_valor(self, valor):
        self.valor = valor

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Puntaje(puntaje_id={self.puntaje_id}, estudiante_id={self.estudiante_id}, nivel_id={self.nivel_id}, fecha={self.fecha}, valor={self.valor})"

    def serialize(self):
        return {
            "puntaje_id": self.puntaje_id,
            "estudiante_id": self.estudiante_id,
            "nivel_id": self.nivel_id,
            "fecha": self.fecha,
            "valor": self.valor,
        }
