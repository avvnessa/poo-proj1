from src.motoca import Motoca
from src.pessoa import Pessoa

if __name__ == '__main__':
    #Inicializando a motocicleta
    motocicleta = Motoca(5)
    print(motocicleta)

    #Embarcando na motocicleta
    motocicleta.subir(Pessoa("João", 5))
    print(motocicleta)

    if not motocicleta.subir(Pessoa("Maria", 6)):
        print(motocicleta)

    # Embarcando e buzinando
    motocicleta = Motoca(5)
    motocicleta.subir(Pessoa("Ana", 4))
    print(motocicleta)
    print(motocicleta.buzinar())

    #Embarcando e desembarcando na motocicleta
    motocicleta = Motoca(5)
    motocicleta.subir(Pessoa("Heitor", 3))
    print(motocicleta)
    motocicleta.descer()
    if not motocicleta.descer():
        print("fail: moto desocupada")

    motocicleta.subir(Pessoa("Alice", 8))
    print(motocicleta)

    # Passeando na motocicleta
    motocicleta = Motoca(7)
    motocicleta.subir(Pessoa("Biatriz", 6))
    if not motocicleta.dirigir(10):
        print("fail: tempo zerado")

    motocicleta.colocarTempo(40)
    print(motocicleta)
    motocicleta.dirigir(20)
    print(motocicleta)

    # Passeando na motocicleta sem idade recomendada
    motocicleta = Motoca(7)
    motocicleta.subir(Pessoa("Edu", 15))
    motocicleta.colocarTempo(20)
    if not motocicleta.dirigir(15):
        print("fail: a pessoa está fora da idade recomanda para andar.")

    print(motocicleta)

    #Passeando com tempo esgotado
    mmotocicleta = Motoca(7)
    motocicleta.subir(Pessoa("Gutavo", 9))
    motocicleta.colocarTempo(20)
    motocicleta.dirigir(20)
    print(motocicleta)
    motocicleta.dirigir(10)