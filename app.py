import os
import textwrap

menu = """
======================
= [d] Depositar      =
= [s] Sacar          =
= [e] Extrato        =
= [q] Sair           =
= [nu] Novo Usuário  =
= [nc] Nova Conta    =
= [lc] Listar Contas =
======================

Digite a operação => """

saldo = 0
limite = 500
extrato = {}
linha_extrato = 0
numero_saques = 0
ultima_operacao = ''
usuarios = []
contas = []
AGENCIA = "0001"

LIMITES_SAQUES = 3


def criar_usuarios(usuarios):
    cpf = input("Digite o CPF (somente número): ")
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (Logradouro, num - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def busca_usuario(cpf, usuarios):
    filtra_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtra_usuario[0] if filtra_usuario else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = busca_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


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
    elif opcao == 'nu':
        os.system('cls')
        criar_usuarios(usuarios)
    elif opcao == 'nc':
        os.system('cls')
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == 'lc':
        os.system('cls')
        listar_contas(contas)
    else:
        os.system('cls')
        print('Operação inválida, por favor selecione \
novamente a operação desejada ')
