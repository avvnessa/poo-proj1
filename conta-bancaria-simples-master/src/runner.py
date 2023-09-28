# Press the green button in the gutter to run the script.
from src.conta import Conta

if __name__ == '__main__':
    minhaConta = Conta(1001, 2000)
    print(minhaConta)
    
    destino = Conta(10, 0)
    print(destino)

    minhaConta.sacar(200)
    print(minhaConta)

    if minhaConta.sacar(10000):
        print("Saldo insuficiente")

    minhaConta.depositar(500)
    print(minhaConta)

    minhaConta.transferir(destino, 400)
    print(minhaConta)

    if minhaConta.transferir(destino,4000000):
        print("Saldo insuficiente")

    minhaConta.sacar(1950)
    print("Saldo insuficiente")

    minhaConta.depositar(50)
    print(minhaConta)

    extrato = minhaConta.verExtrato()
    for i in range(len(extrato)):
      print(extrato[i])
