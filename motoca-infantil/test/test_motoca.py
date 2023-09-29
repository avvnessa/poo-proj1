import unittest
import sys
sys.path.append('../../motoca')
sys.path.append('')

from src.motoca import Motoca
from src.pessoa import Pessoa

class TesteMotoca(unittest.TestCase):

    def testInicializacao(self):
        motoca = Motoca(5)
        self.assertIsNone(motoca.getPessoa(),"Ao criar uma motocicleta ela deve vir sem nenhuma pessoa [null].")
        self.assertEqual(0, motoca.getTempo(),"Ao criar uma motocicleta ela deve vir com tempo 0.")
        self.assertEqual(5, motoca.getPotencia(),"Ao criar uma motocicleta ela deve vir com a potência exata ao que foi passado na inicialização")

    def testSubida(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Vanessa", 5)
        self.assertTrue(motoca.subir(pessoa),"Se não haver nenhuma pessoa na motocicleta, então era poderá embarcar.")
        self.assertEqual(pessoa, motoca.getPessoa(), "A pessoa dirigindo nao e a mesma que subiu")

    def testSubidaMotocaCheia(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Tayane", 6)
        motoca.subir(pessoa)
        self.assertFalse(motoca.subir(Pessoa("Maria", 3)),"Não deve ser possível uma pessoa embarca se já tiver alguém embarcado.")
        self.assertEqual(pessoa, motoca.getPessoa(), "A pessoa dirigindo nao e a correta")

    def testDescerMotocaVazia(self):
        motoca = Motoca(5)
        self.assertFalse(motoca.descer(),"Não deve ser possível desembarcar se não houver ninguem na motocicleta.")

    def testDescerDaMotoca(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Laura", 8)
        motoca.subir(pessoa)
        self.assertTrue(motoca.descer(),"Deve ser possível desembarcar se houver uma pessoa na motocicleta")
        self.assertIsNone(motoca.getPessoa(), "A motoca deveria estar vazia")

    def testDirgirSemPiloto(self):
        motoca = Motoca(5)
        self.assertFalse(motoca.dirigir(5),"Não deve ser possível dirigir se não houver ninguem na motocicleta.")

    def testAdicionandoTempo(self):
        motoca = Motoca(10)
        self.assertTrue(motoca.colocarTempo(10), "O tempo nao foi adicionado")
        self.assertEqual(10, motoca.getTempo(), "O tempo registrado e diferente do adicionado")

    def testAdicionandoTempoNegativo(self):
        motoca = Motoca(10)
        self.assertTrue(motoca.colocarTempo(10), "O tempo nao foi adicionado")
        self.assertEqual(10, motoca.getTempo(), "O tempo registrado e diferente do adicionado")
        self.assertFalse(motoca.colocarTempo(-10), "Nao deve ser possivel adicionar um valor negativo de tmepo")
        self.assertEqual(10, motoca.getTempo(),"A quantidade de tempo nao deve ser alterada apos uma operacao invalida")

    def testDirigirSemTempo(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Davi", 3)
        motoca.subir(pessoa)
        self.assertFalse(motoca.dirigir(5),"Não deve ser possível dirigir se não houver comprado tempo.")
        self.assertEqual(0, motoca.getTempo(), "Nao foi adicionado tempo")

    def testDirigirSemPermissao(self):
        motoca = Motoca(5)
        pessoa = Pessoa("João", 11)
        motoca.subir(pessoa)
        motoca.colocarTempo(10)
        self.assertFalse(motoca.dirigir(5), "Não deve ser possível dirigir se não tiver a idade recomendada.")
        self.assertEqual(pessoa, motoca.getPessoa(), "A pessoa dirigindo nao e a mesma que subiu")

    def testDirgirComTempoSobrando(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Leo", 7)
        motoca.subir(pessoa)
        motoca.colocarTempo(20)
        self.assertEqual(pessoa, motoca.getPessoa(), "A pessoa dirigindo nao e a mesma que subiu")
        self.assertTrue(motoca.dirigir(10),"Ao comprar tempo deve ser possível dirigir na motocicleta")
        self.assertEqual(10, motoca.getTempo(),"Ao dirigir por um determinado tempo menor ao comprado deve restar a quantidade exata não usada.")

    def testDirigirAteAcabarTempo(self):
        motoca = Motoca(5)
        pessoa = Pessoa("Vanessa", 5)
        motoca.subir(pessoa)
        motoca.colocarTempo(20)
        self.assertTrue(motoca.dirigir(25), "Deve ser possivel dirigir ate zerar a quantidade de tempo")
        self.assertEqual(pessoa, motoca.getPessoa(), "A pessoa dirigindo nao e a mesma que subiu")
        self.assertEqual(0, motoca.getTempo(),"Não deve ser possível andar mais do que o tempo comprado.")

    def testBuzinar(self):
        motoca = Motoca(5)
        self.assertEqual("", motoca.buzinar(),"Não deve ser possível buzinar se não houver ninguem na motocicleta.")
        pessoa = Pessoa("Pedro", 5)
        motoca.subir(pessoa)
        self.assertEqual("Peeeeem", motoca.buzinar(),"Ao buzinar deve ser possível ver uma string com a quantidade de e equivalente ao número da potencia")


if __name__ == '__main__':
    unittest.main()