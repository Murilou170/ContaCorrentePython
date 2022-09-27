class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
        else:
            Conta.saque(self, valor)

class CartaoCredito:
    def __init__(self, número, limite = 0, débito =0):
        Conta.__init__(self, número, operações, débito)
        def compra(self, valor, limite):
            if self.limite >= valor:
                self.limite -= valor
                self.débito += valor
                self.operações.append(["Compra no Crédito", valor])
            else:
                print("Limite insuficiente")
        
        def pagFatura(self, valor, limite):
            if self.valor <= self.débito:
                self.débito -= self.valor
                self.limite += valor
                self.operações.append(["Pagamento de fatura", valor])
            else:
                print('Pagamento inválido')


# //componetizar para reusar quando usar a classe do cartão de credito 


def main():
    valor = 0
    valor = int(input("valor da operação: "))
    print(valor)
# aqui você vai fazer os testes
# chama as classes e faz as operações pra ver se tudo dar certo
# falta compotetizar, como eu nunca fiz essa prática em python eu me arrisco fazer
# além de que quando componetizamos essa prática requer que você crie novos arquivos
# não sei se seu professor quer que envie vários arquivos
# então meu conselho é você fazer as etapas de testes E componetizar 
# provavelmente algum maluco da tua faculdade já fez esse main, confere ai e muda as váriáveis se for o caso



    print("Fim do programa")

main()