from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.MundoDAO import MundoDAO


class MundoController:
    def __init__(self):
        factory = ConnectionFactory()
        self.mundoDAO = MundoDAO(factory)

    def mundos_completados(self):
        resultados = self.mundoDAO.lista_stadistica_mundos_completados()
        cantidad_estudiantes_por_mundo = [0, 0, 0, 0]
        for row in resultados:
            # Asigna la cantidad de estudiantes al mundo correspondiente
            cantidad_estudiantes_por_mundo[row[0] - 1] = row[1]
        return cantidad_estudiantes_por_mundo
