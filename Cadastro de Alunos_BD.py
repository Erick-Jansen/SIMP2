import os
import datetime


alunos = []
contador_aluno = 0



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

def gerar_matricula():
    global contador_aluno
    agora = datetime.datetime.now()
    ano = agora.year
    mes = agora.month
    contador_aluno += 1
    numero_sequencial = f'{contador_aluno:04d}'
    matricula = f'{ano}{mes:02d}{numero_sequencial}'
    return matricula



def cadastrar_aluno():
    nome = input(f'Insira o nome do aluno: ')
    idade = int(input(f'Insira a idade do aluno: '))
    email = input(f'Insira o e-mail do aluno: ')
    contato = int(input(f'Inserir o número para contato: '))
    matricula = gerar_matricula

    aluno = {
    'nome' : nome,
    'idade': idade,
    'email': email,
    'contato': contato,
    'matricula': matricula
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso! Matrícula: \n{matricula}")


def consultar_aluno():
    # Implementar a funcionalidade de consulta de aluno
    pass

def excluir_aluno():
    # Implementar a funcionalidade de exclusão de aluno
    pass

if __name__ == "__main__":
    menu()

