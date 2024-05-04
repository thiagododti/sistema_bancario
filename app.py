import os

menu = """[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Digite a operação => """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        os.system('cls')
        print('Deposito')
    elif opcao == 's':
        os.system('cls')
        print('Saque')
    elif opcao == 'e':
        os.system('cls')
        print('Extrato')
    elif opcao == 'q':
        break
    else:
        os.system('cls')
        print('Operação inválida, por favor selecione \
novamente a operação desejada ')
