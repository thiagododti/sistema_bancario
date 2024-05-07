import os

menu = """[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a operação => """

saldo = 0
limite = 500
extrato = []
linha_extrato = 0
numero_saques = 0
ultima_operacao = ''
LIMITES_SAQUES = 3


def alimenta_extrato(operacao, valor):
    global extrato
    global linha_extrato

    extrato.append(f"{linha_extrato}: {operacao}: R$ {valor}")


def deposito(valor):
    global saldo
    global ultima_operacao
    if valor <= 0:
        print('Não é possivel depositar valores negativos ou zerados!')
    else:
        saldo += valor
        ultima_operacao = 'Deposito'
        alimenta_extrato(ultima_operacao, valor)


while True:
    opcao = input(menu)
    if opcao == 'd':
        os.system('cls')
        deposito(float(input()))
    elif opcao == 's':
        os.system('cls')
        print('Saque')
    elif opcao == 'e':
        os.system('cls')
        for e in len(extrato):
            print(extrato[e])
    elif opcao == 'q':
        break
    else:
        os.system('cls')
        print('Operação inválida, por favor selecione \
novamente a operação desejada ')
