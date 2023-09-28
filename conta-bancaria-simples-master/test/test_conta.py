import unittest

from src.conta import Conta


class TestConta(unittest.TestCase):
    conta = None

    @classmethod
    def setUp(cls):
        cls.conta = Conta(1001, 2000)

    def test_criarConta(self):
        self.assertEqual(1001, self.conta.getNumero(), "O numero da conta deve igual ao informado na criacao")
        self.assertEqual(100, self.conta.getLimite(),  "O valor do limite padrao de uma conta 100")
        self.assertEqual(2100, self.conta.getSaldo(), "O saldo deve ser igual ao limite + o saldo")

        conta = Conta(1010, 1000)
        self.assertEqual(1010, conta.getNumero(), "O numero da conta deve igual ao informado na criacao")
        self.assertEqual(100, conta.getLimite(), "O valor do limite padrao de uma conta 100")
        self.assertEqual(1100, conta.getSaldo(), "O saldo deve ser igual ao limite + o saldo")

    def test_varificarSaldo(self):
        self.assertEqual(2100, self.conta.getSaldo(), "O saldo deve ser igual ao limite + o saldo")

    def test_usuarioNaoPodeRealizarSaquesNegativos(self):
        self.assertFalse(self.conta.sacar(-100), "Sacar valores negativos nao deve ser permitido")
        self.assertEqual(2100, self.conta.getSaldo(), "O saldo deve permanecer inalterado")

    def test_usuarioNaoPoderSacarQuantiasMaioresQueOSaldo(self):
        self.assertFalse(self.conta.sacar(5000), "Saldo da conta insuficiente")
        self.assertEqual(2100, self.conta.getSaldo(),  "O saldo deve permanecer inalterado")

    def test_usuarioPodeSacarValoresUtilizandoOLimite(self):
        self.assertTrue(self.conta.sacar(2050), "Ao sacar um valor o limite da conta deve ser considerado")
        self.assertEqual(50, self.conta.getSaldo(), "Valor sacado maior que o saldo")
        self.assertEqual(50, self.conta.getLimite(), "O limite foi utilizado na operacao")

    def test_usuarioPodeSacarValoresSemUtilizarLimite(self):
        self.assertTrue(self.conta.sacar(1000), "Ao sacar um valor o limite da conta deve ser considerado")
        self.assertEqual(1100, self.conta.getSaldo(),  "Valor sacado maior que o saldo")
        self.assertEqual(100, self.conta.getLimite(),  "O limite nao foi utilizado na operacao")

    def test_usuarioNaoDepositarValoresNegativos(self):
        self.assertFalse(self.conta.depositar(-100), "Depositar valores negativos nao deve ser permitido")
        self.assertEqual(2100, self.conta.getSaldo(), "O saldo deve permanecer inalterado")

    def test_usuarioPodeDepositarValoresPositivos(self):
        self.assertTrue(self.conta.depositar(900), "Depositar valores nao negativos deve ser permitido")
        self.assertEqual(3000, self.conta.getSaldo(),  "O saldo nao atualizado corretamente")

    def test_depositosEmContasComLimiteUtilizadoDevemRestaurarOLimite(self):
        self.conta.sacar(2100)

        self.assertTrue(self.conta.depositar(50), "Depositar valores positivos sao permitidos")
        self.assertEqual(50, self.conta.getSaldo(),  "O saldo nao atualizado corretamente")
        self.assertEqual(50, self.conta.getLimite(), "Limite nao restaurado")

        self.assertTrue(self.conta.depositar(100), "Depositar valores positivos sao permitidos")
        self.assertEqual(150, self.conta.getSaldo(), "O saldo nao atualizado corretamente")
        self.assertEqual(100, self.conta.getLimite(), "Limite nao restaurado")

    def test_usuarioNaoPodeTransferirQuantiasNegativas(self):
        destino = Conta(10, 0)
        self.assertFalse(self.conta.transferir(destino, -50), "Transferir valores negativos nao e permitido")

    def test_usuarioNaoPodeTransferirQuantiasMaioresQueOSaldo(self):
        destino = Conta(10, 0)
        self.assertFalse(self.conta.transferir(destino, 3000), "Transferir valores negativos nao e permitido")
        self.assertEqual(2100, self.conta.getSaldo(), "O saldo deve permanecer inalterado")
        self.assertEqual(100, destino.getSaldo(),"O saldo deve permanecer inalterado")

    def test_usuarioPodeTransferirQuantiasUtilizandoLimite(self):
        destino = Conta(10, 0)
        self.assertTrue(self.conta.transferir(destino, 2050), "Transferir valores negativos nao e permitido")
        self.assertEqual(50, self.conta.getSaldo(), "Valor sacado maior que o saldo")
        self.assertEqual(50, self.conta.getLimite(), "O limite foi utilizado na operacao")
        self.assertEqual(2150, destino.getSaldo(), "O saldo deve permanecer inalterado")

    def test_usuarioPodeTransferirQuantiasSemUsarLimite(self):
        destino = Conta(10, 0)
        self.assertTrue(self.conta.transferir(destino, 1000), "Transferir valores negativos nao e permitido")
        self.assertEqual(1100, self.conta.getSaldo(), "Valor sacado maior que o saldo")
        self.assertEqual(100, self.conta.getLimite(), "O limite nao foi utilizado na operacao")
        self.assertEqual(1100, self.conta.getSaldo(), "O saldo deve permanecer inalterado")

    def test_verificaExtrato(self):
        destino = Conta(10, 0)
        self.conta.sacar(200)
        self.conta.sacar(10000)
        self.conta.depositar(500)
        self.conta.transferir(destino, 400)
        self.conta.transferir(destino, 4000000)
        self.conta.sacar(1950)
        self.conta.depositar(50)

        extratoCorreto = [-200.0, 500.0, -400.0, -1950.0, 50.0]
        extrato = self.conta.verExtrato()
        self.assertListEqual(extrato, extratoCorreto, "O extrato nao confere")

if __name__ == '__main__':
    unittest.main()
