from Destino import Destino
class DestinoRepository:
    lista_destino: Destino = []

    def __init__(self) -> None:
        pass

    def set_catalog_item(self, destino: Destino) -> None:
        self.lista_destino.append(destino)

    def check_if_ddd_exists(self, ddd: Destino) -> bool:
        for item in self.lista_destino:
            if (ddd.ddd == item.ddd):
                return True

        return False

    def obter_destino_pelo_ddd(self,ddd):
        for item in self.lista_destino:
            if (ddd == item.ddd):
                return item.destino