import unittest

from src.carro import Carro


class TestCarro(unittest.TestCase):
    carro = None

    @classmethod
    def setUp(cls):
        cls.carro = Carro()

    def testInicializacao(self):
        self.assertEqual(0, self.carro.getPassageiros(),"Ao inicializar um carro o numero de passageiros deve ser zero")
        self.assertEqual(0, self.carro.getCombustivel(), "Ao inicializar um carro a quantidade de combustivel deve ser zero")

    def testEmbarque(self):
        self.assertTrue(self.carro.embarcar(),"Como o carro estava vazio, deve ser possivel embarcar")
        self.assertEqual(1, self.carro.getPassageiros())

    def testEmbarqueEmCarroLotado(self):
        self.carro.embarcar()
        self.carro.embarcar()
        self.assertFalse(self.carro.embarcar(),"Como o carro estava cheio (2 passageiros), nao deve ser possivel embarcar")
        self.assertEqual(2, self.carro.getPassageiros())

    def testDesembarqueEmCarroVazio(self):
        self.assertFalse(self.carro.desembarcar(),  "Como o carro estava vazio, nao deve ser possivel desembarcar" )
        self.assertEqual(0, self.carro.getPassageiros())

    def testDesembarque(self):
        self.carro.embarcar()
        self.assertTrue(self.carro.desembarcar(),"Como o carro nao estava vazio, deve ser possivel desembarcar")
        self.carro.embarcar()
        self.carro.embarcar()
        self.assertTrue(self.carro.desembarcar(),"Como o carro nao estava vazio, deve ser possivel desembarcar" )
        self.assertTrue(self.carro.desembarcar(),"Como o carro nao estava vazio, deve ser possivel desembarcar" )

    def testAbastecerComValorInvalido(self):
        self.assertFalse(self.carro.abastecer(-30),"A quantidade de combustivel deve ser uma valor positivo")
        self.assertEqual(0, self.carro.getCombustivel())

    def testAbastecerSemCompletarTanque(self):
        self.assertTrue(self.carro.abastecer(186))
        self.assertEqual(100, self.carro.getCombustivel(), "O valor de combustivel desejado excede o tamanho do tanque. Logo o tanque fica cheio" )

    def testDirigirCarroVazio(self):
        self.assertFalse(self.carro.dirigir(10),"O carro está vazio, logo nao e possivel dirigi-lo")

    def testDirigirCurtaDistancia(self):
        self.carro.embarcar()
        self.carro.abastecer(32)
        self.assertTrue(self.carro.dirigir(10))
        self.assertEqual(22, self.carro.getCombustivel(),"O carro tinha 32 litros e percorreu uma distancia de 10 km")
        self.assertEqual(10, self.carro.getQuilometragem(), "O carro percorreu 10 km")

    def  testDirigirLongaDistancia(self):
        self.carro.embarcar()
        self.carro.abastecer(32)
        self.assertTrue(self.carro.dirigir(10))
        self.carro.embarcar()
        self.carro.abastecer(80)
        self.assertFalse(self.carro.dirigir(120))
        self.assertEqual(0, self.carro.getCombustivel(),  "A distancia percorrida consumiu todo o combustivel")
        self.assertEqual(110, self.carro.getQuilometragem(),"O carro percorreu 110 km")

    if __name__ == '__main__':
        unittest.main()
