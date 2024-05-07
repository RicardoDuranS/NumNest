from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.MaestroDAO import MaestroDAO


class MaestroController:
    def __init__(self):
        factory = ConnectionFactory()
        self.maestroDAO = MaestroDAO(factory)

    def crearMaestro(self, maestro):
        resultado = self.maestroDAO.crear(maestro)
        if resultado is True:
            return {"message": "ok"}
        else:
            # Imprime el mensaje de error si hay uno
            return {"message": resultado}

    def listarMaestros(self):
        resultados = self.maestroDAO.listar()
        resultados_dict = [maestro.serialize() for maestro in resultados]
        return resultados_dict

    def modificarMaestro(self, maestro):
        resultados = self.maestroDAO.modificar(maestro)
        return {"message": resultados}
