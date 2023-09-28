class Conta:
    def __init__(self, numero:int, saldo:float):
        pass

    def getNumero(self):
        return 0

    def getSaldo(self):
        return 0.0

    def getLimite(self):
        return 0.0

    def sacar(self, valor: float):
        return False

    def depositar(self, valor: float):
        return True

    def transferir(self, destino, valor:float):
        return False

    def verExtrato(self):
        return None