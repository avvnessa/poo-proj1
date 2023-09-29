from pessoa import Pessoa

class Motoca:

    def __init__(self, potencia = 0, pessoa = None, tempo = 0):
        self.potencia = potencia
        self.pessoa = pessoa
        self.tempo = tempo

    def getPessoa(self):
        return self.pessoa

    def getTempo(self):
        return self.tempo

    def getPotencia(self):
        return self.potencia

    def subir(self, pessoa: Pessoa):
        if self.pessoa == None:
            self.pessoa = pessoa
            return True
        else:
            return False

    def descer(self):
        if self.pessoa is not None:
            self.pessoa = None
            return True
        else:
            return False

    def colocarTempo(self, tempo: int):
        if tempo <= 0:
            return False
        else:
            self.tempo = tempo
            return True

    def dirigir(self, tempo: int):
        if self.pessoa:
            if self.pessoa.getIdade() <= 10 and self.tempo > 0:
                if self.tempo >= tempo:
                    self.tempo -= tempo
                    return True
                if self.tempo < tempo:
                    self.tempo = 0
                    return True
        else:
            return False

    def buzinar(self):
        if self.pessoa:
            potencia2 = ""
            i = 1
            while i <= self.potencia:
                potencia2 += "e"
                i+=1
            buzina = "P" + potencia2 + "m"
        else:
            buzina = ""

        return buzina