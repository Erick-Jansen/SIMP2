import os
import datetime

# Inicialização de uma lista para armazenar os dados dos alunos
alunos = []
contador_aluno = 0

def gerar_matricula():
    global contador_aluno
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    contador_aluno += 1
    numero_sequencial = f'{contador_aluno:04d}'  # Número sequencial com 4 dígitos
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula

def calcular_idade(data_nascimento):
    hoje = datetime.datetime.now()
    idade_anos = hoje.year - data_nascimento.year
    idade_meses = hoje.month - data_nascimento.month

    if idade_meses < 0:
        idade_anos -= 1
        idade_meses += 12

    return idade_anos, idade_meses

def cadastrar_aluno():
    while True:
        nome = input('Insira o nome do aluno (nome e sobrenome): ')
        if ' ' in nome.strip() and all(part.isalpha() for part in nome.split()):
            break
        else:
            print("Por favor, insira um nome válido contendo apenas letras, com pelo menos um nome e um sobrenome.")
    
    while True:
        try:
            dia = int(input('Insira o dia de nascimento (DD): '))
            mes = int(input('Insira o mês de nascimento (MM): '))
            ano = int(input('Insira o ano de nascimento (AAAA): '))
            data_nascimento = datetime.datetime(ano, mes, dia)
            idade_anos, idade_meses = calcular_idade(data_nascimento)
            break
        except ValueError:
            print("Data de nascimento inválida. Tente novamente.")

    email = input('Insira o e-mail do aluno: ')
    endereco = input('Insira o endereço do aluno: ')
    contato_aluno = input('Insira o número de contato do aluno: ')
    nome_responsavel = input('Escreva o nome do responsável: ')
    contato_responsavel = input('Escreva o número para contato do responsável: ')
    identidade = input('Escreva o RG do aluno: ')
    grau_escolaridade = input('Qual o grau que o aluno está sendo matrículado?: ')
    
    matricula = gerar_matricula()
    
    aluno = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'idade_anos': idade_anos,
        'idade_meses': idade_meses,
        'email': email,
        'endereco': endereco,
        'contato_aluno': contato_aluno,
        'nome_responsavel': nome_responsavel,
        'contato_responsavel': contato_responsavel,
        'grau_escolaridade': grau_escolaridade,
        'matricula': matricula,
        'identidade': identidade,
    }
    
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: {matricula}\n")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def consultar_aluno():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade_anos']} anos e {aluno['idade_meses']} meses, E-mail: {aluno['email']}, Contato: {aluno['contato_aluno']}, Matrícula: {aluno['matricula']}")
        print("")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def excluir_aluno():
    os.system('cls' if os.name == 'nt' else 'clear')
    matricula = input("Digite a matrícula do aluno a ser excluído: ")
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            confirmar = input(f'Você tem certeza que gostaria de excluir o aluno {aluno["nome"]} do sistema? \n Se sim, confirme com "s", caso não tecle enter. \n--> ')
            if confirmar.lower() == 's':
                alunos.remove(aluno)
                print(f"Aluno com matrícula {matricula} excluído com sucesso!\n")
            else:
                print("Exclusão cancelada.\n")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            return
    print(f"Aluno com matrícula {matricula} não encontrado.\n")
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\nMenu Principal: \n")
        print("1. Cadastrar Aluno")
        print("2. Consultar Aluno")
        print("3. Excluir Aluno")
        print("4. Sair")
        opcao = input("Digite sua opção: \n -->")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            excluir_aluno()
        elif opcao == "4":
            break
        else:
            print("Opção inválida! Escolha uma das opções disponíveis")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    menu()



