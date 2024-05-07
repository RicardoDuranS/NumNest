from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.EstudianteDAO import EstudianteDAO


class EstudianteController:
    def __init__(self):
        factory = ConnectionFactory()
        self.estudianteDAO = EstudianteDAO(factory)

    def validar(self, student):
        var = self.estudianteDAO.validar(student)
        if isinstance(var, dict):
            # Si var es un diccionario, significa que el estudiante es válido
            print("Estudiante valido:", var)
            return var
        else:
            # Si var no es un diccionario, significa que el estudiante no es válido
            return {"message": "Usuario no valido"}

    def listarEstudiantes(self):
        resultados = self.estudianteDAO.listar()
        resultados_dict = [estudiante.serialize() for estudiante in resultados]
        return resultados_dict

    def listarEstudiantesGenero(self):
        resultados = self.estudianteDAO.listarPorGenero()
        return resultados

    def crearEstudiante(self, estudiante):
        resultado = self.estudianteDAO.crear(estudiante)
        if resultado is True:
            return {"message": "Creación de estudiante"}
        else:
            # Imprime el mensaje de error si hay uno
            print(resultado)
            return {"message": resultado}

    def modificarProgreso(self, estudiante):
        resultado = self.estudianteDAO.modificar(estudiante)
        if resultado is True:
            return {"message": "Modificación exitosa"}
        else:
            # Imprime el mensaje de error si hay uno
            print(resultado)
            return {"message": resultado}

    def modificarEstudiante(self, estudiante):
        resultado = self.estudianteDAO.modificarEstudiante(estudiante)
        if resultado is True:
            return {"message": True}
        else:
            # Imprime el mensaje de error si hay uno
            print(resultado)
            return {"message": resultado}

    def estadisticas_globales(self):
        result = self.estudianteDAO.cantidad_estudiantes_activos_y_registrados()
        return result

    def datos_de_estudiante(self, estudiante):
        estudiante_info = self.estudianteDAO.estudiante_info(estudiante)
        return estudiante_info

    def puntajes_de_estudiante(self, estudiante):
        estudiante_scores = self.estudianteDAO.estudiante_scores(estudiante)
        return estudiante_scores
