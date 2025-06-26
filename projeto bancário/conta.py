class conta:
    def __init__(self,titular,numero,saldo ):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
#================================================================================
    @property
    def get_numero(self):
        return self.saldo
    def set_saldo(self,saldo):
        if (saldo < 0):
            print("o saldo não pode ser negativo")

# ================================================================================
# Metodo de saque
    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo = valor
            print("saque realizado com sucesso! ")
        else:
             print("saldo insuficiente")
#================================================================================
# Metodo de depósito
    def depósito(self, valor):
        self.saldo+=valor
        print("depósito realizado com successo! ")
#================================================================================
# Extrato
    def extrato(self):
        print("Cliente",self.titular,"saldo atual",self.saldo)