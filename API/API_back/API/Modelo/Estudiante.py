class Estudiante:
    def __init__(self, estudiante_id=None, listNum=None, grupo=None, progreso=None):
        self.estudiante_id = estudiante_id
        self.listNum = listNum
        self.grupo = grupo
        self.progreso = progreso

    # Métodos getters
    def get_estudiante_id(self):
        return self.estudiante_id

    def get_listNum(self):
        return self.listNum

    def get_grupo(self):
        return self.grupo

    def get_progreso(self):
        return self.progreso

    # Métodos setters
    def set_estudiante_id(self, estudiante_id):
        self.estudiante_id = estudiante_id

    def set_listNum(self, listNum):
        self.listNum = listNum

    def set_grupo(self, grupo):
        self.grupo = grupo

    def set_progreso(self, progreso):
        self.progreso = progreso

    # Sobrescribir el método __str__ para imprimir el objeto
    def __str__(self):
        return f"Estudiante(estudiante_id={self.estudiante_id}, listNum={self.listNum}, grupo={self.grupo}, progreso={self.progreso})"

    # Método para serializar el objeto a un diccionario
    def serialize(self):
        return {
            "estudiante_id": self.estudiante_id,
            "listNum": self.listNum,
            "grupo": self.grupo,
            "progreso": self.progreso,
        }
