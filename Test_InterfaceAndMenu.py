from DestinoRepository import DestinoRepository
from InterfaceUser import InterfaceUser
from Destino import Destino
import unittest
from unittest import mock

class TestDDDAplication(unittest.TestCase):
    def test_set_catalog_item(self):
        destino_repository = DestinoRepository()
        destino_repository.lista_destino = []
        destino1 = Destino(1, "Test 1")
        destino2 = Destino(2, "Test 2")
        destino3 = Destino(3, "Test 3")

        destino_repository.set_catalog_item(destino1)
        destino_repository.set_catalog_item(destino2)

        self.assertEquals(len(destino_repository.lista_destino), 2)
        self.assertFalse(destino3 in destino_repository.lista_destino)
        self.assertEquals(type(destino_repository.lista_destino), list)

    def test_check_if_DDD_exists(self):
        destino_repository = DestinoRepository()
        destino_repository.lista_destino = []
        destino1 = Destino(1, "Test 1")

        destino_repository.set_catalog_item(destino1)
        resultOK = destino_repository.check_if_ddd_exists(destino1)
        resultNOK = destino_repository.check_if_ddd_exists(Destino(0,""))

        self.assertEquals(len(destino_repository.lista_destino),1)
        self.assertTrue(resultOK)
        self.assertFalse(resultNOK)

    def test_check_if_destiny_is_right(self):
        destino_repository = DestinoRepository()
        destino_repository.lista_destino = []
        destino1 = Destino(1, "Test 1")

        ddd = 1

        destino_repository.set_catalog_item(destino1)
        destino_repository.check_if_ddd_exists(destino1)
        cidade = destino_repository.obter_destino_pelo_ddd(ddd)

        self.assertEquals(cidade,destino1.destino)

    def test_check_if_user_input_is_right(self):
        with mock.patch('builtins.input', return_value="1"):
            user = InterfaceUser(DestinoRepository())
            user_input = user.get_user_input()
            destino1 = Destino(1,"Test1")

            self.assertEquals(destino1.ddd, user_input)

