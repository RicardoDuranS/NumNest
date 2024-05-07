from API.ConnectionFactory.ConnectionFactory import ConnectionFactory
from API.DAO.NivelDAO import NivelDAO


class NivelController:
    def __init__(self):
        factory = ConnectionFactory()
        self.nivelDAO = NivelDAO(factory)
