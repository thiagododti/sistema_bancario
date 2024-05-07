import os

menu = """
##################
# [d] Depositar  #
# [s] Sacar      #
# [e] Extrato    #
# [q] Sair       #
##################

Digite a operação => """

saldo = 0
limite = 500
extrato = {}
linha_extrato = 0
numero_saques = 0
ultima_operacao = ''

LIMITES_SAQUES = 3


def alimenta_extrato(operacao, valor):
    global extrato
    global linha_extrato

    extrato[linha_extrato] = [operacao, valor]
    linha_extrato += 1


def deposito(valor):
    global saldo
    global ultima_operacao

    if valor <= 0:
        print('Não é possivel depositar valores negativos ou zerados!')
    else:
        saldo += valor
        ultima_operacao = 'Deposito'
        alimenta_extrato(ultima_operacao, valor)


def saque(valor):
    global saldo
    global ultima_operacao
    global limite
    global numero_saques

    if valor > limite:
        print(f"Limite de R${limite} de saque ultrapassado.")
    elif valor > saldo:
        print(f"Saldo insuficiente para operação: Saldo: R${saldo}")
    elif numero_saques > 2:
        print("Limite de saques diarios ultrapassado.")
    else:
        saldo -= valor
        ultima_operacao = 'Saque'
        numero_saques += 1
        alimenta_extrato(ultima_operacao, valor)


while True:
    opcao = input(menu)
    if opcao == 'd':
        os.system('cls')
        deposito(float(input("Valor do deposito: R$")))
    elif opcao == 's':
        os.system('cls')
        saque(float(input("Valor do saque: R$")))
    elif opcao == 'e':
        os.system('cls')
        for e in extrato:
            print(f"{extrato[e][0]}: R$ {extrato[e][1]}")
        print(f"Saldo da conta: R$ {saldo}")

    elif opcao == 'q':
        break
    else:
        os.system('cls')
        print('Operação inválida, por favor selecione \
novamente a operação desejada ')
