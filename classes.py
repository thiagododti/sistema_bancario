class Conta:
    def __init__(self, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        return self._saldo

    def nova_conta(self):
        pass

    def sacar(self, valor):
        if valor > self._saldo:
            print(f"Saldo insuficiente! Saldo atual: R$ {self._saldo}")
        else:
            self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, historico,
                 limite, limite_saques):
        super().__init__(numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques


class Historico(Conta):
    def __init__(self, numero, agencia, cliente, historico):
        super().__init__(numero, agencia, cliente, historico)

    def adicionar_transacao(self, transacao):
        pass
