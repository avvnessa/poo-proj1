class Pessoa:
    def __init__(self, nome: str, idade: str):
        self.nome = nome
        self.idade = idade

    def getIdade(self):
        return self.idade

    def getNome(self):
        return self.nome

    def __str__(self):
        return "[" + self.nome +":" + self.idade + "]"