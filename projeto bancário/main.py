class Main:
    pass
from cliente import Cliente
from conta import conta

c1 = Cliente("joão","54789869")
conta= conta(c1.nome,9284,0)
print(c1)
print("titular da conta: ", conta.titular,"/numero da conta: /",conta.numero,"seu saldo: ",conta.saldo)
#================================================================================
#Chamando os metodos
input("sacar?")
if 'sim ' in input:
    conta.depósito(100)
    