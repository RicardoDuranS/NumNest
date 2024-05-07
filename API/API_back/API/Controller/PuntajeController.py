from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.PuntajeDAO import PuntajeDAO
from API.Modelo.Puntaje import Puntaje


class PuntajeController:
    def __init__(self):
        factory = ConnectionFactory()
        self.puntajeDAO = PuntajeDAO(factory)

    def registrarPuntaje(self, score):
        var = self.puntajeDAO.crear(score)
        if var:
            return {"message": "Score Registrado Exitosamente"}
        else:
            return {"message": "Error al registrar Score"}

    def ultimoPuntaje(self, estudiante_id, nivel_id):
        var = self.puntajeDAO.ultimo(estudiante_id, nivel_id)
        return {"message": var}


from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.PuntajeDAO import PuntajeDAO
from API.Modelo.Puntaje import Puntaje


class PuntajeController:
    def __init__(self):
        factory = ConnectionFactory()
        self.puntajeDAO = PuntajeDAO(factory)

    def registrarPuntaje(self, score):
        var = self.puntajeDAO.crear(score)
        if var:
            return {"message": "Score Registrado Exitosamente"}
        else:
            return {"message": "Error al registrar Score"}

    def ultimoPuntaje(self, estudiante_id, nivel_id):
        var = self.puntajeDAO.ultimo(estudiante_id, nivel_id)
        return {"message": var}

    def top_puntajes(self):
        var = self.puntajeDAO.listar_top_puntajes()
        return var

    def listarPuntajes(self):
        var = self.puntajeDAO.listar()
        resultados_dict = [puntaje.serialize() for puntaje in var]
        return resultados_dict

    def top_puntajes(self):
        var = self.puntajeDAO.listar_top_puntajes()
        return var

    def listarPuntajes(self):
        var = self.puntajeDAO.listar()
        resultados_dict = [puntaje.serialize() for puntaje in var]
        return resultados_dict
