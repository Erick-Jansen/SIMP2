import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    input("Sistema Bancário \nPressione Enter para prosseguir ou sair\n")
    return input("O que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")

def sacar(saldo, extrato):
    limpar_tela()
    saque = float(input(f"Extrato: R$ {saldo:.2f} \nQual o valor do saque?\n --> "))
    limpar_tela()
    if saldo >= saque > 0:
        print(f"Sacando: R$ {saque:.2f} \nExtrato atual: R$ {(saldo - saque):.2f}")
        extrato.append(f"Sacado o valor de R$ {saque:.2f}")
        saldo -= saque
    else:
        print(f"Saldo insuficiente \nSaldo: R$ {saldo:.2f}")
    return saldo

def depositar(saldo, extrato):
    limpar_tela()
    deposito = float(input(f"Extrato: R$ {saldo:.2f} \nQual o valor do depósito?\n --> "))
    limpar_tela()
    print(f"Depositando R$ {deposito:.2f} \nExtrato atual: R$ {(deposito + saldo):.2f}")
    extrato.append(f"Depositado o valor de R$ {deposito:.2f}\n")
    saldo += deposito
    return saldo

def visualizar_extrato(saldo, extrato):
    limpar_tela()
    print(f"Saldo atual: R$ {saldo:.2f}\n")
    for operacao in extrato:
        print(operacao)

def main():
    saldo = 1500
    extrato = []
    while True:
        escolha = menu()
        if escolha == "":
            break
        elif escolha == "1":
            saldo = sacar(saldo, extrato)
        elif escolha == "2":
            saldo = depositar(saldo, extrato)
        elif escolha == "3":
            visualizar_extrato(saldo, extrato)
        else:
            limpar_tela()
            print("Valor inválido")

    limpar_tela()
    print("\nFechando Sistema...\n\n")

if __name__ == "__main__":
    main()


