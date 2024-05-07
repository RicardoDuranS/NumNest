class Grupo:
    def __init__(self, grupo_id=None, ano_escolar=None):
        self.grupo_id = grupo_id
        self.ano_escolar = ano_escolar

    # Métodos getters
    def get_grupo_id(self):
        return self.grupo_id

    def get_ano_escolar(self):
        return self.ano_escolar

    # Métodos setters
    def set_grupo_id(self, grupo_id):
        self.grupo_id = grupo_id

    def set_ano_escolar(self, ano_escolar):
        self.ano_escolar = ano_escolar

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Grupo(grupo_id={self.grupo_id}, ano_escolar={self.ano_escolar})"
