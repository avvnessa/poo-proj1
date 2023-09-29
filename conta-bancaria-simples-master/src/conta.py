class Conta:
    def __init__(self, numero:int, saldo:float):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = 100
        self.__extrato = []

    def getNumero(self):
        return self.__numero

    def getSaldo(self):
        return self.__saldo+self.__limite

    def getLimite(self):
        return self.__limite

    def sacar(self, valor: float):
        if valor > 0:
            saldoso = self.getSaldo()
            if saldoso >= valor > 0:
                self.__saldo -= valor
                if self.__saldo < 0:
                    self.__limite += self.__saldo
                    self.__saldo = 0
                self.__extrato.append(-valor)
                return True

    def depositar(self, valor: float):
        if valor > 0:
            self.__extrato.append(valor)
            if self.__limite < 100:
                self.__limite += valor
                newval = self.__limite - 100
                if newval > 0:
                    self.__limite -= newval
                    self.__saldo += newval
            else:
                self.__saldo += valor
            return True

    def transferir(self, destino, valor:float):
        conta1 = destino

        if conta1 != None and valor > 0:
            saldoso = self.getSaldo()
            if saldoso >= valor > 0:
                self.sacar(valor)
                conta1.depositar(valor)
                return True
        else:
            conta = None

    def verExtrato(self):
        return self.__extrato