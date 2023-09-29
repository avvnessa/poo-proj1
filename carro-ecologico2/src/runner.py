from src.carro import Carro

if __name__ == '__main__':
    #Criando um carro
    carro = Carro()
    print(carro.__dict__)

    #Embarcando duas pessoas
    carro.embarcar()
    carro.embarcar()
    print(carro.__dict__)

    #Tentando embarcar mais uma pessoas
    if carro.embarcar():
        print("Nao foi possivel realizar o embarque")

    #Desembarcando
    carro.desembarcar()
    carro.desembarcar()
    if carro.desembarcar():
        print("Nao foi possivel desembarcar")

    #Abastecendo
    carro.abastecer(60)
    print(carro.__dict__)

    #Dirigir
    if carro.dirigir(10):
        print("Nao foi possivel dirigir porque o carro estava vazio")

    # Embarcando e dirigindo
    carro.embarcar()
    carro.dirigir(10)
    print(carro.__dict__)

    # Dirigindo ate acabar o combustivel
    quilometragemAntigo = carro.getQuilometragem()
    if carro.dirigir(70):
        distancia = carro.getQuilometragem() - quilometragemAntigo
        print("O combustivel acabou ao percorrer " + distancia + " kms")

    print(carro.__dict__)

    #Abastecendo
    carro.abastecer(200)
    print(carro.__dict__)
