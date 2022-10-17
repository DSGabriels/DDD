from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUser import InterfaceUser

destino_repository = DestinoRepository()
destino_repository.set_catalog_item(Destino(18, "Araçatuba"))
destino_repository.set_catalog_item(Destino(24, "Angra dos Reis"))
destino_repository.set_catalog_item(Destino(75, "Feira de Santana"))
destino_repository.set_catalog_item(Destino(94, "Marabá"))
destino_repository.set_catalog_item(Destino(91, "Belém"))

user_interface = InterfaceUser(destino_repository)

print(user_interface.show_destinies())

user_interface.user_output()