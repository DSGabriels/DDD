from DestinoRepository import DestinoRepository
from Destino import Destino


class InterfaceUser:
    def __init__(self, destino_repository: DestinoRepository) -> None:
        self.destino_repository = destino_repository

    def get_user_input(self):
        result = int(input(
            "Informe um DDD\n"))
        return result

    def show_destinies(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        catalogo = formatText.format("DDD", "Destino")

        for destino in self.destino_repository.lista_destino:
            catalogo += formatText.format(destino.ddd, destino.destino)

        return catalogo

    def user_output(self):
        ddd = self.get_user_input()
        if (not self.destino_repository.obter_destino_pelo_ddd(ddd)):
            print("DDD inexistente")
            return False

        print(f"Destino: {self.destino_repository.obter_destino_pelo_ddd(ddd)}")
        return True
