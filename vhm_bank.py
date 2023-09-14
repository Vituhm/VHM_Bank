#algoritmo de sistema bancario simples com correção pelo GPT na estrutura de decisão para tratamento de exceções (entradas inválidas)
import os
#função para depósito na conta
def deposito(clientes, conta, valor):
    for cliente in clientes:
        if cliente['conta'] == conta:
            cliente['saldo'] += valor
            print("Depósito de R$",valor, "realizado com sucesso!")
            break  #encerra o loop assim que a conta for encontrada

#função para saque na conta
def saque(clientes, conta, valor):
    for cliente in clientes:
        if cliente['conta'] == conta:
            if cliente['saldo'] >= valor:
                cliente['saldo'] -= valor
                print("Saque de R$",valor, "realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
            break  #encerra o loop assim que a conta for encontrada

#função para exibir o saldo atual da conta
def saldo(clientes, conta):
    os.system("cls")
    for cliente in clientes:
        if cliente['conta'] == conta:
            print("Saldo em conta: R$",cliente['saldo'])
            break  #encerra o loop assim que a conta for encontrada

#função para transferência de valores de uma conta para outra
def pix(clientes, conta, valor):
    for cliente in clientes:
        if cliente['conta'] == conta:
            if cliente['saldo'] >= valor:
                cliente['saldo'] -= valor
                print("Transferência de R$",valor, "realizada com sucesso!")
            else:
                print("Saldo insuficiente para realizar a transferência.")
            break  #encerra o loop assim que a conta for encontrada

clientes = [
    {"nome": "José", "saldo": 5000.0, "conta": 1122}, {"nome": "Maria", "saldo": 18000.0, "conta": 2233},
    {"nome": "Pedro", "saldo": 0.0, "conta": 3344}, {"nome": "João", "saldo": 3500.0, "conta": 4455}
]
#loop principal com verificação do cliente e conta
while True:
    print("____________________________________")
    print("______________SYS_BANK______________")
    cliente = input("Nome:")
    conta = input("N° da conta:")
    os.system("cls")

    #loop principal com as opções
    while True:
        print("____________________________________")
        print("______________SYS_BANK______________")
        print("-- Selecione uma opção --")
        print("1) Depósito")
        print("2) Saque")
        print("3) Consultar Saldo")
        print("4) Área PIX")
        print("5) Sair")
        print("____________________________________")

        op = input("Escolha uma opção: ")
        os.system("cls")

        #estrutura de decisão com checagem de erros, para informações inválidas
        try:
            if op == "1":
                valor = float(input("Informe o valor desejado:"))
                deposito(clientes, int(conta), valor)
            elif op == "2":
                valor = float(input("Informe o valor desejado:"))
                saque(clientes, int(conta), valor)
            elif op == "3":
                saldo(clientes, int(conta))
            elif op == "4":
                valor = float(input("Informe o valor desejado:"))
                pix(clientes, int(conta), valor)
            elif op == "5":
                print("Volte sempre!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de inserir um número válido.")