from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.GrupoDAO import GrupoDAO


class GrupoController:
    def __init__(self):
        factory = ConnectionFactory()
        self.grupoDAO = GrupoDAO(factory)

    def listarGrupos(self):
        resultados = self.grupoDAO.listar()
        # Extrae los IDs de los grupos y los convierte en una lista de enteros
        ids_grupos = [grupo.grupo_id for grupo in resultados]
        return ids_grupos

    def agregarGrupo(self, grupo):
        resultados = self.grupoDAO.crear(grupo)
        return {"message": resultados}

    def eliminarGrupo(self, grupo):
        resultados = self.grupoDAO.eliminar(grupo)
        return {"message": resultados}
