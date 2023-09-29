class Carro:
    def __init__(self):
        self.combustivel = 0
        self.quilometragem = 0
        self.passageiros = 0
        self.limite_pessoas = 2
        self.limite_tanque = 100

    def getPassageiros(self):
        return self.passageiros

    def getCombustivel(self):
        return self.combustivel

    def getQuilometragem(self):
        return self.quilometragem

    def embarcar(self):
        if self.passageiros < 2:
            self.passageiros = self.passageiros + 1
            return True
        else:
            return False

    def desembarcar(self):
        if self.passageiros > 0:
            self.passageiros = self.passageiros - 1
            return True
        else:
            return False

    def dirigir(self, distancia):
        if self.passageiros == 0 or self.combustivel == 0:
            return False

        else:
            if self.combustivel - distancia < 0:
                self.quilometragem = self.quilometragem + (self.combustivel)
                self.combustivel = 0
                return False

            else:
                self.quilometragem = self.quilometragem + distancia
                self.combustivel = self.combustivel - distancia
                return True

    def abastecer(self, quantidade):
        if quantidade > 0:
            self.combustivel += quantidade
            if self.combustivel > 100:
                self.combustivel = 100
            return True
        else:
            return False